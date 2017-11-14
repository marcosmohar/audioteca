# para crear premisos a nuestro gusto
from rest_framework.permissions import BasePermission
# 
from modules.users.models import User
# para definir que grupo va a tener permisos
from django.contrib.auth.models import Group

class GroupPataratasPermissions(BaseException):

    def _is_in_group(self, group_name, user):
        # regresa True si la id del usuario existe dentro del grupo pasado al request
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()


    def has_permission(self,request, view):
        if self._is_in_group('pataratas', request.user):
            return True
        else:
            return False