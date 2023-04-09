from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS: # safemethod ichida get bor agar get jonatsa korsatsin
            return True

        if request.user.is_authenticated and request.user.is_admin: # agar user bolsa va admin bolsa true bolmasa false
            return True
        return False
