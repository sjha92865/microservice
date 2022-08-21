from django.urls import path
# from . import views
# from .views import newproject

from core.views import MyView

urlpatterns = [
    path('post/', MyView.as_view()),
    path('post/<>', MyView.as_view()),

    # path('post/', MyView.as_view()),

]
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('about/', TemplateView.as_view(template_name="index.html")),
# ]
# urlpatterns = [
    
#     # path('h/',views.newproject,name='newproject'),
#     path('h/',newproject.as_view()),


   
# ]

















# from .views import CnocOpsView, CnocOpsViewDownload,Home
# #login_required(login_url='/login/')
# #login_required(login_url='/login/')
# urlpatterns = [
#     path('', (CnocOpsView.as_view()), name='cnocopsview'),
#     # path('download/', (CnocOpsViewDownload.as_view()), name='cnocops_download'),
#     # path('home/', (Home.as_view()), name='home'),
#     # path('<ticket_id>/',views.hello,name='hello'),
# ]