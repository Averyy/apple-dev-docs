# filenameExtension

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type property that returns the tag class used to map a type to a filename extension.

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
static var filenameExtension: UTTagClass { get }
```

#### Discussion

The tag class for filename extensions such as `txt`.

Don’t include the leading period (`.`) character in the tag; it isn’t part of the filename extension.

The raw value of this tag class is `public.filename-extension`.

## See Also

- [static var mimeType: UTTagClass](uttagclass/mimetype.md)
  A type property that returns the tag class used to map a type to a MIME type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass/filenameextension)*