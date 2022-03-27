from django.contrib.auth.mixins import AccessMixin


class AdminRequiredMixin(AccessMixin):
    """Убедитесь, что текущий пользователь является админом."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.status == 'admin':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)