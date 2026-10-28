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

## Return Value

true iff the object is of class OSNumber isEqualTo() returns true.

## Discussion

If the object is of class OSNumber, the result of isEqualTo(const OSNumber * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

### Comparing Numbers
- [- isEqualTo](./api-3180922-isequalto.md)
  Compares the number with an OSNumber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/3434345-isequalto)*