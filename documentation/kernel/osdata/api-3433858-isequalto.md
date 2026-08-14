# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the data with an OSObject

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const OSMetaClassBase *anObject);
```

#### Return_value

true iff the object is of class OSData or OSString and isEqualTo() returns true.

#### Discussion

If the object is of class OSData, the result of isEqualTo(const OSData * aDataObj) is returned. If the object is of class OSString, the result of OSString::isEqualTo(const OSData * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [- isEqualTo](osdata/3180882-isequalto.md)
  Compares the data with an OSData
- [- isEqualTo](osdata/3433843-isequalto.md)
  Compares the data with an OSString
- [- isEqualTo](osdata/3433844-isequalto.md)
  Compares the data with a pointer to bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433858-isequalto)*