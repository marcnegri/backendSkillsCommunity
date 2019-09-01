from django.urls import path
from .quickstart.views import UserView
from .quickstart.views import SkillView
from .quickstart.views import SkillsGroupView
from .quickstart.views import ReviewView

urlpatterns = [
    path('users/', UserView.user_list),
    path('users/<int:pk>/', UserView.user_detail),
    path('skills/<int:pk>/', SkillView.skill_detail),
    path('skills/', SkillView.skill_list),
    path('skillsgroups/<int:pk>/', SkillsGroupView.skillsgroup_detail),
    path('skillsgroups/<int:skills_group_id>/skills/', SkillView.skill_list_by_group),
    path('skillsgroups/', SkillsGroupView.skillsgroup_list),
    path('reviews/', ReviewView.review_list),
    path('reviews/<int:pk>/', ReviewView.review_detail),
]