# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the string with an OSObject

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

If the object is of class OSString, the result of isEqualTo(const OSString * aDataObj) is returned. If the object is of class OSData, the result of isEqualTo(const OSData * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [- isEqualTo](osstring/3180976-isequalto.md)
  Compares the string with an OSString.
- [- isEqualTo](osstring/3433852-isequalto.md)
  Compares the string with an OSData.
- [- isEqualTo](osstring/3433853-isequalto.md)
  Compares the string with a c-string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3434577-isequalto)*