from django.urls import path
from .views import (
    Home,
    AcademyCreateView,
    AcademyListView,
    AcademyUpdateView,
    AcademyDeleteView,
    ClassCreateView,
    ClassListView,
    ClassUpdateView,
    ClassDeleteView,
    StudentCreateView,
    StudentListView,
    StudentUpdateView,
    StudentDeleteView,
    ChargesCreateView,
    ChargesListView,
    ChargesUpdateView,
    ChargesDeleteView,
    AttendanceCreateView,
    AttendanceListView,
    AttendanceUpdateView,
    AttendanceDeleteView,
    FeeSubmissionCreateView,
    FeeSubmissionListView,
    FeeSubmissionUpdateView,
    FeeSubmissionDeleteView,
    RewardCreateView,
    RewardListView,
    RewardUpdateView,
    RewardDeleteView,
    ClassAttendanceListView,
    ClassAttendanceDetailView,
    students_attendance_statistics,
    CreateTestView,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    # Academy URLs
    path("academy/create/", AcademyCreateView.as_view(), name="academy_create"),
    path("academy/", AcademyListView.as_view(), name="academy_list"),
    path(
        "academy/<int:pk>/update/", AcademyUpdateView.as_view(), name="academy_update"
    ),
    path(
        "academy/<int:pk>/delete/", AcademyDeleteView.as_view(), name="academy_delete"
    ),
    # Class URLs
    path("class/create/", ClassCreateView.as_view(), name="class_create"),
    path("class/", ClassListView.as_view(), name="class_list"),
    path("class/<int:pk>/update/", ClassUpdateView.as_view(), name="class_update"),
    path("class/<int:pk>/delete/", ClassDeleteView.as_view(), name="class_delete"),
    # Student URLs
    path("student/create/", StudentCreateView.as_view(), name="student_create"),
    path("student/", StudentListView.as_view(), name="student_list"),
    path(
        "student/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"
    ),
    path(
        "student/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"
    ),
    # Charges URLs
    path("charges/create/", ChargesCreateView.as_view(), name="charges_create"),
    path("charges/", ChargesListView.as_view(), name="charges_list"),
    path(
        "charges/<int:pk>/update/", ChargesUpdateView.as_view(), name="charges_update"
    ),
    path(
        "charges/<int:pk>/delete/", ChargesDeleteView.as_view(), name="charges_delete"
    ),
    # Attendance URLs
    path(
        "attendance/create/", AttendanceCreateView.as_view(), name="attendance_create"
    ),
    path("attendance/", AttendanceListView.as_view(), name="attendance_list"),
    path(
        "attendance/<int:pk>/update/",
        AttendanceUpdateView.as_view(),
        name="attendance_update",
    ),
    path(
        "attendance/<int:pk>/delete/",
        AttendanceDeleteView.as_view(),
        name="attendance_delete",
    ),
    # FeeSubmission URLs
    path(
        "fee-submission/create/",
        FeeSubmissionCreateView.as_view(),
        name="fee_submission_create",
    ),
    path(
        "fee-submission/", FeeSubmissionListView.as_view(), name="fee_submission_list"
    ),
    path(
        "fee-submission/<int:pk>/update/",
        FeeSubmissionUpdateView.as_view(),
        name="fee_submission_update",
    ),
    path(
        "fee-submission/<int:pk>/delete/",
        FeeSubmissionDeleteView.as_view(),
        name="fee_submission_delete",
    ),
    # Reward URLs
    path("reward/create/", RewardCreateView.as_view(), name="reward_create"),
    path("reward/", RewardListView.as_view(), name="reward_list"),
    path("reward/<int:pk>/update/", RewardUpdateView.as_view(), name="reward_update"),
    path("reward/<int:pk>/delete/", RewardDeleteView.as_view(), name="reward_delete"),
    path(
        "class-attendance/",
        ClassAttendanceListView.as_view(),
        name="class_attendance_list",
    ),
    path(
        "class-attendance/",
        ClassAttendanceListView.as_view(),
        name="class_attendance_list",
    ),
    path(
        "class-attendance/<int:class_id>/",
        ClassAttendanceDetailView.as_view(),
        name="class_attendance_detail",
    ),
    path(
        "attendance-statistics/",
        students_attendance_statistics,
        name="attendance_statistics",
    ),
    path("test/create/", CreateTestView.as_view(), name="create_test"),
]
