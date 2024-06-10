from rest_framework import permissions



#in this permission only created user and owner can perform action otherwise read only permissions

class IsOwnerOrSuperuserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_superuser
    




