# UTTypeReference

**Framework**: Uniform Type Identifiers  
**Kind**: class

An object that represents a type of data to load, send, or receive.

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
class UTTypeReference
```

#### Overview

The [`UTTypeReference`](uttypereference.md) object may represent files on disk, abstract data types with no on-disk representation, or entirely unrelated hierarchical classification systems, such as hardware. Each instance has a unique [`identifier`](uttype-swift.struct/identifier.md), and helpful properties, [`preferredFilenameExtension`](uttype-swift.struct/preferredfilenameextension.md) and [`preferredMIMEType`](uttype-swift.struct/preferredmimetype.md).

> **Note**:  The system includes static declarations for many common types, which you can look up by identifier, filename extension, or MIME type.

The [`UTTypeReference`](uttypereference.md) object may provide additional information related to the type. For example, it may include a localized user-facing description, a reference URL to technical documentation about the type, or its version number. You can look up types by their conformance to get either a type or a list of types that are relevant to your use case.

To define your own types in your app’s `Info.plist`, see [`Defining file and data types for your app`](defining-file-and-data-types-for-your-app.md).

## Topics

### Looking up a type
- [class func types(tag: String, tagClass: String, conformingTo: UTType?) -> [UTType]](uttypereference/types(tag:tagclass:conformingto:).md)
  Returns an array of types from the provided tag and tag class.
### Creating a type
- [convenience init?(String)](uttypereference/init(_:).md)
  Creates a type based on an identifier.
- [convenience init?(mimeType: String)](uttypereference/init(mimetype:).md)
  Creates a type based on a MIME type.
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
### Identifying a type
- [var identifier: String](uttype-swift.struct/identifier.md)
  The string that represents the type.
### Obtaining tags
- [var preferredFilenameExtension: String?](uttype-swift.struct/preferredfilenameextension.md)
  The preferred filename extension for the type.
- [var preferredMIMEType: String?](uttype-swift.struct/preferredmimetype.md)
  The preferred MIME type for the type.
- [var tags: [UTTagClass : [String]]](uttype-swift.struct/tags.md)
  The tag specification dictionary of the type.
### Obtaining additional type information
- [var isDeclared: Bool](uttypereference/isdeclared.md)
  A Boolean value that indicates whether the system declares the type.
- [var isDynamic: Bool](uttypereference/isdynamic.md)
  A Boolean value that indicates whether the system generates the type.
- [var isPublic: Bool](uttypereference/ispublic.md)
  A Boolean value that indicates whether the type is in the public domain.
- [var referenceURL: URL?](uttype-swift.struct/referenceurl.md)
  The reference URL for the type.
- [var version: Int?](uttype-swift.struct/version.md)
  The type’s version, if available.
### Checking a type’s relationship to another type
- [var supertypes: Set<UTType>](uttype-swift.struct/supertypes.md)
  The set of types the type directly or indirectly conforms to.
- [func conforms(to: UTType) -> Bool](uttypereference/conforms(to:).md)
  Returns a Boolean value that indicates whether a type conforms to the type.
- [func isSubtype(of: UTType) -> Bool](uttypereference/issubtype(of:).md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [func isSupertype(of: UTType) -> Bool](uttypereference/issupertype(of:).md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
### Describing a type
- [var localizedDescription: String?](uttype-swift.struct/localizeddescription.md)
  A localized description of the type.
### Type Properties
- [static var shazamCustomCatalog: UTType](uttype-swift.struct/shazamcustomcatalog.md)
  A type that represents a custom catalog.
- [static var shazamSignature: UTType](uttype-swift.struct/shazamsignature.md)
  A type that represents a signature.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct UTType](uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [struct UTTagClass](uttagclass.md)
  A type that represents tag classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference)*