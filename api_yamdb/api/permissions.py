from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorAdminModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.user.is_admin
            or request.user.is_moderator
            or obj.author == request.user
        )


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_anonymous:
            if user.role == 'user' or user.role == 'moderator':
                return False
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


class CategoryPermissions(BasePermission):
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
