# init(filenameExtension:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: init

Creates a type that represents the specified filename extension and conforms to an existing type.

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
convenience init?(filenameExtension: String, conformingTo supertype: UTType)
```

#### Discussion

If the system recognizes the filename extension, the intializer returns the corresponding type; otherwise, the initializer returns a dynamic type whose [`isDeclared`](uttype-swift.struct/isdeclared.md) and [`isPublic`](uttype-swift.struct/ispublic.md) properties are both set to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `filenameExtension`: The filename extension.
- `supertype`: The type the resulting type must conform to, such as   or  .

## See Also

- [convenience init?(String)](uttypereference/init(_:).md)
  Creates a type based on an identifier.
- [convenience init?(mimeType: String)](uttypereference/init(mimetype:).md)
  Creates a type based on a MIME type.
- [convenience init?(mimeType: String, conformingTo: UTType)](uttypereference/init(mimetype:conformingto:).md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [convenience init?(filenameExtension: String)](uttypereference/init(filenameextension:).md)
  Creates a type that represents the specified filename extension.
- [convenience init?(tag: String, tagClass: String, conformingToType: UTType?)](uttypereference/init(tag:tagclass:conformingtotype:).md)
  Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [init(exportedAs: String)](uttypereference/init(exportedas:).md)
  Creates a type your app owns based on an identifier.
- [init(exportedAs: String, conformingTo: UTType)](uttypereference/init(exportedas:conformingto:).md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String)](uttypereference/init(importedas:).md)
  Creates a type your app uses, but doesn’t own, based on an identifier.
- [init(importedAs: String, conformingTo: UTType)](uttypereference/init(importedas:conformingto:).md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(filenameextension:conformingto:))*