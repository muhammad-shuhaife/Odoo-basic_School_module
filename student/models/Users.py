from odoo import models, fields, api


class Users(models.Model):
    _inherit = 'res.users'
    _description = 'IsAdmin'

    manager = fields.Boolean(string='Is Manager')
    # student = fields.Boolean(string='Is student')
    admin = fields.Boolean(string='Is admin')
    # teacher = fields.Boolean(string='Is teacher')

    # def write(self, vals):
    #     fields_to_reset = ['manager', 'student', 'admin', 'teacher']
    #
    #     for field_name in fields_to_reset:
    #         if field_name in vals:
    #             field_value = vals[field_name]
    #             if field_value:
    #                 vals.update({name: False for name in fields_to_reset if name != field_name})
    #                 break
    #
    #     return super(Users, self).write(vals)

    @api.model
    def create(self, values):
        user = super(Users, self).create(values)
        groups_to_add = []

        if values.get('manager'):
            manager_group = self.env.ref('student.manager_group')
            if manager_group:
                groups_to_add.append((4, manager_group.id))

        if values.get('admin'):
            admin_group = self.env.ref('student.admin_group')
            if admin_group:
                groups_to_add.append((4, admin_group.id))

        if groups_to_add:
            user.write({'groups_id': groups_to_add})

        return user

    # def write(self, vals):
    #     groups_to_assign = []
    #     groups_to_remove = []
    #     if 'manager' in vals:
    #         if vals['manager']:
    #             groups_to_assign.append(self.env.ref('student.manager_group'))
    #         else:
    #             groups_to_remove.append(self.env.ref('student.manager_group'))
    #     if 'student' in vals:
    #         if vals['student']:
    #             groups_to_assign.append(self.env.ref('student.student_group'))
    #         else:
    #             groups_to_remove.append(self.env.ref('student.student_group'))
    #     if 'admin' in vals:
    #         if vals['admin']:
    #             groups_to_assign.append(self.env.ref('student.admin_group'))
    #         else:
    #             groups_to_remove.append(self.env.ref('student.admin_group'))
    #     if 'teacher' in vals:
    #         if vals['teacher']:
    #             groups_to_assign.append(self.env.ref('student.teacher_group'))
    #         else:
    #             groups_to_remove.append(self.env.ref('student.teacher_group'))
    #     if groups_to_assign:
    #         self.write({'groups_id': [(4, group.id) for group in groups_to_assign]})
    #     if groups_to_remove:
    #         self.write({'groups_id': [(3, group.id) for group in groups_to_remove]})
    #     return super(Users, self).write(vals)
