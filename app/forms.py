from django import forms
from .models import Resume

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
 ('Banglore', 'Banglore')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','About_yourself','education', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email','Work_experience','Specialization','linkdin_link', 'job_city', 'profile_image', 'my_file']
        labels = {'name':'Full Name','About_yourself': 'About yourself', 'education': 'Education','dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID', 'Work_experience':'Work experience','linkdin_link': 'Linkdin link','profile_image':'Profile Image', 'my_file':'Document'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'About_yourself': forms.TextInput(attrs={'class':'form-control'}),
            'education': forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'Work_experience':forms.TextInput(attrs={'class':'form-control'}),
            'Specialization':forms.Select(attrs={'class':'form-select'}),
            'linkdin_link':forms.TextInput(attrs={'class':'form-control'}),
            }