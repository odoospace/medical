# Copyright 2008-2020 Luis Falcon.
# Copyright 2011-2020 GNU Solidario.
# Copyright 2020 LabViv.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import models, fields, api
from datetime import datetime


class VegetarianTypes(models.Model):
    _name = 'medical.vegetarian_types'
    _description = 'Vegetarian Types'

    name = fields.Char(
        string='Vegetarian',
        translate=True,
        required=True,
        help="Vegetarian"
    )
    code = fields.Char(
        string='Code',
        required=True,
        help="Short description"
    )
    desc = fields.Char(
        string='Description',
        required=True,
        help="Short description"
    )


# Diet by belief / religion
class DietBelief(models.Model):
    _name = "medical.diet.belief"
    _description = 'Diet by Belief'

    name = fields.Char(
        string='Belief',
        required=True,
        translate=True
    )
    code = fields.Char(
        string='Code',
        required=True
    )
    description = fields.Text(
        string='Description',
        required=True,
        translate=True
    )

    _sql_constraints = [(
        'code_uniq', 'unique(name)',
        'The Diet code already exists'
    )]


class DrugsRecreational(models.Model):
    _name = 'medical.drugs_recreational'
    _description = 'Recreational Drug'

    name = fields.Char(
        string='Name',
        translate=True,
        required=True,
        help="Name of the drug"
    )
    code = fields.Char(
        string='Code',
        required=True,
        help="Please use CAPITAL LETTERS and no spaces"
    )
    street_name = fields.Char(
        string='Street names',
        help="Common name of the drug in street jargon"
    )
    toxicity = fields.Selection(
        [
            ('0', 'None'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Extreme'),
        ],
        string='Toxicity',
        sort=False
    )
    addiction_level = fields.Selection(
        [
            ('0', 'None'),
            ('1', 'Low'),
            ('2', 'High'),
            ('3', 'Extreme'),
        ],
        string='Addiction level',
        sort=False
    )
    legal_status = fields.Selection(
        [
            ('0', 'Legal'),
            ('1', 'Illegal'),
        ],
        string='Legal Status',
        sort=False
    )
    category = fields.Selection(
        [
            ('cannabinoid', 'Cannabinoids'),
            ('depressant', 'Depressants'),
            ('dissociative', 'Dissociative Anesthetics'),
            ('hallucinogen', 'Hallucinogens'),
            ('opioid', 'Opioids'),
            ('stimulant', 'Stimulants'),
            ('other', 'Others'),
        ],
        string='Category',
        sort=False
    )
    withdrawal_level = fields.Integer(
        string='Withdrawal',
        help="Presence and severity of characteristic withdrawal symptoms.\n"
             "Using Henningfield rating. 1=highest and 6=lowest"
    )
    reinforcement_level = fields.Integer(
        string='Reinforcement',
        help="A measure of the substance's ability to get users to take it "
             " again and again, and in preference to other substances.\n"
             "Using Henningfield rating. 1=highest and 6=lowest"
    )
    tolerance_level = fields.Integer(
        string='Tolerance',
        help="How much of the substance is needed to satisfy increasing "
             "cravings for it, and the level of stable need that is eventually "
             "reached.\n"
             "Using Henningfield rating. 1=highest and 6=lowest"
    )
    dependence_level = fields.Integer(
        string='Dependence',
        help="How difficult it is for the user to quit, the relapse rate, "
             "the percentage of people who eventually become dependent, the "
             "rating users give their own need for the substance and the "
             "degree to which the substance will be used in the face of "
             "evidence that it causes harm.\nUsing Henningfield rating. "
             "1=highest and 6=lowest"
    )
    intoxication_level = fields.Integer(
        string='Intoxication',
        help="the level of intoxication is associated with addiction and "
             "increases the personal and social damage a substance may do. \n"
             "Using Henningfield rating."
             "1=highest and 6=lowest"
    )
    route_oral = fields.Boolean(string='Oral')
    route_popping = fields.Boolean(
        string='Skin Popping',
        help="Subcutaneous or Intradermical administration"
    )
    route_inhaling = fields.Boolean(
        string='Smoke / Inhale',
        help="Insufflation, excluding nasal"
    )
    route_sniffing = fields.Boolean(
        string='Sniffing',
        help="Also called snorting - inhaling through the nares"
    )
    route_injection = fields.Boolean(
        string='Injection',
        help="Injection - Intravenous, Intramuscular..."
    )
    dea_schedule_i = fields.Boolean(
        string='DEA schedule I',
        help="Schedule I and II drugs have a high potential for abuse. "
             "They require greater storage security and have a quota on "
             "manufacturing, among other restrictions. Schedule I drugs are "
             "available for research only and have no approved medical use; "
             "Schedule II drugs are available only by prescription "
             "(unrefillable) and require a form for ordering. Schedule III "
             "and IV drugs are available by prescription, may have five "
             "refills in 6 months, and may be ordered orally. "
             "Some Schedule V drugs are available over the counter"
    )
    dea_schedule_ii = fields.Boolean(
        string='II',
        help="Schedule I and II drugs have a high potential for abuse."
             "They require greater storage security and have a quota on"
             "manufacturing, among other restrictions. Schedule I drugs are"
             "available for research only and have no approved medical use; "
             "Schedule II drugs are available only by prescription "
             "(unrefillable) and require a form for ordering. Schedule III "
             "and IV drugs are available by prescription, may have five"
             "refills in 6 months, and may be ordered orally. "
             "Some Schedule V drugs are available over the counter"
    )
    dea_schedule_iii = fields.Boolean(
        string='III',
        help="Schedule I and II drugs have a high potential for abuse. "
             "They require greater storage security and have a quota on "
             "manufacturing, among other restrictions. Schedule I drugs are "
             "available for research only and have no approved medical use; "
             "Schedule II drugs are available only by prescription "
             "(unrefillable) and require a form for ordering. Schedule III "
             "and IV drugs are available by prescription, may have five "
             "refills in 6 months, and may be ordered orally. "
             "Some Schedule V drugs are available over the counter"
    )
    dea_schedule_iv = fields.Boolean(
        string='IV',
        help="Schedule I and II drugs have a high potential for abuse. "
             "They require greater storage security and have a quota on "
             "manufacturing, among other restrictions. Schedule I drugs are "
             "available for research only and have no approved medical use; "
             "Schedule II drugs are available only by prescription "
             "(unrefillable) and require a form for ordering. Schedule III "
             "and IV drugs are available by prescription, may have five "
             "refills in 6 months, and may be ordered orally. "
             "Some Schedule V drugs are available over the counter"
    )
    dea_schedule_v = fields.Boolean(
        string='V',
        help="Schedule I and II drugs have a high potential for abuse. "
             "They require greater storage security and have a quota on "
             "manufacturing, among other restrictions. Schedule I drugs are "
             "available for research only and have no approved medical use; "
             "Schedule II drugs are available only by prescription "
             "(unrefillable) and require a form for ordering. Schedule III "
             "and IV drugs are available by prescription, may have five "
             "refills in 6 months, and may be ordered orally. "
             "Some Schedule V drugs are available over the counter"
    )
    info = fields.Text(string='Extra Info')

    _sql_constraints = [
        (
            'name_unique',
            'unique(name)',
            'The Recreational Drug name must be unique'
        ), (
            'code_unique',
            'unique(code)',
            'The Recreational Drug CODE must be unique'
        )
    ]


class PatientRecreationalDrugs(models.Model):
    _name = 'medical.patient_recreational_drugs'
    _description = 'Patient use of Recreational Drugs'

    patient = fields.Many2one(
        'medical.patient',
        'Patient',
        required=True,
    )
    recreational_drug = fields.Many2one(
        'medical.drugs_recreational',
        string='Recreational Drug'
    )


class PatientCAGE(models.Model):
    '''CAGE questionnaire to assess patient dependency to alcohol'''
    _name = 'medical.patient.cage'
    _description = 'Patient CAGE Questionnaire'

    name = fields.Many2one(
        'medical.patient',
        'Patient',
        required=True
    )
    evaluation_date = fields.Datetime('Date')
    cage_c = fields.Boolean(
        'Hard to cut down',
        help='Have you ever felt you needed to cut down on your drinking?'
    )
    cage_a = fields.Boolean(
        'Angry with critics',
        help='Have people annoyed you by criticizing your drinking?'
    )
    cage_g = fields.Boolean(
        'Guilt',
        help='Have you ever felt guilty about drinking?'
    )
    cage_e = fields.Boolean(
        'Eye-opener',
        help='Have you ever felt you needed a drink first thing in the morning\
        (Eye-opener) to steady your nerves or to get rid of a hangover?'
    )
    cage_score = fields.Integer('CAGE Score')

    # Show the icon depending on the CAGE Score
    cage_warning_icon = fields.Char(
        'Cage Warning Icon',
        default='get_cage_warning_icon'
    )

    def get_cage_warning_icon(self, name):
        if (self.cage_score > 1):
            return 'gnuhealth-warning'

    @api.depends('cage_c', 'cage_a', 'cage_g', 'cage_e')
    def on_change_with_cage_score(self):
        total = 0
        if self.cage_c:
            total = total + 1
        if self.cage_a:
            total = total + 1
        if self.cage_g:
            total = total + 1
        if self.cage_e:
            total = total + 1
        return total

    @api.depends
    def default_evaluation_date():
        return datetime.now()

    @api.depends
    def default_cage_score():
        return 0


class MedicalPatient(models.Model):
    _name = 'medical.patient'
    _inherit = 'medical.patient'

    exercise = fields.Boolean('Exercise')
    exercise_minutes_day = fields.Integer(
        'Minutes / day',
        help="How many minutes a day the patient exercises"
    )
    sleep_hours = fields.Integer(
        'Hours of sleep',
        help="Average hours of sleep per day"
    )
    sleep_during_daytime = fields.Boolean(
        'Sleeps at daytime',
        help="Check if the patient sleeps during daylight rather than at night"
    )
    number_of_meals = fields.Integer('Meals per day')
    vegetarian_type = fields.Many2one(
        'medical.vegetarian_types',
        'Vegetarian'
    )
    diet_belief = fields.Many2one(
        'medical.diet.belief',
        'Belief',
        help="Enter the patient belief or religion"
    )
    eats_alone = fields.Boolean(
        'Eats alone',
        help="Check this box if the patient eats by him / herself."
    )
    salt = fields.Boolean(
        'Salt',
        help="Check if patient consumes salt with the food"
    )
    coffee = fields.Boolean('Coffee')
    coffee_cups = fields.Integer(
        'Cups per day',
        help="Number of cup of coffee a day"
    )
    soft_drinks = fields.Boolean(
        'Soft drinks (sugar)',
        help="Check if the patient consumes soft drinks with sugar"
    )
    diet = fields.Boolean(
        'Currently on a diet',
        help="Check if the patient is currently on a diet"
    )
    diet_info = fields.Char(
        'Diet info',
        help="Short description on the diet"
    )
    smoking = fields.Boolean('Smokes')
    smoking_number = fields.Integer('Cigarretes a day')
    ex_smoker = fields.Boolean('Ex-smoker')
    second_hand_smoker = fields.Boolean(
        'Passive smoker',
        help="Check it the patient is a passive / second-hand smoker"
    )
    age_start_smoking = fields.Integer('Age started to smoke')
    age_quit_smoking = fields.Integer(
        'Age of quitting',
        help="Age of quitting smoking"
    )
    alcohol = fields.Boolean('Drinks Alcohol')
    age_start_drinking = fields.Integer(
        'Age started to drink ',
        help="Date to start drinking"
    )
    age_quit_drinking = fields.Integer(
        'Age quit drinking ',
        help="Date to stop drinking"
    )
    ex_alcoholic = fields.Boolean('Ex alcoholic')
    alcohol_beer_number = fields.Integer('Beer / day')
    alcohol_wine_number = fields.Integer('Wine / day')
    alcohol_liquor_number = fields.Integer('Liquor / day')
    drug_usage = fields.Boolean('Drug Habits')
    ex_drug_addict = fields.Boolean('Ex drug addict')
    drug_iv = fields.Boolean(
        'IV drug user',
        help="Check this option if the patient injects drugs"
    )
    age_start_drugs = fields.Integer(
        'Age started drugs ',
        help="Age of start drugs"
    )
    age_quit_drugs = fields.Integer(
        'Age quit drugs ',
        help="Date of quitting drugs"
    )
    recreational_drugs = fields.One2many(
        'medical.patient_recreational_drugs',
        'patient',
        'Drugs'
    )
    traffic_laws = fields.Boolean(
        'Obeys Traffic Laws',
        help="Check if the patient is a safe driver"
    )
    car_revision = fields.Boolean(
        'Car Revision',
        help="Maintain the vehicle. Do periodical checks - tires,breaks ..."
    )
    car_seat_belt = fields.Boolean(
        'Seat belt',
        help="Safety measures when driving : safety belt"
    )
    car_child_safety = fields.Boolean(
        'Car Child Safety',
        help="Safety measures when driving : child seats, "
             "proper seat belting, not seating on the front seat, ...."
    )
    home_safety = fields.Boolean(
        'Home safety',
        help="Keep safety measures for kids in the kitchen, "
             "correct storage of chemicals, ..."
    )
    motorcycle_rider = fields.Boolean(
        'Motorcycle Rider',
        help="The patient rides motorcycles"
    )
    helmet = fields.Boolean(
        'Uses helmet',
        help="The patient uses the proper motorcycle helmet"
    )
    lifestyle_info = fields.Text(string='Lifestyle extra information')
    sexual_preferences = fields.Selection(
        [
            ('h', 'Heterosexual'),
            ('g', 'Homosexual'),
            ('b', 'Bisexual'),
            ('t', 'Transexual'),
        ],
        'Sexual Preferences',
        sort=False
    )
    sexual_practices = fields.Selection(
        [
            ('s', 'Safe / Protected sex'),
            ('r', 'Risky / Unprotected sex'),
        ],
        'Sexual Practices',
        sort=False
    )
    sexual_partners = fields.Selection(
        [
            ('m', 'Monogamous'),
            ('t', 'Polygamous'),
        ],
        'Sexual Partners',
        sort=False
    )
    sexual_partners_number = fields.Integer('Number of sexual partners')
    first_sexual_encounter = fields.Integer('Age of first sexual encounter')
    anticonceptive = fields.Selection(
        [
            ('0', 'None'),
            ('1', 'Pill / Minipill'),
            ('2', 'Male condom'),
            ('3', 'Vasectomy'),
            ('4', 'Female sterilisation'),
            ('5', 'Intra-uterine device'),
            ('6', 'Withdrawal method'),
            ('7', 'Fertility cycle awareness'),
            ('8', 'Contraceptive injection'),
            ('9', 'Skin Patch'),
            ('10', 'Female condom'),
        ],
        'Contraceptive Method',
        sort=False
    )
    sex_oral = fields.Selection(
        [
            ('0', 'None'),
            ('1', 'Active'),
            ('2', 'Passive'),
            ('3', 'Both'),
        ],
        'Oral Sex',
        sort=False
    )
    sex_anal = fields.Selection(
        [
            ('0', 'None'),
            ('1', 'Active'),
            ('2', 'Passive'),
            ('3', 'Both'),
        ],
        'Anal Sex',
        sort=False
    )
    prostitute = fields.Boolean(
        string='Prostitute',
        help="Check if the patient (he or she) is a prostitute"
    )
    sex_with_prostitutes = fields.Boolean(
        string='Sex with prostitutes',
        help="Check if the patient (he or she) has sex with prostitutes"
    )
    sexuality_info = fields.Text(string='Sexuality extra information')
    cage = fields.One2many(
        'medical.patient.cage',
        'name',
        'CAGE'
    )
