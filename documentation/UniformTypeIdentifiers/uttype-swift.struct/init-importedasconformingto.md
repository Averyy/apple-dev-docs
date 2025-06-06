# init(importedAs:conformingTo:)

**Framework**: Uniform Type Identifiers  
**Kind**: init

Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.

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
init(importedAs identifier: String, conformingTo parentType: UTType? = nil)
```

#### Discussion

Define a type with this initializer when you’re supporting a type that another app owns. For example, the following code uses another app’s type information to open or save files in its app:

```swift
extension UTType {
    /// The type of a supported file format.
    public static var anotherFormat: UTType {
        UTType(importedAs: "com.example.anotherformat")
    }
}
```

## Parameters

- `identifier`: The identifier of your type.
- `parentType`: A type to extend with this type.

## See Also

- [init?(String)](uttype-swift.struct/init(_:).md)
  Creates a type based on an identifier.
- [init?(mimeType: String, conformingTo: UTType)](uttype-swift.struct/init(mimetype:conformingto:).md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [init?(filenameExtension: String, conformingTo: UTType)](uttype-swift.struct/init(filenameextension:conformingto:).md)
  Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init?(tag: String, tagClass: UTTagClass, conformingTo: UTType?)](uttype-swift.struct/init(tag:tagclass:conformingto:).md)
  Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(exportedas:conformingto:).md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(importedas:conformingto:))*