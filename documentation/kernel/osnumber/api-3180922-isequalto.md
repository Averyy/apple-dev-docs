# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the number with an OSNumber.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual bool isEqualTo(const OSNumber *aNumber);
```

#### Return_value

true iff the two numbers have the same value.

#### Discussion

If the passed OSNumber object has the same value, regardless of size, true is returned. Otherwise false is returned.

## Parameters

- `aNumber`: The OSNumber to compare with.

## See Also

- [- isEqualTo](osnumber/3434345-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/3180922-isequalto)*