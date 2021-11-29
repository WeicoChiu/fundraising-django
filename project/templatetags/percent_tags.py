from django import template
from  project.models import Project
import math

register = template.Library()

@register.simple_tag()
def percent_goal(project):
    percent = project.total_donate/project.goal * 100
    return math.floor(percent)