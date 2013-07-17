from django.template import Library

'''
Created on 12-Jul-2013

@author: ss
'''

register = Library()

@register.filter
def get_mod_3( value ):
    if value == 0:
        return 1
    return ( value ) % 3 