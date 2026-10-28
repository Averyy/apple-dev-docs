# preferredFilenameExtension

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Instance Property

The preferred filename extension for the type.

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
var preferredFilenameExtension: String? { get }
```

```objc
@property (readonly, nullable) NSString * preferredFilenameExtension;
```

## Discussion

If available, the preferred (first available) tag of class [`filenameExtension`](../uttagclass/filenameextension.md).

Many types require the generation of a filename; for example, when saving a file to disk. If not `nil`, the value of this property is the best available filename extension for this type.

The value of this property is equivalent to, but more efficient than:

```swift
type.tags[.filenameExtension]?.first
```

## See Also

### Obtaining tags
- [preferredMIMEType](./preferredmimetype.md)
  The preferred MIME type for the type.
- [tags](./tags.md)
  The tag specification dictionary of the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/preferredfilenameextension)*