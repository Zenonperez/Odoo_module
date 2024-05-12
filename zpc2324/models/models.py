# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


class member(models.Model):
     _name = 'zpc2324.member'
     _description = 'Member of a team in a project organization'

     name = fields.Char('Name', required=True)
     last_name = fields.Char('Last Name', required=True)
     age = fields.Integer('Age', compute='_compute_age')
     birthdate = fields.Date('Birthdate')
     email = fields.Char('Email', required=True)
     phone = fields.Char('Phone', required=True)
     id_number = fields.Char('ID', size=9, required=True)
     salary = fields.Float('Salary')
     working = fields.Boolean('Working', default=True, help="Is this member working?")
     team_id = fields.Many2one('zpc2324.team')
     task_id = fields.Many2many('zpc2324.task', string="Tasks")

     _sql_constraints = [('id_number_uniq', 'unique (id_number)', "The member ID alredy exists !")]

     @api.depends('birthdate')
     def _compute_age(self):
         today = date.today()
         for record in self:
             if record.birthdate:
                 record.age = relativedelta(today, record.birthdate).years
             else:
                 record.age = 0


     def print_report(self):
            return self.env.ref('zpc2324.template_zpc2324_member').report_action(self)

class team(models.Model):
     _name = 'zpc2324.team'
     _description = 'The team in a project organization'

     name = fields.Char('Department', required=True)
     leader_id = fields.Many2one('hr.employee', string="Leader")
     member_ids = fields.One2many('zpc2324.member', 'team_id', string="Members")
     member_number = fields.Integer('Member', compute='_compute_member_number')
     description = fields.Char('Description')

     @api.depends('member_ids')
     def _compute_member_number(self):
         for count in self:
             count.member_number = len(count.member_ids)


class task(models.Model):
      _name = 'zpc2324.task'
      _description = 'The tasks required to do a project'

      name = fields.Char('Task', size=32, required=True)
      description = fields.Text('Description')
      taskStatus = fields.Selection([('todo', 'ToDo'), ('done', 'Done'), ('in_progres', 'In Progress'), ('canceled', 'Canceled')], default='todo', string='Task Status')
      startDate = fields.Datetime('Datetime', default=fields.Datetime.now)
      taskMilestone = fields.Datetime('Milestone', required=True)
      estimatedDuration = fields.Float('Aproximated duration')
      members = fields.Many2many('zpc2324.member', string='Members')

