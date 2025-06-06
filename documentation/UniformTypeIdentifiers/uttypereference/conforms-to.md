# conforms(to:)

**Framework**: Uniform Type Identifiers  
**Kind**: method

Returns a Boolean value that indicates whether a type conforms to the type.

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
func conforms(to type: UTType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the type directly or indirectly conforms to `type`, or if it’s equal to `type`.

## Parameters

- `type`: An   instance.

## See Also

- [var supertypes: Set<UTType>](uttype-swift.struct/supertypes.md)
  The set of types the type directly or indirectly conforms to.
- [func isSubtype(of: UTType) -> Bool](uttypereference/issubtype(of:).md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [func isSupertype(of: UTType) -> Bool](uttypereference/issupertype(of:).md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/conforms(to:))*