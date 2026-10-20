# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the string with an OSData.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const OSData *aDataObject);
```

*macOS*

```cpp
virtual bool isEqualTo(const OSData *aDataObject);
```

#### Return Value

true if the OSData and OSString contain the same c-string.

#### Discussion

If the passed OSData object has the same length and all bytes are identical, true is returned. If the passed OSData object has a length one byte greater than the OSString, all bytes are identical, and the last byte of the OSData is zero, true is returned. Otherwise false is returned.

## Parameters

- `aDataObject`: The OSData to compare with.

## See Also

### Comparing Strings
- [- isEqualTo](./api-3180976-isequalto.md)
  Compares the string with an OSString.
- [- isEqualTo](./api-3433853-isequalto.md)
  Compares the string with a c-string.
- [- isEqualTo](./api-3434577-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3433852-isequalto)*