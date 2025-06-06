# UTTypeCopyDescription(_:)

**Framework**: Core Services  
**Kind**: func

Returns the localized, user-readable type description string associated with a uniform type identifier.

**Availability**:
- iOS 3.0+ - Deprecated in 15.0
- iPadOS 3.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.3+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

## Declaration

```swift
func UTTypeCopyDescription(_ inUTI: CFString) -> Unmanaged<CFString>?
```

#### Return_value

A localized string describing the type, or `NULL` if no type description is available.

#### Discussion

The localized string that describes the uniform type is found in the type’s declaration.

## Parameters

- `inUTI`: A uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448514-uttypecopydescription)*