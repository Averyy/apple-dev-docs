# cmEmbeddedUseMask

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmEmbeddedUseMask: Int { get }
```

#### Discussion

This mask provides access to bit 1 of the `flags` field, which specifies whether the profile can be used independently or can only be used as an embedded profile. It has the value 0 if the profile can be used anywhere, 1 if it must be embedded.

You should interpret the setting of this bit as an indication of copyright protection. If the profile developer set this bit to 1, you should use this profile as an embedded profile only and not copy the profile for your own purposes. The profile developer also specifies explicit copyright intention using the `cmCopyrightTag` profile tag (defined in the `CMICCProfile.h` header file).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmembeddedusemask)*