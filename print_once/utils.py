import inspect
import builtins

_CALL_ONCE_COUNTER_DICT = dict()

def call_once(func, *args, identifier=None, max_times=1, **kwargs):

    if identifier is None:
        stack = inspect.stack()
        caller_frame = stack[1]
        file_name = caller_frame.filename
        line_number = caller_frame.lineno
        identifier = f"{file_name}:{line_number}"
    
    if func not in _CALL_ONCE_COUNTER_DICT:
        _CALL_ONCE_COUNTER_DICT[func] = dict()

    this_counter = _CALL_ONCE_COUNTER_DICT[func]

    this_counter[identifier] = this_counter.get(identifier, 0) + 1
    if this_counter[identifier] <= max_times:
        return func(*args, **kwargs)
    return None

def print_once(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file = None,
    flush = False,
    identifier=None,
    max_times=1,
):
    if identifier is None:
        stack = inspect.stack()
        caller_frame = stack[1]
        file_name = caller_frame.filename
        line_number = caller_frame.lineno
        identifier = f"{file_name}:{line_number}"
    
    return call_once(builtins.print, *values, sep=sep, end=end, file=file, flush=flush, identifier=identifier, max_times=max_times)