# init(filenameExtension:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: init  
**Role**: Initializer

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

## Discussion

If the system finds no types with the provided filename extension and conformance, but the inputs are otherwise valid, it may provide a dynamic type. The initializer returns `nil` if the parameters aren’t valid.

This initializer is equivalent to calling:

```swift
UTType(tag: filenameExtension,
       tagClass: .filenameExtension,
       conformingTo: supertype)
```

To get the type of a file on disk, use [`contentType`](../../Foundation/urlresourcevalues/contenttype.md).

> ❗ **Important**:  You can’t always derive the type of a file system item based solely on its filename extension.

A type depends on other attributes in addition to the filename extension, including whether the item is a directory.

## Parameters

- `filenameExtension`: The filename extension.
- `supertype`: Another type that the resulting type must conform to; for example, [`UTTypeData`](../uttypedata.md) or [`UTTypePackage`](../uttypepackage.md).

## See Also

### Creating a type
- [init?(String)](./init%28_%29.md)
  Creates a type based on an identifier.
- [init?(mimeType: String, conformingTo: UTType)](./init%28mimetype,conformingto%29.md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [init?(tag: String, tagClass: UTTagClass, conformingTo: UTType?)](./init%28tag,tagclass,conformingto%29.md)
  Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs: String, conformingTo: UTType?)](./init%28exportedas,conformingto%29.md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String, conformingTo: UTType?)](./init%28importedas,conformingto%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(filenameextension:conformingto:))*