# Supported Property Dictionary Constants

**Framework**: Video Toolbox

Property dictionary key and constant values.

#### Overview

Property dictionary key and constant values for a dictionary populated by [`VTSessionCopySupportedPropertyDictionary(_:supportedPropertyDictionaryOut:)`](vtsessioncopysupportedpropertydictionary(_:supportedpropertydictionaryout:).md).

## Topics

### Properties
- [let kVTPropertyTypeKey: CFString](kvtpropertytypekey.md)
  Dictionary key used to access the property type.
- [Property Type Constants](property-type-constants.md)
  Supported constant values for `kVTPropertyTypeKey`.
- [let kVTPropertyReadWriteStatusKey: CFString](kvtpropertyreadwritestatuskey.md)
  Dictionary key to access the read/write status of a property.
- [Read/Write Status Constants](read-write-status-constants.md)
  Supported constant values for `kVTPropertyReadWriteStatusKey`.
- [let kVTPropertyShouldBeSerializedKey: CFString](kvtpropertyshouldbeserializedkey.md)
  Dictionary key to access the serializable status of a property.
- [let kVTPropertySupportedValueListKey: CFString](kvtpropertysupportedvaluelistkey.md)
  Dictionary key to access the array of of supported values.
- [let kVTPropertySupportedValueMaximumKey: CFString](kvtpropertysupportedvaluemaximumkey.md)
  Dictionary key to access the maximum value of a property.
- [let kVTPropertySupportedValueMinimumKey: CFString](kvtpropertysupportedvalueminimumkey.md)
  Dictionary key to access the minimum value of a property.
- [let kVTPropertyDocumentationKey: CFString](kvtpropertydocumentationkey.md)
  Dictionary key to access any documentation intended for developers only.

## See Also

- [func VTSessionCopyProperty(VTSession, key: CFString, allocator: CFAllocator?, valueOut: UnsafeMutableRawPointer?) -> OSStatus](vtsessioncopyproperty(_:key:allocator:valueout:).md)
  Retrieves a property on a Video Toolbox session.
- [func VTSessionCopySerializableProperties(VTSession, allocator: CFAllocator?, dictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](vtsessioncopyserializableproperties(_:allocator:dictionaryout:).md)
  Retrieves the set of serializable property keys and their current values.
- [func VTSessionCopySupportedPropertyDictionary(VTSession, supportedPropertyDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](vtsessioncopysupportedpropertydictionary(_:supportedpropertydictionaryout:).md)
  Retrieves a dictionary enumerating all the supported properties of a video toolbox session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/supported-dictionary-constants)*