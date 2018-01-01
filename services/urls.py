from django.conf.urls import url
from . import views

app_name = 'services'
urlpatterns = [
    url(r'^$', views.services, name='services'),
    url(r'^reservation/', views.reservation, name='reservation'),
    url(r'^get_calendar/', views.generate_calendar, name='get_calendar'),
    url(r'^summary/', views.generate_summary, name = 'summary'),
    url(r'^worker_summary/', views.generate_worker_reservation_summary, name = 'worker_summary'),
    url(r'^save_reservation/', views.save_reservation, name = 'save_reservation'),
    url(r'^save_worker_reservation/', views.save_worker_reservation, name = 'save_reservation'),
    url(r'^client_reservations/', views.client_services, name = 'client_reservations'),
    url(r'^worker_reservation/(?P<id_client>\d+)/$', views.worker_reservation, name='worker_reservation'),
    url(r'^worker_services/', views.worker_services_table, name = 'worker_services'),
    url(r'^get_worker_calendar/', views.generate_worker_calendar, name = 'get_worker_calendar'),
    url(r'^get_all_future_reservations/', views.get_all_future_reservations, name = 'get_all_future_reservations'),
    url(r'^get_all_past_reservations/', views.get_all_past_reservations, name = 'get_all_past_reservations'),
    url(r'^service_resignation/', views.client_service_resignation, name = 'service_resignation'),
]
