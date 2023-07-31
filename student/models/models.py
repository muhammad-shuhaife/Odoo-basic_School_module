# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.exceptions import UserError,ValidationError
import re

# class SaleOrderInherit(models.Model):
#     _inherit = 'sale.order'
#
#     address = fields.Char(string="Address")
#     grade = fields.Char(string="grade")

#
# class ProductInherit(models.Model):
#     _inherit = 'product.template'
#
#     quality = fields.Char(string="Quality")
#     grade = fields.Char(string="grade")


# class ProductLineInherit(models.Model):
#     _inherit = 'product.template.attribute.line'
#
#     count = fields.Char(string="Quality")
#     rate = fields.Char(string="grade")

class Student(models.Model):
    _name = 'student.student'
    _description = 'student.student'
    _rec_name = "first_name"

    student_sequence = fields.Char("Student Id" ,readonly=True)
    first_name = fields.Char(string="first name")
    last_name = fields.Char(string="second name")
    date_of_birth = fields.Date(string="date of birth")
    age = fields.Integer(compute='compute_age',store=True)
    phone = fields.Char(string="phone",default="91111111111")
    email = fields.Char(string="email")
    address = fields.Char(string="Address")
    grade = fields.Char(string="grade")
    student_id = fields.Many2one("student.class", string='Class')
    # schedule_student = fields.Datetime(string="schedule",related='student_ids.schedule')
    state = fields.Selection([('confirm', 'Confirm'),
                              ('reject', 'Reject')])
    # allocation_ids = fields.One2many('student.allocation', 'student_id', string='Borrowed Books')
    user_id = fields.Many2one('res.users',string="User")

    @api.model
    def create(self, vals):
        vals['student_sequence'] = self.env['ir.sequence'].next_by_code('student.student')
        return super(Student, self).create(vals)

    def email_function(self):
        st = self.search([])

        for rec in st:
            template_id = rec.env.ref('student.email_template_demo')
            email_values = {
                'email_to': rec.email,
            }
            template_id.send_mail(rec.id, force_send=True,email_values=email_values)

    @api.constrains('email')
    def _validate_email(self):
        for record in self:
            if record.email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', record.email):
                raise ValidationError("Invalid email address!")

    def confirm_student(self):
        self.state = 'confirm'

    def reject_student(self):
        self.state = 'reject'

    def url_act_fun(self):
        return{
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'https://www.python.org/',

        }

    def email_crone(self):
        print("wonderful==============================")

    # def Fcreate(self, values):
    #     student = super(Student, self).create(values)
    #     user = student.user_id
    #     if user:
    #         student_gp = self.env.ref('student.student_group')
    #         if student_gp:
    #             user.write({'groups_id': [(4, student_gp.id)]})
    #     return student
#===================================================================================================================

# @api.model
# def default_get(self, fields):
#     defaults = super(Student,self).default_get(fields)
#     print("==========================defaults==============",defaults)
#     print("==========================fields==============",fields)
#     defaults['phone'] = '1234567890'
#     return defaults

#===================================================================================================================

    @api.depends('date_of_birth')
    def compute_age(self):
        for record in self:
            delta = relativedelta(date.today(), record.date_of_birth)
            record.age = delta.years


#===================================================================================================================

    # @api.model
    # def create(self, vals):
    #     vals['phone'] = '987654321'
    #     # vals.update({'phone':'987654321'})
    #     res = super(Student,self).create(vals)
    #     print("===================create======================",res)
    #     return res
#it returns the data of specified field 


#===================================================================================================================


    # def write(self, vals):
    #
    #     print('IIIIIIIIIIIIIIIIIIIIIIN')
    #     vals['email'] = 'mail'
    #     res = super(Student,self).write(vals)
    #     #1
    #     # student_ids = self.env['student.student'].search([('first_name', '=', 'sree'),('first_name', '=', 'Sudarsanan')])
    #     #2
    #     student_ids = self.search([('first_name', '=', 'azmar')])
    #     browse_id = self.env['student.student'].browse([3])
    #     new_records = self.env['student.student'].create([
    #         {'first_name': 'anandhu', 'last_name': 'mr.nair'},
    #         {'first_name': 'azmar', 'last_name': 'rahman'},
    #         {'first_name': 'razeen', 'last_name': 'abdurahman'},])
    #     # record = self.env['my.model'].browse(record_id)
    #     # student_ids.unlink()
    #     read=student_ids.read(['first_name','last_name'])
    #     print("===================READ======================",read)
    #
    #     print("===================newrecord======================",new_records)
    #     print("==================browse=================",browse_id)
    #     print("==================browse.name=================",browse_id.first_name)
    #
    #     print("==================write=================",res)
    #     print("==================search1=================",student_ids)
    #     print("==================search2=================",student_ids)
    #     return res
# it returns true or false


#===================================================================================================================


    # def unlink(self):
    #     for rec in self:
    #         if rec.first_name == 'anandhu':
    #             raise UserError('you cannnot remove this')
    #         print('==========call unlink===========')
    #         res= super(Student,self).unlink()
    #         print('unlink type==============',res)
    #     return res

    # @api.onchange('patient_id')
    # def onchange_patient_id(self):
    #     if self.patient_id:
    #         if self.patient_id.gender:
    #             self.gender = self.patient_id.gender
    #         if self.patient_id.note:
    #             self.note = self.patient_id.note
    #     else:
    #         self.gender = ''
    #         self.note = ''
    # @api.constrains('name')
    # def check_name(self):
    #     for rec in self:
    #         students = self.env['school.student'].search([('name','=',rec.name),('id','=',rec.id)])
    #         if students:
    #             raise ValidationError(_("Name %s Already Exists" % rec.name))
    # @api.constrains('age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.age == 0:
    #             raise ValidationError(_("Age Cannot Be Zero.."))
    # def unlink(self):
    #     for rec in self:
    #         if rec.name == 'wrwrwrwrwrw':
    #             raise UserError('You cannot delete Class 11 Records')
    #     print("===Call Unlink-------->")
    #     res = super(Student, self).unlink()
    #     print("Unlink Return Type==================")
    #     return res
    # def write(self, vals):
    #     print("write method is worked............",vals)
    #     return super(Student,self).write(vals)
    # @api.model
    # def create(self, vals):
    #     print("Create Call=----------------", vals)
    #     vals['contact_info'] = '********create method is called**********'
    #     res = super(Student,self).create(vals)
    #     print("===res====", res)
    #     return res
    # @api.model
    # def default_get(self, fields):
    #     vals = super(Student, self).default_get(fields)
    #     print("===fields==", fields)
    #     print("========vals", vals)
    #     vals['contact_info'] = 'Default  Contact'
    #     vals['name'] = 'This is defaul_get method'
    #     return vals
    # @api.model
    # def show_id(self):
    #     active_id = self.env.context.get('active_id')
    #     if active_id:
    #         return self.env['student.classes'].browse(active_id)