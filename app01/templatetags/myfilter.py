#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from django import template
register=template.Library()

@register.filter(name="add_sb")
def add_sb(arg):
    return "{} sb.".format(arg)

@register.filter(name="cut")
def cut(value,arg):
    return value.replace(arg,'')