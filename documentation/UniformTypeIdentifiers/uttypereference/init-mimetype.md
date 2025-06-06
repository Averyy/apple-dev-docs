# init(mimeType:)

**Framework**: Uniform Type Identifiers  
**Kind**: init

Creates a type based on a MIME type.

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
convenience init?(mimeType: String)
```

#### Discussion

This initializer returns `nil` if the system doesn’t know the MIME type.

## Parameters

- `mimeType`: A string that represents the MIME type.

## See Also

- [convenience init?(String)](uttypereference/init(_:).md)
  Creates a type based on an identifier.
- [convenience init?(mimeType: String, conformingTo: UTType)](uttypereference/init(mimetype:conformingto:).md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [convenience init?(filenameExtension: String)](uttypereference/init(filenameextension:).md)
  Creates a type that represents the specified filename extension.
- [convenience init?(filenameExtension: String, conformingTo: UTType)](uttypereference/init(filenameextension:conformingto:).md)
  Creates a type that represents the specified filename extension and conforms to an existing type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(mimetype:))*