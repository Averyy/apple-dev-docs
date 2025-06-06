# identifier

**Framework**: Uniform Type Identifiers  
**Kind**: property

The string that represents the type.

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
var identifier: String { get }
```

#### Discussion

The identifier uniquely identifies its type, represented by a reverse-DNS string, such as `public.jpeg` or `com.adobe.pdf`.

API that doesn’t use [`UTType`](uttype-swift.struct.md) uses a `String` or [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) to refer to a type by its identifier.

## See Also

- [typealias ReferenceType](uttype-swift.struct/referencetype.md)
  An alias for the associated reference type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/identifier)*