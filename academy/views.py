from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView
from django.urls import reverse_lazy
from .models import (
    Academy,
    Class,
    Student,
    Charges,
    Attendance,
    FeeSubmission,
    Reward,
    ClassAttendance,
    AttendanceRecord,
)
from .forms import AttendanceRecordForm
from django.utils.dateparse import parse_date
from datetime import date
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Student
from django.db.models import Count, Case, When, IntegerField, Sum


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class AcademyListView(ListView):
    model = Academy
    template_name = "academy_list.html"
    context_object_name = "academies"


class AcademyCreateView(CreateView):
    model = Academy
    fields = ["name", "address", "director", "contact_number", "email"]
    template_name = "academy_create.html"
    success_url = reverse_lazy("home")


class AcademyUpdateView(UpdateView):
    model = Academy
    fields = ["name", "address", "director", "contact_number", "email"]
    template_name = "academy_update.html"
    success_url = reverse_lazy("academy_list")


class AcademyDeleteView(DeleteView):
    model = Academy
    success_url = reverse_lazy("academy_list")


# ListView for Class model
class ClassListView(ListView):
    model = Class
    template_name = "class_list.html"
    context_object_name = "classes"


class ClassCreateView(CreateView):
    model = Class
    fields = ["name", "academy", "class_teacher"]
    template_name = "class_create.html"
    success_url = reverse_lazy("class_list")


class ClassUpdateView(UpdateView):
    model = Class
    fields = ["name", "academy", "class_teacher"]
    template_name = "class_update.html"
    success_url = reverse_lazy("class_list")


class ClassDeleteView(DeleteView):
    model = Class
    template_name = "class_confirm_delete.html"
    success_url = reverse_lazy("class_list")


# ListView for Student model
class StudentListView(ListView):
    template_name = "student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        # Retrieve all classes
        classes = Class.objects.all()

        # Create a dictionary to store students grouped by class
        students_by_class = {}

        # Iterate through each class and fetch related students
        for class_instance in classes:
            students = Student.objects.filter(class_enrolled=class_instance)
            students_by_class[class_instance] = students

        return students_by_class


class StudentCreateView(CreateView):
    model = Student
    fields = [
        "name",
        "address",
        "national_identity_number",
        "roll_number",
        "class_enrolled",
        "date_of_birth",
        "guardian_name",
        "guardian_contact_number",
        "guardian_email",
        "fee_amount",
    ]
    template_name = "student_create.html"
    success_url = reverse_lazy("student_list")


class StudentUpdateView(UpdateView):
    model = Student
    fields = [
        "name",
        "address",
        "national_identity_number",
        "roll_number",
        "class_enrolled",
        "date_of_birth",
        "guardian_name",
        "guardian_contact_number",
        "guardian_email",
        "fee_amount",
    ]
    template_name = "student_update.html"
    success_url = reverse_lazy("student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("student_list")


# ListView for Charges model
class ChargesListView(ListView):
    model = Charges
    template_name = "charges_list.html"
    context_object_name = "charges"


class ChargesCreateView(CreateView):
    model = Charges
    fields = ["student", "class_associated", "amount", "description", "date"]
    template_name = "charge_create.html"
    success_url = reverse_lazy("charges_list")


class ChargesUpdateView(UpdateView):
    model = Charges
    fields = ["student", "class_associated", "amount", "description", "date"]
    template_name = "charge_update.html"
    success_url = reverse_lazy("charges_list")


class ChargesDeleteView(DeleteView):
    model = Charges
    template_name = "charges_confirm_delete.html"
    success_url = reverse_lazy("charges_list")


# ListView for Attendance model
class AttendanceListView(ListView):
    model = Attendance
    template_name = "attendance_list.html"
    context_object_name = "attendance"


class AttendanceCreateView(CreateView):
    model = Attendance
    fields = ["student", "attendance_class", "date", "status", "remarks"]
    template_name = "attendance_create.html"
    success_url = reverse_lazy("attendance_list")


class AttendanceUpdateView(UpdateView):
    model = Attendance
    fields = ["student", "attendance_class", "date", "status", "remarks"]
    template_name = "attendance_update.html"
    success_url = reverse_lazy("attendance_list")


class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = "attendance_confirm_delete.html"
    success_url = reverse_lazy("attendance_list")


# ListView for FeeSubmission model
class FeeSubmissionListView(ListView):
    model = FeeSubmission
    template_name = "fee_submission_list.html"
    context_object_name = "fee_submissions"


class FeeSubmissionCreateView(CreateView):
    model = FeeSubmission
    fields = ["student", "fee_class", "amount", "date", "payment_method", "remarks"]
    template_name = "fee_submission_create.html"
    success_url = reverse_lazy("fee_submission_list")


class FeeSubmissionUpdateView(UpdateView):
    model = FeeSubmission
    fields = ["student", "fee_class", "amount", "date", "payment_method", "remarks"]
    template_name = "fee_submission_update.html"
    success_url = reverse_lazy("fee_submission_list")


class FeeSubmissionDeleteView(DeleteView):
    model = FeeSubmission
    template_name = "fee_submission_confirm_delete.html"
    success_url = reverse_lazy("fee_submission_list")


# ListView for Reward model
class RewardListView(ListView):
    model = Reward
    template_name = "reward_list.html"
    context_object_name = "rewards"


class RewardCreateView(CreateView):
    model = Reward
    fields = [
        "student",
        "reward_class",
        "title",
        "description",
        "date",
        "awarded_by",
        "amount",
    ]
    template_name = "reward_create.html"
    success_url = reverse_lazy("reward_list")


class RewardUpdateView(UpdateView):
    model = Reward
    fields = [
        "student",
        "reward_class",
        "title",
        "description",
        "date",
        "awarded_by",
        "amount",
    ]
    template_name = "reward_update.html"
    success_url = reverse_lazy("reward_list")


class RewardDeleteView(DeleteView):
    model = Reward
    template_name = "reward_confirm_delete.html"
    success_url = reverse_lazy("reward_list")


# List view for ClassAttendance with students list for attendance
class ClassAttendanceListView(ListView):
    model = Class
    template_name = "class_attendance_list.html"
    context_object_name = "classes"


class ClassAttendanceDetailView(FormView):
    template_name = "class_attendance_detail.html"
    form_class = AttendanceRecordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_instance = get_object_or_404(Class, id=self.kwargs["class_id"])
        students = Student.objects.filter(class_enrolled=class_instance)
        context["class"] = class_instance
        context["students"] = students
        context["date"] = date.today()  # Add the current date to the context
        return context

    def post(self, request, *args, **kwargs):
        class_instance = get_object_or_404(Class, id=self.kwargs["class_id"])
        students = Student.objects.filter(class_enrolled=class_instance)
        attendance_date = request.POST.get("date")  # Ensure date is passed from form
        attendance_date = parse_date(
            attendance_date
        )  # Parse the date to ensure correct format

        if not attendance_date:
            return self.form_invalid(self.get_form())  # Handle invalid date

        # Check if ClassAttendance instance already exists for the given date
        class_attendance, created = ClassAttendance.objects.get_or_create(
            attendance_class=class_instance, date=attendance_date
        )

        # If not created, delete existing attendance records for this date
        if not created:
            AttendanceRecord.objects.filter(class_attendance=class_attendance).delete()

        # Create or update attendance records
        for student in students:
            status = request.POST.get(f"status_{student.id}")
            remarks = request.POST.get(f"remarks_{student.id}", "")
            AttendanceRecord.objects.create(
                class_attendance=class_attendance,
                student=student,
                status=status,
                remarks=remarks,
            )

        return redirect("class_attendance_list")


def get_students_attendance_info():
    # Group students by their enrolled class and annotate statistics
    students_by_class = []
    classes = Class.objects.all()

    for class_instance in classes:
        students = Student.objects.filter(class_enrolled=class_instance).annotate(
            total_attendances=Count("attendancerecord", distinct=True),
            total_leaves=Count(
                Case(
                    When(attendancerecord__status="Absent", then=1),
                    output_field=IntegerField(),
                ),
                distinct=True,
            ),
            total_fee=Sum("charges__amount"),
            total_amount_paid=Sum("feesubmission__amount"),
        )
        students_by_class.append(
            {
                "class": class_instance,
                "students": students,
            }
        )

    return students_by_class


def students_attendance_statistics(request):
    students_by_class = get_students_attendance_info()
    context = {
        "students_by_class": students_by_class,
    }
    return render(request, "attendance_statistics.html", context)


from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings
from .models import Test
from .forms import TestForm  # Assuming you have a form for Test model


class CreateTestView(CreateView):
    model = Test
    form_class = TestForm
    template_name = "test_form.html"
    success_url = reverse_lazy("home")

    def send_email_on_test_creation(self, test_instance):
        subject = "New Test Entry Added"
        message = f"A new test entry was added for {test_instance.student_test.name}."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
            test_instance.student_test.guardian_email
        ]  # Change as per your model structure
        send_mail(subject, message, from_email, recipient_list)

    def form_valid(self, form):
        # Save the form and get the test instance
        test_instance = form.save()

        # Send email notification
        self.send_email_on_test_creation(test_instance)

        return super().form_valid(form)
