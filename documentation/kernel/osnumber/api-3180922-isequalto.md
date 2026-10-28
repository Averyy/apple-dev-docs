# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the number with an OSNumber.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const OSNumber *aNumber);
```

*macOS*

```cpp
virtual bool isEqualTo(const OSNumber *aNumber);
```

## Return Value

true iff the two numbers have the same value.

## Discussion

If the passed OSNumber object has the same value, regardless of size, true is returned. Otherwise false is returned.

## Parameters

- `aNumber`: The OSNumber to compare with.

## See Also

### Comparing Numbers
- [- isEqualTo](./api-3434345-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/3180922-isequalto)*