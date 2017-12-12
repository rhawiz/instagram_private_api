# flake8: noqa

from instagram_private_api.client import Client
from instagram_private_api.compatpatch import ClientCompatPatch
from instagram_private_api.errors import (
    ClientError, ClientLoginError, ClientLoginRequiredError,
    ClientCookieExpiredError, ClientThrottledError, ClientConnectionError
)
from .endpoints.upload import MediaRatios
from .endpoints.common import MediaTypes


__version__ = '1.3.6'
