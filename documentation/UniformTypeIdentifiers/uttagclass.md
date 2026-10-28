# UTTagClass

**Framework**: Uniform Type Identifiers  
**Kind**: struct  
**Role**: Structure

A type that represents tag classes.

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
struct UTTagClass
```

## Overview

A tag class is a label that represents the mapping of a [`UTType`](./uttype-swift.struct.md) to another type system; for example, a MIME type or a file system extension.

A tag is a specific instance of a tag class. For example, the tag `txt` is an instance of the tag class [`UTTagClassFilenameExtension`](./uttagclassfilenameextension.md) and represents the type [`UTTypePlainText`](./uttypeplaintext.md).

[`UTTagClass`](./uttagclass.md) uses an untyped `String` or [`CFString`](../CoreFoundation/cfstring.md) to refer to a tag class as a string. To get the string representation of a tag class, use its `rawValue-swift.property` property.

## Topics

### Getting a declared types mapping
- [static var filenameExtension: UTTagClass](./uttagclass/filenameextension.md)
  A type property that returns the tag class used to map a type to a filename extension.
- [static var mimeType: UTTagClass](./uttagclass/mimetype.md)
  A type property that returns the tag class used to map a type to a MIME type.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Uniform type identifiers
- [struct UTType](./uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [class UTTypeReference](./uttypereference.md)
  An object that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass)*