# init(filenameExtension:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: init

Creates a type based on a filename extension and an existing supertype that it conforms to.

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
init?(filenameExtension: String, conformingTo supertype: UTType = .data)
```

#### Discussion

If the system finds no types with the provided filename extension and conformance, but the inputs are otherwise valid, it may provide a dynamic type. The initializer returns `nil` if the parameters aren’t valid.

This initializer is equivalent to calling:

```swift
UTType(tag: filenameExtension,
       tagClass: .filenameExtension,
       conformingTo: supertype)
```

To get the type of a file on disk, use [`contentType`](https://developer.apple.com/documentation/foundation/urlresourcevalues/3551434-contenttype).

> ❗ **Important**:  You can’t always derive the type of a file system item based solely on its filename extension.

 You can’t always derive the type of a file system item based solely on its filename extension.

A type depends on other attributes in addition to the filename extension, including whether the item is a directory.

## Parameters

- `filenameExtension`: The filename extension.
- `supertype`: Another type that the resulting type must conform to; for example,   or  .

## See Also

- [init?(String)](uttype-swift.struct/init(_:).md)
  Creates a type based on an identifier.
- [init?(mimeType: String, conformingTo: UTType)](uttype-swift.struct/init(mimetype:conformingto:).md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [init?(tag: String, tagClass: UTTagClass, conformingTo: UTType?)](uttype-swift.struct/init(tag:tagclass:conformingto:).md)
  Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(exportedas:conformingto:).md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(importedas:conformingto:).md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(filenameextension:conformingto:))*