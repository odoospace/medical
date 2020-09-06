# Copyright 2008 Luis Falcon <falcon@gnuhealth.org>
# Copyright 2015 Acsone.
# Copyright 2020 LabViv.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import fields, models


class MedicalPatientMedication(models.Model):
    _name = 'medical.patient.medication'
    _description = 'Medical Patient Medication'
    _inherit = ['abstract.medical.medication', 'medical.medication.template']
    _rec_name = 'patient_id'

    medication_template_id = fields.Many2one(
        comodel_name='medical.medication.template',
        string='Medication Template', index=True)
    patient_id = fields.Many2one(
        comodel_name='medical.patient', string='Patient', index=True,
        required=True)
    physician_id = fields.Many2one(
        comodel_name='medical.practitioner', string='Physician',
        help='Physician who prescribed the medicament', index=True)
    active = fields.Boolean(
        help='Check if the patient is currently taking the medication',
        default=True)
    is_course_complete = fields.Boolean(string='Course Completed')
    is_discontinued = fields.Boolean()
    date_start_treatment = fields.Datetime()
    date_stop_treatment = fields.Datetime()
    discontinued_reason = fields.Char(
        help='Short description for discontinuing the treatment')
    adverse_reaction = fields.Text(
        help='Side effects or adverse reactions that patient experienced')
    notes = fields.Text()
