# type: ignore[attr-defined]
"""one day, SEQuence problems got the qUEen's END ordER, the codename is SEQUEENDER."""

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
