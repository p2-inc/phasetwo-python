"""Python client for the Phase Two Admin REST API.

The API classes and models are generated into ``phasetwo.openapi`` by
https://github.com/p2-inc/phasetwo-sdk-generator and re-exported here, so
``from phasetwo import OrganizationsApi`` works. Hand-written helpers live next to
this file; never edit ``phasetwo/openapi`` by hand.
"""

from importlib.metadata import PackageNotFoundError, version as _version

from phasetwo.openapi import *  # noqa: F401,F403
from phasetwo.openapi import __all__ as _generated_all

try:
    __version__ = _version("phasetwo-sdk")
except PackageNotFoundError:  # running from a source checkout
    __version__ = "0.0.0"

__all__ = list(_generated_all)
