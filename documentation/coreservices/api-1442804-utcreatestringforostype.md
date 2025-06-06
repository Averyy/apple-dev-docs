# UTCreateStringForOSType(_:)

**Framework**: Core Services  
**Kind**: func

Encodes an `OSType` into a string suitable for use as a tag argument.

**Availability**:
- macOS 10.3+ - Deprecated in 12.0

## Declaration

```swift
func UTCreateStringForOSType(_ inOSType: OSType) -> Unmanaged<CFString>
```

#### Return_value

A string that encodes the OSType.

#### Discussion

The UTI functions assume that all alternate identifier tags can be represented as Core Foundation strings. OSTypes are integer-based rather than string-based, so to pass an OSType into a UTI function, you must call this function to convert it to a string.

## Parameters

- `inOSType`: The   to convert.

## See Also

- [func UTGetOSTypeFromString(CFString) -> OSType](1450472-utgetostypefromstring.md)
  Decodes a tag string into an OSType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442804-utcreatestringforostype)*