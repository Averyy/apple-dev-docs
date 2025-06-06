# mimeType

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type property that returns the tag class used to map a type to a MIME type.

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
static var mimeType: UTTagClass { get }
```

#### Discussion

The tag class for MIME types such as `text/plain`. The raw value of this tag class is `public.mime-type`.

## See Also

- [static var filenameExtension: UTTagClass](uttagclass/filenameextension.md)
  A type property that returns the tag class used to map a type to a filename extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass/mimetype)*