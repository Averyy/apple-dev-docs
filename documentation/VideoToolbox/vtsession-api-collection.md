# VTSession

**Framework**: Video Toolbox

An abstract object that provides the common interface to configure VideoToolbox session objects.

## Topics

### Setting Properties
- [func VTSessionSetProperty(VTSession, key: CFString, value: CFTypeRef?) -> OSStatus](vtsessionsetproperty(_:key:value:).md)
  Sets a property on a VideoToolbox session.
- [func VTSessionSetProperties(VTSession, propertyDictionary: CFDictionary) -> OSStatus](vtsessionsetproperties(_:propertydictionary:).md)
  Sets multiple properties at once.
### Getting Properties
- [func VTSessionCopyProperty(VTSession, key: CFString, allocator: CFAllocator?, valueOut: UnsafeMutableRawPointer?) -> OSStatus](vtsessioncopyproperty(_:key:allocator:valueout:).md)
  Retrieves a property on a Video Toolbox session.
- [func VTSessionCopySerializableProperties(VTSession, allocator: CFAllocator?, dictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](vtsessioncopyserializableproperties(_:allocator:dictionaryout:).md)
  Retrieves the set of serializable property keys and their current values.
- [func VTSessionCopySupportedPropertyDictionary(VTSession, supportedPropertyDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](vtsessioncopysupportedpropertydictionary(_:supportedpropertydictionaryout:).md)
  Retrieves a dictionary enumerating all the supported properties of a video toolbox session.
- [Supported Property Dictionary Constants](supported-dictionary-constants.md)
  Property dictionary key and constant values.
### Data Types
- [typealias VTSession](vtsession.md)
  A reference to a VideoToolbox compression session,  decompression session or pixel transfer session.
### Enumerations
- [Frame Delay](1441330-frame-delay.md)
  Indicates that no limit should be placed on the compression window.

## See Also

- [struct VTInt32Point](vtint32point.md)
  A structure that represents a 32-bit integer point value.
- [struct VTInt32Size](vtint32size.md)
  A structure that represents a 32-bit integer size value.
- [var VT_SUPPORT_COLORSYNC_PIXEL_TRANSFER: Bool](vt_support_colorsync_pixel_transfer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsession-api-collection)*