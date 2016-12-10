from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date, timedelta






class UserProfile(models.Model):
	F = 'F'
	M = 'M'

	GENDER_CHOICES = (
		(F, 'F'),
		(M, 'M'),
	)

	N  = 'N'
	A  = 'Group A'
	B  = 'Group B'
	AB = 'Group AB'
	O  = 'Group 0'	

	BLOOD_TYPES = (
		(A, 'Group A'),
		(B, 'Group B'),
		(AB, 'Group AB'),
		(O, 'Group 0'),
		(N, 'N'),
	)

	user = models.ForeignKey('auth.User', unique=True)
	gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default=F)
	dob = models.DateField('Date of birth',null=True)
	blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES, default=N)

	def __str__(self):
		return 'UserProfile ' + self.user.username





class Lab(models.Model):
	user = models.ForeignKey('auth.User', verbose_name='User', null=True)
	date = models.DateField('Date',blank=False, null=True)
	ref_number = models.IntegerField('Reference Number', blank=False,null=False,unique=True)
	doctor = models.CharField('Doctor', max_length=300, blank=True, null=True)
	collection_point = models.CharField('Collection point', max_length=500, blank=True, null=True)
	patient_code = models.IntegerField('Patient Code', blank=False,null=True)

	def check_abnormal_lab(self):
		labResults = LabResult.objects.filter(lab_ref__pk=self.pk)
		for labResult in labResults:
			if labResult.is_abnormal() == True:
				return True
		return False

	def get_user_age_lab(self):
		born = UserProfile.objects.filter(user=self.user)[:1].get().dob
		today = self.date
		return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

	user_age_lab = property(get_user_age_lab)
	abnormal_lab = property(check_abnormal_lab)

	

	def __str__(self):
		return 'Lab ' + str(self.ref_number)





class Marker(models.Model):

	Leucocite = 'Leucocite(WBC)'
	Hematii = 'Hematii(RBC)'
	Hemoglobina = 'Hemoglobina(HGB)'
	VEM = 'VEM(volum eritocitar mediu)'
	HEM = 'HEM(hemoglobina eritocitara medie)'
	CHEM = 'CHEM(conc HB eritocitara medie)'
	RDW = 'RDW'
	Trombocite = 'Trombocite(PLT)'
	MPW = 'MPW'
	PDW = 'PDW'
	Neutro = 'Neutro'
	Lym = 'Lym'
	Monocite = 'Monocite'
	Eozinofile = 'Eozinofile'
	Bazofile = 'Bazofile'
	Creatinina = 'Creatinina serica'
	Magneziu = 'Magneziu seric'
	Sideremie = 'Sideremie'
	Glicemie = 'Glicemie'
	TGP = 'TGP'
	TSH = 'TSH'
	FT4 = 'FT4'

	NAME_CHOICES = (
		(Leucocite,'Leucocite(WBC)'),
		(Hematii,'Hematii(RBC)'),
		(Hemoglobina,'Hemoglobina(HGB)'),
		(VEM,'VEM(volum eritocitar mediu'),
		(HEM,'HEM(hemoglobina eritocitara medie)'),
		(CHEM,'CHEM(conc HB eritocitara medie)'),
		(RDW, 'RDW'),
		(Trombocite,'Trombocite'),
		(MPW, 'MPW'),
		(PDW,'PDW'),
		(Neutro,'Neutro'),
		(Lym,'Lym'),
		(Monocite, 'Monocite'),
		(Eozinofile, 'Eozinofile'),
		(Bazofile, 'Bazofile'),
		(Creatinina,'Creatinina serica'),
		(Magneziu, 'Magneziu seric'),
		(Sideremie, 'Sideremie'),
		(Glicemie, 'Glicemie'),
		(TGP, 'TGP'),
		(TSH, 'TSH'),
		(FT4, 'FT4'),
	)

	Hematologie = 'Hematologie'
	Biochimie = 'Biochimie'
	Dozari = 'Dozari hormonale, Imunologie si markeri tumorali (Chemiluminiscenta)'

	CATEGORY_CHOICES = (
		(Hematologie, 'Hematologie'),
		(Biochimie, 'Biochimie'),
		(Dozari, 'Dozari hormonale, Imunologie si markeri tumorali (Chemiluminiscenta)'),

	)

	mm3 = '10^3/mm3'
	mm6 = '10^6/mm3'
	gdl = 'g/dl'
	percentage = '%'
	fL = 'fL'
	mgdl = 'mg/dl'
	UL = 'U\L'
	microUI = 'μUI\ml'
	ng = 'ng/dl'

	UM_CHOICES = (
		(mm3, '10^3/mm3'),
		(mm6, '10^6/mm3'),
		(gdl, 'g/dl'),
		(percentage, '%'),
		(fL, 'fL'),
		(mgdl, 'mg/dl'),
		(UL,'U\L'),
		(microUI, 'μUI\ml'),
		(ng, 'ng/dl'),
	)

	GENDER = 'Gender'
	AGE = 'Age'
	NONE = 'None'

	VARIANT_TYPE = (

		(GENDER, 'Gender'),
		(AGE,'Age'),
		(NONE, 'None'),

	)
	
	name = models.CharField('Name', max_length=100, blank=False, null=False, choices=NAME_CHOICES, default=Leucocite)
	abbr = models.CharField('Abbreviation', max_length=10, blank=True, null=True)
	category = models.CharField('Category',max_length=100, blank=False, null=False, choices=CATEGORY_CHOICES, default=Hematologie)
	um = models.CharField('Unit', max_length=10, blank=False, null=False, choices=UM_CHOICES,default=mm3)
	variant_type = models.CharField('Type', max_length=10, choices=VARIANT_TYPE, default=NONE)

	def __str__(self):
		return self.name





class MarkerPredefined(models.Model):
	FEMALE = 'Female'
	MALE = 'Male'
	CHILD = 'Child'
	NA = 'N/A'

	GENDER_CHOICES = (
		(FEMALE, 'Female'),
		(MALE, 'Male'),
		(CHILD, 'Child'),
		(NA, 'N/A'),
	)


	marker_ref = models.ForeignKey(Marker, related_name="Marker_MarkerPredefined_ref")
	variant_gender =  models.CharField('Gender', max_length=10, choices=GENDER_CHOICES, default=NA)
	variant_age = models.IntegerField('Age', blank=False,null=False,default=0)

	threshold_min = models.DecimalField('Min Value', default=0, max_digits=10, decimal_places=3, null=True)
	threshold_max = models.DecimalField('Max Value', default=0, max_digits=10, decimal_places=3, null=True)

	def __str__(self):
		return self.marker_ref.name + ' - ' + self.variant_gender + ' - ' +  variant_age





class LabResult(models.Model):
	
	lab_ref = models.ForeignKey(Lab, related_name="Lab_ref")
	marker_ref = models.ForeignKey(Marker, related_name="Marker_LabResults_ref", verbose_name="Marker")
	predefined_ref = models.ForeignKey(MarkerPredefined ,related_name="MarkerPredefined_LabResults_ref")
	value = models.DecimalField('Value', default=0, max_digits=10, decimal_places=3, null=True)

	def is_abnormal(self):
		if self.value < self.predefined_ref.threshold_min:
			return True

		if self.value > self.predefined_ref.threshold_max:
			return True

		return False 

	def __str__(self):
		return 'LabResult ' + str(self.lab_ref)





class LabNote(models.Model):
	lab_ref = models.ForeignKey(Lab, related_name="Lab_LabNote_ref")
	comment = models.TextField('Comment')
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return "Note " + str(self.pk) + " " + str(self.lab_ref.ref_number)





class Dictionary(models.Model):
	marker_ref = models.ForeignKey(Marker,related_name="Marker_Dictionary_ref")
	text = models.TextField("Text")

	def __str__(self):
		return self.marker_ref.name