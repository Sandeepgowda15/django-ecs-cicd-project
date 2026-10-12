import ipaddress

ALB_HEALTHCHECK_NETWORKS = (
    ipaddress.ip_network("172.31.0.0/20"),
    ipaddress.ip_network("172.31.80.0/20"),
)

ALLOWED_HEALTHCHECK_HOST = (
    "django-app-alb-2034587205.us-east-1.elb.amazonaws.com"
)


class ALBHealthCheckHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health/":
            host = request.META.get("HTTP_HOST", "").split(":")[0]

            try:
                host_ip = ipaddress.ip_address(host)
            except ValueError:
                host_ip = None

            if host_ip and any(
                host_ip in network
                for network in ALB_HEALTHCHECK_NETWORKS
            ):
                request.META["HTTP_HOST"] = ALLOWED_HEALTHCHECK_HOST

        return self.get_response(request)
