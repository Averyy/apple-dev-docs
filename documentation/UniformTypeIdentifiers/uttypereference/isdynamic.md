# isDynamic

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system generates the type.

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
var isDynamic: Bool { get }
```

```objc
@property (readonly, getter=isDynamic) BOOL dynamic;
```

#### Discussion

The system recognizes dynamic types, but they may not be directly declared or claimed by an app. The system returns dynamic types when it encounters a file whose metadata doesn’t have a corresponding type known to the system.

The system either declares a type or dynamically generates a type, but not both.

## See Also

### Obtaining additional type information
- [var isDeclared: Bool](./isdeclared.md)
  A Boolean value that indicates whether the system declares the type.
- [var isPublic: Bool](./ispublic.md)
  A Boolean value that indicates whether the type is in the public domain.
- [var referenceURL: URL?](../uttype-swift.struct/referenceurl.md)
  The reference URL for the type.
- [var version: Int?](../uttype-swift.struct/version.md)
  The type’s version, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/isdynamic)*