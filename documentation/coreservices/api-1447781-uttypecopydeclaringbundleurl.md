# UTTypeCopyDeclaringBundleURL(_:)

**Framework**: Core Services  
**Kind**: func

Returns the location of a bundle containing the declaration for a type.

**Availability**:
- iOS 3.0+ - Deprecated in 14.0
- iPadOS 3.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.3+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 7.0

## Declaration

```swift
func UTTypeCopyDeclaringBundleURL(_ inUTI: CFString) -> Unmanaged<CFURL>?
```

#### Return_value

A URL that points to the bundle that holds the uniform type identifier’s declaration, or `NULL` if a bundle that holds the declaration cannot be located.

## Parameters

- `inUTI`: A uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447781-uttypecopydeclaringbundleurl)*