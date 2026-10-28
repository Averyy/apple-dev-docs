# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the string with an OSString.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const OSString *aString);
```

*macOS*

```cpp
virtual bool isEqualTo(const OSString *aString);
```

## Return Value

true iff the two strings have the same length and characters.

## Discussion

If the passed OSString object has the same length and all characters are identical, true is returned. Otherwise false is returned.

## Parameters

- `aString`: The OSString to compare with.

## See Also

### Comparing Strings
- [- isEqualTo](./api-3433852-isequalto.md)
  Compares the string with an OSData.
- [- isEqualTo](./api-3433853-isequalto.md)
  Compares the string with a c-string.
- [- isEqualTo](./api-3434577-isequalto.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3180976-isequalto)*