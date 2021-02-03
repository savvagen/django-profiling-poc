from drf_yasg2.openapi import Parameter, IN_QUERY, IN_PATH
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import action, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from constance import config


class SentryPerformanceViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]

    @action(methods=["GET"], detail=False)
    @swagger_auto_schema(manual_parameters=[Parameter('enable', IN_QUERY, type='boolean'), ])
    # @permission_classes((permissions.IsAdminUser,))
    def enable_sentry_tracing(self, *args, **kwargs):
        cond = self.request.GET.get('enable', False)  # self.request.query_params["enabled"]
        enable = True if cond.lower() == 'true' else False
        config.SENTRY_TRACING_ENABLED = enable
        return Response(data={
            "message": f"Success. Tracing Status changed.",
            "sentry_tracing_enabled": config.SENTRY_TRACING_ENABLED
        })


    @action(methods=["GET"], detail=False)
    # @permission_classes((permissions.IsAuthenticated,))
    def check_tracing_is_enabled(self, *args, **kwargs):
        return Response(data={"sentry_tracing_enabled": config.SENTRY_TRACING_ENABLED})
