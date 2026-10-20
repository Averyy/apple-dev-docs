# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the string with an OSObject

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```cpp
virtual bool isEqualTo(const OSMetaClassBase *anObject);
```

#### Return Value

true iff the object is of class OSData or OSString and isEqualTo() returns true.

#### Discussion

If the object is of class OSString, the result of isEqualTo(const OSString * aDataObj) is returned. If the object is of class OSData, the result of isEqualTo(const OSData * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

### Comparing Strings
- [- isEqualTo](./api-3180976-isequalto.md)
  Compares the string with an OSString.
- [- isEqualTo](./api-3433852-isequalto.md)
  Compares the string with an OSData.
- [- isEqualTo](./api-3433853-isequalto.md)
  Compares the string with a c-string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3434577-isequalto)*