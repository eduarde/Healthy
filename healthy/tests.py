from django.test import TestCase
from .models import  Lab, UserProfile, LabResult, Marker, MarkerPredefined

from django.contrib.auth.models import User

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.db import IntegrityError





class LabTestCase(TestCase):

	def setUp(self):
		lab_date = "2015-03-03"
		user_dob = "1991-12-09"
		self.user = User.objects.create(username='user_test')
		self.userprofile = UserProfile.objects.create(user=self.user, gender="M", dob=user_dob, blood_type="Group A")
		Lab.objects.create(user=self.user, date=lab_date, ref_number="1234", doctor="Doctor Test", collection_point="Hospital Test", patient_code="1234")
		self.expected_age_lab = self.years_between(lab_date,user_dob)

	@staticmethod	
	def years_between(d1, d2):
		d1 = datetime.strptime(d1, "%Y-%m-%d")
		d2 = datetime.strptime(d2, "%Y-%m-%d") 
		return relativedelta(d1, d2).years

	def test_lab_user_age_lab(self):
		
		lab = Lab.objects.get(ref_number="1234")
		self.assertEqual(lab.user_age_lab, self.expected_age_lab)

	def test_lab_unique_ref_number(self):
		with self.assertRaises(IntegrityError):
			Lab.objects.create(user=self.user, date="2015-03-03", ref_number="1234", doctor="Doctor Test", collection_point="Hospital Test", patient_code="1234")	





class LabResultTestCase(TestCase):
	def setUp(self):
		lab_date = "2015-03-03"
		self.user = User.objects.create(username='user_test')

		self.lab = 	Lab.objects.create(user=self.user, date=lab_date, ref_number="1234", doctor="Doctor Test", collection_point="Hospital Test", patient_code="1234")
		self.marker = Marker.objects.create(name="Leucocite", abbr="L", category="Hematologie", um="mm3")
		self.marker_pred = MarkerPredefined.objects.create(marker_ref=self.marker, threshold_min="10",threshold_max="20" )

		self.labresult_normal = LabResult.objects.create(lab_ref=self.lab, marker_ref=self.marker, predefined_ref=self.marker_pred, value="15")
		self.labresult_abnormal = LabResult.objects.create(lab_ref=self.lab, marker_ref=self.marker, predefined_ref=self.marker_pred, value="55")

		self.labresult_normal_limit_min = LabResult.objects.create(lab_ref=self.lab, marker_ref=self.marker, predefined_ref=self.marker_pred, value="10")
		self.labresult_normal_limit_max = LabResult.objects.create(lab_ref=self.lab, marker_ref=self.marker, predefined_ref=self.marker_pred, value="20")

	def test_labresult_check_normal_value(self):
		self.assertEqual(self.labresult_normal.is_abnormal(), False)

	def test_labresult_check_abnormal_value(self):
		self.assertEqual(self.labresult_abnormal.is_abnormal(), True)

	def test_labresult_check_limit_max_value(self):
		self.assertEqual(self.labresult_normal_limit_max.is_abnormal(), False)

	def test_labresult_check_limit_min_value(self):
		self.assertEqual(self.labresult_normal_limit_min.is_abnormal(), False)		