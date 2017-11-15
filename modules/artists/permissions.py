from rest_framework.permissions import BasePermission 
from modules.users.models import User
from django.contrib.auth.models import Group

class GroupPatatasPermissions(BaseException):

    def _is_in_group(self, group_name, user):
        # regresa True si la id del usuario existe dentro del grupo pasado al request
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()


    def has_permission(self,request, view):
        if self._is_in_group('patatas', request.user):
            return True
        else:
            return False