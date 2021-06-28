from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('who-we-are', views.who_we_are, name='who_we_are'),
	path('our-work', views.our_work, name='our_work'),
	path('faq', views.faq, name='faq'),
	path('work-with-us', views.work_with_us, name='work_with_us'),

	path('blogs', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<pk>/publish', views.post_publish, name='post_publish'),
	path('post/<pk>/remove/', views.post_remove, name='post_remove'),

	path('share-your-story/', views.share_your_story, name='survivor_story'),
    path('new-story', views.new_story, name='new_story'),
]
