
from django.urls import path
from .views import ReporterViews, IssueView

urlpatterns=[
    path('reporters/',ReporterViews.as_view()),
    path('issues/',IssueView.as_view()),
    # path('reporters/<int:id>/',ReporterViews.as_view()),
    # path('issues/<int:id>/',IssueView.as_view()),
]   