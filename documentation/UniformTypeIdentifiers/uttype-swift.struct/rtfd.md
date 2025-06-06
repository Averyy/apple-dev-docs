# rtfd

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents Rich Text Format Directory documents.

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
static var rtfd: UTType { get }
```

#### Discussion

RTFD is RTF with content embedded in its on-disk format.

The identifier for this type is `com.apple.rtfd`.

This type conforms to [`UTTypePackage`](uttypepackage.md) and [`UTTypeCompositeContent`](uttypecompositecontent.md).

## See Also

- [static var pdf: UTType](uttype-swift.struct/pdf.md)
  A type that represents Adobe Portable Document Format (PDF) documents.
- [static var flatRTFD: UTType](uttype-swift.struct/flatrtfd.md)
  A type that represents flattened Rich Text Format Directory documents.
- [static var epub: UTType](uttype-swift.struct/epub.md)
  A type that represents data in the electronic publication (EPUB) format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/rtfd)*