from django.urls import path
from ViewData import views
urlpatterns = [

    path('',views.index_view),
    path('View1/',views.street_view,name='view1'),
    path('View3/',views.hot_community_baidu),
    path('View2/',views.street_view2),
    path('View4/',views.handle_view),

]