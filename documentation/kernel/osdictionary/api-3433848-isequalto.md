# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the dictionary with an OSObject

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const OSMetaClassBase *anObject);
```

#### Return_value

true iff the object is of class OSDictionary and isEqualTo(const OSDictionary * anArray) returns true.

#### Discussion

If the object is of class OSDictionary, the result of isEqualTo(const OSDictionary * anArray) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [- isEqualTo](osdictionary/3180902-isequalto.md)
  Compares certain members of two dictionaries with isEqualTo().
- [- isEqualTo](osdictionary/3433847-isequalto.md)
  Compares all members of two dictionaries with isEqualTo().


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3433848-isequalto)*