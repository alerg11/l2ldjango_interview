from django import template

register = template.Library()

@register.filter(name="l2l_dt")
def l2l_dt(value):
    if isinstance(value, str):
        return value.replace("T", " ")
    else:
        return value.strftime("%Y-%m-%d %H:%M:%S")