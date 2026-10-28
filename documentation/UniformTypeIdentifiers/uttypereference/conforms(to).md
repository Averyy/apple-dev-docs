# conforms(to:)

**Framework**: Uniform Type Identifiers  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) conformsToType:(UTType *) type;
```

## Return Value

[`true`](../../Swift/true.md) if the type directly or indirectly conforms to `type`, or if it’s equal to `type`.

## Parameters

- `type`: An [`UTType`](../uttype-swift.struct.md) instance.

## See Also

### Checking a type’s relationship to another type
- [var supertypes: Set<UTType>](../uttype-swift.struct/supertypes.md)
  The set of types the type directly or indirectly conforms to.
- [func isSubtype(of: UTType) -> Bool](./issubtype%28of%29.md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [func isSupertype(of: UTType) -> Bool](./issupertype%28of%29.md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
- [supertypes](./supertypes.md)
  The set of types the type directly or indirectly conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/conforms(to:))*