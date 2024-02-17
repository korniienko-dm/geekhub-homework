from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only access to anyone,
    but only allow write access to admin users.
    """

    def has_permission(self, request, view):
        """Check if the user has permission to perform the requested action."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """Custom permission to allow read-only access to anyone,
    but only allow write access to authenticated users."""

    def has_permission(self, request, view):
        """Check if the user has permission to perform the requested action."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
