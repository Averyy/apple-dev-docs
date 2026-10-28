# init(mimeType:)

**Framework**: Uniform Type Identifiers  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) typeWithMIMEType:(NSString *) mimeType;
```

## Discussion

This initializer returns `nil` if the system doesn’t know the MIME type.

## Parameters

- `mimeType`: A string that represents the MIME type.

## See Also

### Creating a type
- [convenience init?(String)](./init%28_%29.md)
  Creates a type based on an identifier.
- [convenience init?(mimeType: String, conformingTo: UTType)](./init%28mimetype,conformingto%29.md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [convenience init?(filenameExtension: String)](./init%28filenameextension%29.md)
  Creates a type that represents the specified filename extension.
- [convenience init?(filenameExtension: String, conformingTo: UTType)](./init%28filenameextension,conformingto%29.md)
  Creates a type that represents the specified filename extension and conforms to an existing type.
- [convenience init?(tag: String, tagClass: String, conformingToType: UTType?)](./init%28tag,tagclass,conformingtotype%29.md)
  Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [init(exportedAs: String)](./init%28exportedas%29.md)
  Creates a type your app owns based on an identifier.
- [init(exportedAs: String, conformingTo: UTType)](./init%28exportedas,conformingto%29.md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String)](./init%28importedas%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier.
- [init(importedAs: String, conformingTo: UTType)](./init%28importedas,conformingto%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(mimetype:)-1txq0)*