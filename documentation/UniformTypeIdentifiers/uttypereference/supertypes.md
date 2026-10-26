# supertypes

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Instance Property

The set of types the type directly or indirectly conforms to.

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
var supertypes: Set<UTType> { get }
```

```objc
@property (readonly) NSSet<UTType *> * supertypes;
```

## See Also

### Checking a type’s relationship to another type
- [- conformsToType:](./conforms%28to%29.md)
  Returns a Boolean value that indicates whether a type conforms to the type.
- [- isSubtypeOfType:](./issubtype%28of%29.md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [- isSupertypeOfType:](./issupertype%28of%29.md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/supertypes)*