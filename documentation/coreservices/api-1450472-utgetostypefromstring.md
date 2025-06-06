# UTGetOSTypeFromString(_:)

**Framework**: Core Services  
**Kind**: func

Decodes a tag string into an OSType.

**Availability**:
- macOS 10.3+ - Deprecated in 12.0

## Declaration

```swift
func UTGetOSTypeFromString(_ inString: CFString) -> OSType
```

#### Return_value

The OSType that was encoded in the string.

#### Discussion

You call this function to convert an OSType string returned by a UTI function back into the integer-based OSType.

## Parameters

- `inString`: A string that encodes an OSType.

## See Also

- [func UTCreateStringForOSType(OSType) -> Unmanaged<CFString>](1442804-utcreatestringforostype.md)
  Encodes an `OSType` into a string suitable for use as a tag argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1450472-utgetostypefromstring)*