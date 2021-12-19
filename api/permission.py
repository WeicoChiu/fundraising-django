from rest_framework import permissions


class AdminCreateOrModeifyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or bool(request.user and request.user.is_staff)

class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or bool(request.user and request.user.is_authenticated)

class ProjectOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method == 'GET' and bool(request.user and request.user.is_authenticated)) or \
                obj.projectowner.user == request.user
