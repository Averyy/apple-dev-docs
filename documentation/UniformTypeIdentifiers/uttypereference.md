# UTTypeReference

**Framework**: Uniform Type Identifiers  
**Kind**: class  
**Role**: Class

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

```objc
@interface UTType : NSObject
```

#### Overview

The [`UTTypeReference`](./uttypereference.md) object may represent files on disk, abstract data types with no on-disk representation, or entirely unrelated hierarchical classification systems, such as hardware. Each instance has a unique [`identifier`](./uttype-swift.struct/identifier.md), and helpful properties, [`preferredFilenameExtension`](./uttype-swift.struct/preferredfilenameextension.md) and [`preferredMIMEType`](./uttype-swift.struct/preferredmimetype.md).

> **Note**:  The system includes static declarations for many common types, which you can look up by identifier, filename extension, or MIME type.

The [`UTTypeReference`](./uttypereference.md) object may provide additional information related to the type. For example, it may include a localized user-facing description, a reference URL to technical documentation about the type, or its version number. You can look up types by their conformance to get either a type or a list of types that are relevant to your use case.

To define your own types in your app’s `Info.plist`, see [Defining file and data types for your app](./defining-file-and-data-types-for-your-app.md).

## Topics

### Looking up a type
- [class func types(tag: String, tagClass: String, conformingTo: UTType?) -> [UTType]](./uttypereference/types%28tag,tagclass,conformingto%29.md)
  Returns an array of types from the provided tag and tag class.
### Creating a type
- [convenience init?(String)](./uttypereference/init%28_%29.md)
  Creates a type based on an identifier.
- [convenience init?(mimeType: String)](./uttypereference/init%28mimetype%29-1txq0.md)
  Creates a type based on a MIME type.
- [convenience init?(mimeType: String, conformingTo: UTType)](./uttypereference/init%28mimetype,conformingto%29.md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [convenience init?(filenameExtension: String)](./uttypereference/init%28filenameextension%29.md)
  Creates a type that represents the specified filename extension.
- [convenience init?(filenameExtension: String, conformingTo: UTType)](./uttypereference/init%28filenameextension,conformingto%29.md)
  Creates a type that represents the specified filename extension and conforms to an existing type.
- [convenience init?(tag: String, tagClass: String, conformingToType: UTType?)](./uttypereference/init%28tag,tagclass,conformingtotype%29.md)
  Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [init(exportedAs: String)](./uttypereference/init%28exportedas%29.md)
  Creates a type your app owns based on an identifier.
- [init(exportedAs: String, conformingTo: UTType)](./uttypereference/init%28exportedas,conformingto%29.md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String)](./uttypereference/init%28importedas%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier.
- [init(importedAs: String, conformingTo: UTType)](./uttypereference/init%28importedas,conformingto%29.md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
### Identifying a type
- [var identifier: String](./uttype-swift.struct/identifier.md)
  The string that represents the type.
- [identifier](./uttypereference/identifier.md)
  The string that represents the type.
### Obtaining tags
- [var preferredFilenameExtension: String?](./uttype-swift.struct/preferredfilenameextension.md)
  The preferred filename extension for the type.
- [var preferredMIMEType: String?](./uttype-swift.struct/preferredmimetype.md)
  The preferred MIME type for the type.
- [var tags: [UTTagClass : [String]]](./uttype-swift.struct/tags.md)
  The tag specification dictionary of the type.
- [preferredFilenameExtension](./uttypereference/preferredfilenameextension.md)
  The preferred filename extension for the type.
- [preferredMIMEType](./uttypereference/preferredmimetype.md)
  The preferred MIME type for the type.
- [tags](./uttypereference/tags.md)
  The tag specification dictionary of the type.
### Obtaining additional type information
- [var isDeclared: Bool](./uttypereference/isdeclared.md)
  A Boolean value that indicates whether the system declares the type.
- [var isDynamic: Bool](./uttypereference/isdynamic.md)
  A Boolean value that indicates whether the system generates the type.
- [var isPublic: Bool](./uttypereference/ispublic.md)
  A Boolean value that indicates whether the type is in the public domain.
- [var referenceURL: URL?](./uttype-swift.struct/referenceurl.md)
  The reference URL for the type.
- [var version: Int?](./uttype-swift.struct/version.md)
  The type’s version, if available.
- [referenceURL](./uttypereference/referenceurl.md)
  The reference URL for the type.
- [version](./uttypereference/version.md)
  The type’s version, if available.
### Checking a type’s relationship to another type
- [var supertypes: Set<UTType>](./uttype-swift.struct/supertypes.md)
  The set of types the type directly or indirectly conforms to.
- [func conforms(to: UTType) -> Bool](./uttypereference/conforms%28to%29.md)
  Returns a Boolean value that indicates whether a type conforms to the type.
- [func isSubtype(of: UTType) -> Bool](./uttypereference/issubtype%28of%29.md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [func isSupertype(of: UTType) -> Bool](./uttypereference/issupertype%28of%29.md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
- [supertypes](./uttypereference/supertypes.md)
  The set of types the type directly or indirectly conforms to.
### Describing a type
- [var localizedDescription: String?](./uttype-swift.struct/localizeddescription.md)
  A localized description of the type.
- [localizedDescription](./uttypereference/localizeddescription.md)
  A localized description of the type.
### Type Properties
- [static var shazamCustomCatalog: UTType](./uttype-swift.struct/shazamcustomcatalog.md)
  A type that represents a custom catalog.
- [static var shazamSignature: UTType](./uttype-swift.struct/shazamsignature.md)
  A type that represents a signature.
- [SHCustomCatalogContentType](./uttype-c.class/shcustomcatalogcontenttype.md)
  A type representing the @c SHCustomCatalog file format with the .shazamcatalog extension
- [SHSignatureContentType](./uttype-c.class/shsignaturecontenttype.md)
  A type representing the @c SHSignature file format with the .shazamsignature extension
### Initializers
- [convenience init?(MIMEType: String)](./uttypereference/init%28mimetype%29-7gu84.md)
- [convenience init?(MIMEType: String, conformingToType: UTType)](./uttypereference/init%28mimetype,conformingtotype%29.md)
- [init?(coder: NSCoder)](./uttypereference/init%28coder%29.md)
- [convenience init?(filenameExtension: String, conformingToType: UTType)](./uttypereference/init%28filenameextension,conformingtotype%29.md)
- [convenience init?(identifier: String)](./uttypereference/init%28identifier%29.md)
- [convenience init?(identifier: String, allowUndeclared: Bool)](./uttypereference/init%28identifier,allowundeclared%29.md)
- [convenience init?(tag: String, tagClass: String, conformingTo: UTType?)](./uttypereference/init%28tag,tagclass,conformingto%29.md)
### Default Implementations
- [UTTypeReference Implementations](./uttypereference/uttypereference-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Uniform type identifiers
- [struct UTType](./uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [struct UTTagClass](./uttagclass.md)
  A type that represents tag classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference)*