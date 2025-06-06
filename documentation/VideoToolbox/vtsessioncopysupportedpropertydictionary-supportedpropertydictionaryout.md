# VTSessionCopySupportedPropertyDictionary(_:supportedPropertyDictionaryOut:)

**Framework**: Videotoolbox  
**Kind**: func

Retrieves a dictionary enumerating all the supported properties of a video toolbox session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTSessionCopySupportedPropertyDictionary(_ session: VTSession, supportedPropertyDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus
```

#### Discussion

The keys of the returned dictionary are the supported property keys.

The values are themselves dictionaries, each containing the following optional fields:

- The type of value ([`kVTPropertyTypeKey`](kvtpropertytypekey.md))
- The read/write status of the property ([`kVTPropertyReadWriteStatusKey`](kvtpropertyreadwritestatuskey.md))
- Whether the property is suitable for serialization ([`kVTPropertyShouldBeSerializedKey`](kvtpropertyshouldbeserializedkey.md))
- A range or list of the supported values, if appropriate
- Developer-level documentation for the property ([`kVTPropertyDocumentationKey`](kvtpropertydocumentationkey.md))

The caller must release the returned dictionary.

## Parameters

- `session`: The session object.
- `supportedPropertyDictionaryOut`: A pointer to a  doc://com.apple.documentation/documentation/corefoundation/cfdictionary-rum .

## See Also

- [func VTSessionCopyProperty(VTSession, key: CFString, allocator: CFAllocator?, valueOut: UnsafeMutableRawPointer?) -> OSStatus](vtsessioncopyproperty(_:key:allocator:valueout:).md)
  Retrieves a property on a Video Toolbox session.
- [func VTSessionCopySerializableProperties(VTSession, allocator: CFAllocator?, dictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](vtsessioncopyserializableproperties(_:allocator:dictionaryout:).md)
  Retrieves the set of serializable property keys and their current values.
- [Supported Property Dictionary Constants](supported-dictionary-constants.md)
  Property dictionary key and constant values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsessioncopysupportedpropertydictionary(_:supportedpropertydictionaryout:))*