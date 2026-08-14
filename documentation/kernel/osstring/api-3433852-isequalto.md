# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the string with an OSData.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const OSData *aDataObject);
```

#### Return_value

true if the OSData and OSString contain the same c-string.

#### Discussion

If the passed OSData object has the same length and all bytes are identical, true is returned. If the passed OSData object has a length one byte greater than the OSString, all bytes are identical, and the last byte of the OSData is zero, true is returned. Otherwise false is returned.

## Parameters

- `aDataObject`: The OSData to compare with.

## See Also

- [- isEqualTo](osstring/3180976-isequalto.md)
  Compares the string with an OSString.
- [- isEqualTo](osstring/3433853-isequalto.md)
  Compares the string with a c-string.
- [- isEqualTo](osstring/3434577-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3433852-isequalto)*