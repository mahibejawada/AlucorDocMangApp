from docoperations import views
from django.urls import path

urlpatterns=[
    path("SaveDocs/", views.SaveDocs.as_view()),
    path("UserDocsGet/", views.UserDocsGet.as_view()),
    path("UserDocsUpdate/", views.UserDocsGet.as_view()),
    path("UserDocsDelete/", views.UserDocsGet.as_view()),

]