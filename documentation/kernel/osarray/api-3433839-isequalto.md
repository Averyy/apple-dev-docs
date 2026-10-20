# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the array with an OSObject

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```cpp
virtual bool isEqualTo(const OSMetaClassBase *anObject);
```

#### Return Value

true iff the object is of class OSArray and isEqualTo(const OSArray * anArray) returns true.

#### Discussion

If the object is of class OSArray, the result of isEqualTo(const OSArray * anArray) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

### Comparing Arrays
- [- isEqualTo](./api-3180817-isequalto.md)
  Compares all members of two arrays with isEqualTo().


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3433839-isequalto)*