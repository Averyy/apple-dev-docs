# init(tag:tagClass:conformingToType:)

**Framework**: Uniform Type Identifiers  
**Kind**: init  
**Role**: Initializer

Creates a type that represents the specified tag and tag class and which conforms to an existing type.

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
convenience init?(tag: String, tagClass: String, conformingToType supertype: UTType?)
```

## Discussion

If the system recognizes the filename extension, the intializer returns the corresponding type; otherwise, the initializer returns a dynamic type whose [`isDeclared`](../uttype-swift.struct/isdeclared.md) and [`isPublic`](../uttype-swift.struct/ispublic.md) properties are both set to [`false`](../../Swift/false.md).

## Parameters

- `tag`: The tag, such as a filename extension.
- `tagClass`: The appropriate tag class, such as [`filenameExtension`](../uttagclass/filenameextension.md).
- `supertype`: The type the resulting type must conform to, such as [`data`](../uttype-swift.struct/data.md).

## See Also

### Creating a type
- [convenience init?(String)](./init%28_%29.md)
  Creates a type based on an identifier.
- [convenience init?(mimeType: String)](./init%28mimetype%29-1txq0.md)
  Creates a type based on a MIME type.
- [convenience init?(mimeType: String, conformingTo: UTType)](./init%28mimetype,conformingto%29.md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [convenience init?(filenameExtension: String)](./init%28filenameextension%29.md)
  Creates a type that represents the specified filename extension.
- [convenience init?(filenameExtension: String, conformingTo: UTType)](./init%28filenameextension,conformingto%29.md)
  Creates a type that represents the specified filename extension and conforms to an existing type.
- [init(exportedAs: String)](./init%28exportedas%29.md)
  Creates a type your app owns based on an identifier.
- [init(exportedAs: String, conformingTo: UTType)](./init%28exportedas,conformingto%29.md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String)](./init%28importedas%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier.
- [init(importedAs: String, conformingTo: UTType)](./init%28importedas,conformingto%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(tag:tagclass:conformingtotype:))*