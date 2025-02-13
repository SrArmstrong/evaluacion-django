from rest_framework import permissions

class EsAdministrador(permissions.BasePermission):
    "Permite editar y añadir solo a los administradores."
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Administrador').exists()

class EsEliminador(permissions.BasePermission):
    "Permite eliminar solo a los del grupo Eliminador."
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Eliminador').exists()

class EsVisualizador(permissions.BasePermission):
    "Permite solo ver los datos."
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Visualizador').exists()
