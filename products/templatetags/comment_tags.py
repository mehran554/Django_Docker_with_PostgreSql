from django import template

register = template.Library()


@register.filter
def only_active_comment_show(comments):
    return comments.filter(active=True)
