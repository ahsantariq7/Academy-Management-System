from django import forms
from .models import ClassAttendance, AttendanceRecord, FeeSubmission, Test


class ClassAttendanceForm(forms.ModelForm):
    class Meta:
        model = ClassAttendance
        fields = ["attendance_class", "date"]


class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ["status", "remarks"]


class FeeSubmissionForm(forms.ModelForm):
    class Meta:
        model = FeeSubmission
        fields = ["student", "fee_class", "amount", "date", "payment_method", "remarks"]


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"
