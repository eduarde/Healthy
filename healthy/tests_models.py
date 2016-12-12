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





class MarkerPredefinedTestCase(TestCase):
	def setUp(self):
		self.marker_normal = Marker.objects.create(name="Leucocite", abbr="L", category="Hematologie", um="mm3")
		self.marker_pred_normal = MarkerPredefined.objects.create(marker_ref=self.marker_normal, threshold_min="10",threshold_max="20")

		lab_date = "2016-03-03"
		user_dob = "2007-05-09"
		self.user = User.objects.create(username='user_test')
		self.userprofile = UserProfile.objects.create(user=self.user, gender="M", dob=user_dob, blood_type="Group A")
		Lab.objects.create(user=self.user, date=lab_date, ref_number="1234", doctor="Doctor Test", collection_point="Hospital Test", patient_code="1234")
		self.marker_child = Marker.objects.create(name="Leucocite", abbr="L", category="Hematologie", um="mm3",variant_type="Gender")
		self.marker_pred_child = MarkerPredefined.objects.create(marker_ref=self.marker_child, threshold_min="5",threshold_max="10",variant_gender="Child")

		self.marker_male = Marker.objects.create(name="Leucocite", abbr="L", category="Hematologie", um="mm3",variant_type="Gender")
		self.marker_pred_male = MarkerPredefined.objects.create(marker_ref=self.marker_male, threshold_min="20",threshold_max="30", variant_gender="Male")

		self.marker_age = Marker.objects.create(name="Leucocite", abbr="L", category="Hematologie", um="mm3",variant_type="Age")
		self.marker_pred_age = MarkerPredefined.objects.create(marker_ref=self.marker_age, threshold_min="15",threshold_max="30", variant_age="30")

	def test_marker_values_normal(self):
		self.assertEqual(self.marker_pred_normal.variant_gender,'N/A')
		self.assertEqual(self.marker_pred_normal.variant_age,0)
		self.assertTrue(int(self.marker_pred_normal.threshold_min) > 9 )
		self.assertTrue(int(self.marker_pred_normal.threshold_max) < 21 )

	def test_marker_values_child(self):
		gender = "N/A"
		lab = Lab.objects.get(ref_number="1234")
		if int(lab.user_age_lab) < 12:
			gender = 'Child'
		self.assertEqual(self.marker_pred_child.variant_gender,gender)
		self.assertEqual(int(self.marker_pred_child.variant_age),0)
		self.assertTrue(int(self.marker_pred_child.threshold_min) > 4 )
		self.assertTrue(int(self.marker_pred_child.threshold_max) < 11 )	

	def test_marker_values_male(self):
		self.assertEqual(self.marker_pred_male.variant_gender,'Male')
		self.assertEqual(self.marker_pred_male.variant_age,0)
		self.assertTrue(int(self.marker_pred_male.threshold_min) > 19 )
		self.assertTrue(int(self.marker_pred_male.threshold_max) < 31 )

	def test_marker_values_age(self):
		self.assertEqual(self.marker_pred_age.variant_gender,'N/A')
		self.assertEqual(int(self.marker_pred_age.variant_age),30)
		self.assertTrue(int(self.marker_pred_age.threshold_min) > 14 )
		self.assertTrue(int(self.marker_pred_age.threshold_max) < 31 )

