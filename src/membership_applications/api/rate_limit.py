from slowapi import Limiter
from slowapi.util import get_remote_address

from membership_applications.api.config import api_settings

# Counts requests in-memory, per process -- there's no shared store (e.g.
# Redis) backing this. With ApiSettings.workers > 1, or multiple replicas,
# each process keeps its own counters, so a limit like "60/minute" on a
# route effectively becomes "60 x (workers x replicas) per minute" instead
# of a real global limit. Fine at 1 worker/1 replica; revisit with a shared
# storage backend before relying on this for a real rate-limiting guarantee.
limiter = Limiter(
    key_func=get_remote_address, default_limits=[api_settings.default_rate_limit]
)
