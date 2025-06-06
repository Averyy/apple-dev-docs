# tags

**Framework**: Uniform Type Identifiers  
**Kind**: property

The tag specification dictionary of the type.

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
var tags: [UTTagClass : [String]] { get }
```

#### Discussion

Uniform Type Identifiers don’t store tag information for nonstandard tag classes. Identifiers normalize string values into arrays that contain those strings. For example, a tag specification dictionary with values of:

```other
{
    "public.mime-type": "x/y",
    "nonstandard-tag-class": "abc",
}
```

Normalizes to:

```other
{
    "public.mime-type": ["x/y"]
}
```

Use the tag class [`mimeType`](uttagclass/mimetype.md) or [`filenameExtension`](uttagclass/filenameextension.md) to retrieve the list of supporting MIME types or filename extensions for your type. For example, the following example retrieves a list of the filename extensions for the [`mpeg`](uttype-swift.struct/mpeg.md) type:

```swift
let MPEGextensions = UTType.mpeg.tags[.filenameExtension]
```

Types that have no tags for the requested tag class return a nil, not an empty array.

To get the preferred filename extension or MIME type, use the tag class [`preferredFilenameExtension`](uttype-swift.struct/preferredfilenameextension.md) or [`preferredMIMEType`](uttype-swift.struct/preferredmimetype.md), respectively.

## See Also

- [var preferredFilenameExtension: String?](uttype-swift.struct/preferredfilenameextension.md)
  The preferred filename extension for the type.
- [var preferredMIMEType: String?](uttype-swift.struct/preferredmimetype.md)
  The preferred MIME type for the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/tags)*