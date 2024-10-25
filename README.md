
# print-once

`print-once` is a lightweight Python package designed to help you control the output of specific messages and function calls in your code. It ensures that messages are printed only a limited number of times, which can be useful for reducing console clutter and ensuring unique notifications.

It's well-suited for certain debugging scenarios, such as printing tensor or hyperparameter information only on the first step or the first call during deep learning training.

## Installation

Install `print-once` via pip:

```bash
pip install print-once
```

## Usage

### `print_once`

Use `print_once` as an alternative to `print`. It will display a message only once, or a specified number of times.

```python
from print_once import print_once

for i in range(100):
    print_once(f"called {i}")  # This line will be printed only once

for i in range(10, 20):
    print_once(f"called {i}", max_times=3)  # This line is printed up to 3 times
```

In the example above, the output will be:

```
called 0
called 10
called 11
called 12
```

**Note**: `print_once` identifies unique calls based on *file path* and *line number*, so calls on different lines will be treated separately. You can understand it as that each line using `print_once` will execute only once.

### `call_once`

It also provides a `call_once` function to ensure a custom function is executed only once.

```python
from print_once import call_once

def my_func(x, y):
    print(f'{x} + {y} = {x + y}')

for i in range(100):
    # `my_func` will be called only once
    call_once(my_func, i, i + 1)
```

The result will be:
```
0 + 1 = 1
```
