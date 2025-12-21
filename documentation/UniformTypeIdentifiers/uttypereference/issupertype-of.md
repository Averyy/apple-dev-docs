# isSupertype(of:)

**Framework**: Uniform Type Identifiers  
**Kind**: method

Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func isSupertype(of type: UTType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `type` directly or indirectly conforms to the type, but returns [`false`](https://developer.apple.com/documentation/Swift/false) if it’s equal to the type.

## Parameters

- `type`: A   instance.

## See Also

- [var supertypes: Set<UTType>](uttype-swift.struct/supertypes.md)
  The set of types the type directly or indirectly conforms to.
- [func conforms(to: UTType) -> Bool](uttypereference/conforms(to:).md)
  Returns a Boolean value that indicates whether a type conforms to the type.
- [func isSubtype(of: UTType) -> Bool](uttypereference/issubtype(of:).md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/issupertype(of:))*