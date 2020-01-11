from rest_framework.permissions import BasePermission

class IsVoterChief(BasePermission):
    """Verify if user is voter chief"""

    def has_permission(self, request, view):
        """Verify user is voter chief"""
        return request.user.is_voting_chief


class IsVoterNode(BasePermission):
    """Verify if user is used in node"""

    def has_permission(self, request, view):
        """Verify user is voter node"""
        return request.user.is_voting_node


class IsStaff(BasePermission):
    """Verify if user is staff."""

    def has_permission(self, request, view):
        """Verify user is staff"""
        return request.user.is_staff
