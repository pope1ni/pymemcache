# API Backwards compatibility

from pymemcache.client.base import Client  # noqa: F401
from pymemcache.client.base import PooledClient  # noqa: F401
from pymemcache.client.hash import HashClient  # noqa: F401

from pymemcache.exceptions import MemcacheError  # noqa: F401
from pymemcache.exceptions import MemcacheClientError  # noqa: F401
from pymemcache.exceptions import MemcacheUnknownCommandError  # noqa: F401
from pymemcache.exceptions import MemcacheIllegalInputError  # noqa: F401
from pymemcache.exceptions import MemcacheServerError  # noqa: F401
from pymemcache.exceptions import MemcacheUnknownError  # noqa: F401
from pymemcache.exceptions import MemcacheUnexpectedCloseError  # noqa: F401
