# preferredMIMEType

**Framework**: Uniform Type Identifiers  
**Kind**: property

The preferred MIME type for the type.

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
var preferredMIMEType: String? { get }
```

#### Discussion

If available, the preferred (first available) tag of class [`mimeType`](uttagclass/mimetype.md). If not `nil`, the value of this property is the best available MIME type value for this type.

The value of this property is equivalent to, but more efficient than:

```swift
type.tags[.mimeType]?.first
```

## See Also

- [var preferredFilenameExtension: String?](uttype-swift.struct/preferredfilenameextension.md)
  The preferred filename extension for the type.
- [var tags: [UTTagClass : [String]]](uttype-swift.struct/tags.md)
  The tag specification dictionary of the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/preferredmimetype)*