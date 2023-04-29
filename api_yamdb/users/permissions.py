from rest_framework import permissions


class AdminAndSuperUser(permissions.BasePermission):
    """..."""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_superuser or request.user.is_admin
            or obj == request.user)
