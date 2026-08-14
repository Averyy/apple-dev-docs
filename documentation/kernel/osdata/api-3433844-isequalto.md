# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the data with a pointer to bytes

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const void *bytes, unsigned int numBytes);
```

#### Return_value

true iff the length of the data are equal and all bytes are identical.

#### Discussion

If the passed data has the same length and all bytes are identical, true is returned. Otherwise false is returned.

## Parameters

- `bytes`: C-pointer to untyped data.
- `numBytes`: Count of bytes to be compared.

## See Also

- [- isEqualTo](osdata/3180882-isequalto.md)
  Compares the data with an OSData
- [- isEqualTo](osdata/3433843-isequalto.md)
  Compares the data with an OSString
- [- isEqualTo](osdata/3433858-isequalto.md)
  Compares the data with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433844-isequalto)*