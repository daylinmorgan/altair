from toolz import curried
from ..utils.core import sanitize_dataframe
from ..utils.data import (
    MaxRowsError,
    curry,
    limit_rows,
    pipe,
    sample,
    to_csv,
    to_json,
    to_values,
    check_data_type,
)
from ..utils.data import DataTransformerRegistry as _DataTransformerRegistry
from ..utils.data import _DataType, _ToValuesReturnType
from ..utils.plugin_registry import PluginEnabler


@curried.curry
def default_data_transformer(
    data: _DataType, max_rows: int = 5000
) -> _ToValuesReturnType:
    return curried.pipe(data, limit_rows(max_rows=max_rows), to_values)


class DataTransformerRegistry(_DataTransformerRegistry):
    def disable_max_rows(self) -> PluginEnabler:
        """Disable the MaxRowsError."""
        options = self.options
        if self.active == "default":
            options = options.copy()
            options["max_rows"] = None
        return self.enable(**options)


__all__ = (
    "DataTransformerRegistry",
    "MaxRowsError",
    "curry",
    "sanitize_dataframe",
    "default_data_transformer",
    "limit_rows",
    "pipe",
    "sample",
    "to_csv",
    "to_json",
    "to_values",
    "check_data_type",
)
