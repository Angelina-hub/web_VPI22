from django.contrib import admin
from django.urls import path
from EstablishmentsWeb import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'EstablishmentsWeb'
default_auto_field = 'django.db.models.BigAutoField'


def ready(self):
    import EstablishmentsWeb.templatetags.my_filters  # Import your filter module

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.Establishments, name='Home'),
    path('establishments/', views.EstablishmentsJson, name='EstablishmentsJson'),
    path('establishments/<int:id_establishment>', views.EstablishmentsInformation, name='EstablishmentsInformation'),
    path('feedback/<int:id_establishment>', views.feedback, name='EstablishmentReview'),
    path('feedbacks/<int:id_establishment>', views.feedbacksestablishment, name='ReviewForEstablishment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)