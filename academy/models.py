from django.db import models


class Academy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    director = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(default="ahsantariq0724@gmail.com")

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)
    class_teacher = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    national_identity_number = models.CharField(
        max_length=13, null=True, blank=True
    )  # Renamed from 'cnic'
    roll_number = models.CharField(max_length=20, null=True, blank=True)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_contact_number = models.CharField(
        max_length=20, null=True, blank=True
    )  # Renamed from 'guardian_contact'
    guardian_email = models.EmailField(null=True, blank=True)
    fee_amount = models.FloatField(null=True, blank=True)  # Renamed from 'Fee'

    def __str__(self):
        return self.name + self.class_enrolled.name


class Test(models.Model):
    date = models.DateField()
    test_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_test = models.ForeignKey(Student, on_delete=models.CASCADE)
    obtained_marks = models.FloatField()
    total_marks = models.FloatField()
    day_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_test.name} - {self.day_name}, {self.date.strftime('%B %d, %Y')}"


class Charges(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="charges"
    )
    class_associated = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name="charges"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.date.strftime('%B %d, %Y')}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("Present", "Present"), ("Absent", "Absent"), ("Leave", "Leave")],
        default="Present",  # Added default value
    )
    remarks = models.TextField(blank=True)


class FeeSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ("Cash", "Cash"),
            ("Bank Transfer", "Bank Transfer"),
            ("Online Payment", "Online Payment"),
        ],
    )
    remarks = models.TextField(blank=True)


class Reward(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reward_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    awarded_by = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class ClassAttendance(models.Model):
    attendance_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.attendance_class.name} - {self.date.strftime('%B %d, %Y')}"


class AttendanceRecord(models.Model):
    class_attendance = models.ForeignKey(
        ClassAttendance, on_delete=models.CASCADE, related_name="attendance_records"
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[("Present", "Present"), ("Absent", "Absent"), ("Leave", "Leave")],
        default="Present",
    )
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.status}"


# Update model list
model = [
    Academy,
    Class,
    Student,
    Test,
    Charges,
    Attendance,
    FeeSubmission,
    Reward,
    ClassAttendance,
    AttendanceRecord,
]
