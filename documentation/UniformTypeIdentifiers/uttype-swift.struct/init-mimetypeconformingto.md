# init(mimeType:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: init

Creates a type based on a MIME type and a supertype that it conforms to.

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
init?(mimeType: String, conformingTo supertype: UTType = .data)
```

#### Discussion

This initializer is equivalent to calling:

```swift
UTType(tag: mimeType,
       tagClass: .mimeType,
       conformingTo: supertype)
```

The initializer may provide a dynamic type if the parameters are valid, but the system doesn’t find any types with the MIME type and conformance. The initializer returns `nil` if the parameters aren’t valid.

## Parameters

- `mimeType`: A string that represents the MIME type.
- `supertype`: Another   instance that the resulting type must conform to; for example,  .

## See Also

- [init?(String)](uttype-swift.struct/init(_:).md)
  Creates a type based on an identifier.
- [init?(filenameExtension: String, conformingTo: UTType)](uttype-swift.struct/init(filenameextension:conformingto:).md)
  Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init?(tag: String, tagClass: UTTagClass, conformingTo: UTType?)](uttype-swift.struct/init(tag:tagclass:conformingto:).md)
  Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(exportedas:conformingto:).md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(importedas:conformingto:).md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(mimetype:conformingto:))*