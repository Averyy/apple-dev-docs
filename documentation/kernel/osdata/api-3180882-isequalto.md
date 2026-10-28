# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the data with an OSData

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const OSData *aDataObj);
```

*macOS*

```cpp
virtual bool isEqualTo(const OSData *aDataObj);
```

## Return Value

true iff the object is of class OSArray and isEqualTo(const OSArray * anArray) returns true.

## Discussion

If the passed OSData object has the same length and all bytes are identical, true is returned. Otherwise false is returned.

## Parameters

- `aDataObj`: The OSData to compare with.

## See Also

### Comparing Data Objects
- [- isEqualTo](./api-3433843-isequalto.md)
  Compares the data with an OSString
- [- isEqualTo](./api-3433844-isequalto.md)
  Compares the data with a pointer to bytes
- [- isEqualTo](./api-3433858-isequalto.md)
  Compares the data with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180882-isequalto)*