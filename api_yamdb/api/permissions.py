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
        if not user.is_anonymous:
            if user.role == 'user' or user.role == 'moderator':
                return False
        # if request.method == 'GET':
        #     return False
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


class CommentPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not user.is_anonymous:
            if request.method == 'PATCH' and user.role == 'user' \
                    and obj.author_id != user.id:
                return False
            if request.method == 'DELETE' and user.role == 'user' \
                    and obj.author_id == user.id:
                return True
            if request.method == 'DELETE' and user.role == 'user' \
                    and obj.author_id != user.id:
                return False
        return (user.is_authenticated
                and (obj.author == user or user.is_admin or user.is_moderator)
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
