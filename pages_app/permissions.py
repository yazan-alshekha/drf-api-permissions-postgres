from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):

        # read only permission
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permission
        return obj.author ==request.user