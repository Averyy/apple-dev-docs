# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the data with an OSString

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const OSString *aString);
```

#### Return_value

true if the OSData and OSString contain the same c-string.

#### Discussion

If the passed OSString object has the same length and all bytes are identical, true is returned. If the passed OSString object has a length one byte less than the OSData, all bytes are identical, and the last byte of the OSData is zero, true is returned. Otherwise false is returned.

## Parameters

- `aString`: The object to compare with.

## See Also

- [- isEqualTo](osdata/3180882-isequalto.md)
  Compares the data with an OSData
- [- isEqualTo](osdata/3433844-isequalto.md)
  Compares the data with a pointer to bytes
- [- isEqualTo](osdata/3433858-isequalto.md)
  Compares the data with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433843-isequalto)*