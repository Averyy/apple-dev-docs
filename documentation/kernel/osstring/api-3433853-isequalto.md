# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Compares the string with a c-string.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool isEqualTo(const char *cString);
```

#### Return_value

true iff the two strings have the same length and characters.

#### Discussion

If the passed c-string has the same length and all characters are identical to those in the OSString, true is returned. Otherwise false is returned.

## Parameters

- `cString`: The c-string to compare with.

## See Also

- [- isEqualTo](osstring/3180976-isequalto.md)
  Compares the string with an OSString.
- [- isEqualTo](osstring/3433852-isequalto.md)
  Compares the string with an OSData.
- [- isEqualTo](osstring/3434577-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3433853-isequalto)*