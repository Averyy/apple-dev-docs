# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the array with an OSObject

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const OSMetaClassBase *anObject);
```

#### Return_value

true iff the object is of class OSArray and isEqualTo(const OSArray * anArray) returns true.

#### Discussion

If the object is of class OSArray, the result of isEqualTo(const OSArray * anArray) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [- isEqualTo](osarray/3180817-isequalto.md)
  Compares all members of two arrays with isEqualTo().


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3433839-isequalto)*