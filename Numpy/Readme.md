# Conditional selection

It is possible to make in Numpy conditional selection like Matlab

## Requirements

- Numpy library

```python
import numpy as np
```

## Instructions

First we generate a matrix with random values

```python
a = np.random.randint(2, 10, size =(10,10))
```

## Example of selection

```python
b = a > 2
```

It generate the following result:

## Selection of element in an array

### Selection with greater values

```python
a[a>3]
```

### Selection with equal values

```python
a[a==3]
```

## References

- [https://www.youtube.com/watch?v=ndCUJ9-Kn0U&t=78s](https://www.youtube.com/watch?v=ndCUJ9-Kn0U&t=78s)
