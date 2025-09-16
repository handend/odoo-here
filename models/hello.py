from odoo import models, fields, api

class CandidateSurvey(models.Model):
    _name = "candidate.survey"
    _description = "Candidate Survey"

    # Aday bilgileri
    name = fields.Char("Full Name", required=True)
    email = fields.Char("Email")
    phone = fields.Char("Phone")

    # Sorular
    question1 = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string="Do you meet requirement 1?")
    question2 = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string="Do you meet requirement 2?")

    # Eligibility
    eligible = fields.Boolean("Eligible", compute="_compute_eligibility", store=True)

    @api.depends("question1", "question2")
    def _compute_eligibility(self):
        for rec in self:
            rec.eligible = (rec.question1 == 'yes' and rec.question2 == 'yes')

    # Butonla yönlendirme
    def action_go_to_appointment(self):
        """Redirects to Appointments module if eligible"""
        if self.eligible:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Appointments',
                'res_model': 'appointment.type',
                'view_mode': 'calendar,tree,form',
                'target': 'current',
            }
        else:
            return False