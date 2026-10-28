# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the string with a c-string.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const char *cString);
```

*macOS*

```cpp
virtual bool isEqualTo(const char *cString);
```

## Return Value

true iff the two strings have the same length and characters.

## Discussion

If the passed c-string has the same length and all characters are identical to those in the OSString, true is returned. Otherwise false is returned.

## Parameters

- `cString`: The c-string to compare with.

## See Also

### Comparing Strings
- [- isEqualTo](./api-3180976-isequalto.md)
  Compares the string with an OSString.
- [- isEqualTo](./api-3433852-isequalto.md)
  Compares the string with an OSData.
- [- isEqualTo](./api-3434577-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3433853-isequalto)*