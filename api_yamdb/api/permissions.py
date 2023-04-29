from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorAdminModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return (user.is_authenticated
                and (obj.author == user or user.is_admin or user.is_moderator)
                )


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            request.method in SAFE_METHODS
            or user.is_authenticated and user.is_admin
        )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            request.method in SAFE_METHODS
            or user.is_authenticated and user.is_admin
        )