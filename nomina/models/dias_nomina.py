# -*- coding: utf-8 -*-

from odoo import fields, models, api

class diasNomina(models.Model):
	_inherit = 'hr.payslip'

	@api.multi
	def button_import_attendance(self):
		for payslip in self:
			payslip._worked_days_line()

	@api.multi
	def _worked_days_line(self):
		wd_obj = self.env["hr.payslip.worked_days"]
		date_from = self.date_from
		date_to = self.date_to
		worked_lines = {
						"name": "Dias Trabajados",
						"code": "WORK100",
						"number_of_days": 7,
						"number_of_hours": 0.0,
						"contract_id": self.contract_id.id,
						"payslip_id": self.id,
					}
		print 'worked_lines->>>> '+str(worked_lines)
		#wd_obj.create({'worked_days_line_ids': [(0, 0, x) for x in worked_lines]})
		wd_obj.create(worked_lines)
	