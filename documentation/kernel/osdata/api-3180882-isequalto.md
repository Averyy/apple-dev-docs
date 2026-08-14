# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the data with an OSData

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual bool isEqualTo(const OSData *aDataObj);
```

#### Return_value

true iff the object is of class OSArray and isEqualTo(const OSArray * anArray) returns true.

#### Discussion

If the passed OSData object has the same length and all bytes are identical, true is returned. Otherwise false is returned.

## Parameters

- `aDataObj`: The OSData to compare with.

## See Also

- [- isEqualTo](osdata/3433843-isequalto.md)
  Compares the data with an OSString
- [- isEqualTo](osdata/3433844-isequalto.md)
  Compares the data with a pointer to bytes
- [- isEqualTo](osdata/3433858-isequalto.md)
  Compares the data with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180882-isequalto)*