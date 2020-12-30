from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists() #true or false
        return not blocked

class AnnonPermissionOnly(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    message = "You are already authenticated.." #To display custom message

    def has_permission(self, request, view):
        return not request.user.is_authenticated

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = "You must be the owner of the content to change it." #To display custom message

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.owner == request.user)
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user