# VTSessionCopySerializableProperties(_:allocator:dictionaryOut:)

**Framework**: Video Toolbox  
**Kind**: func

Retrieves the set of serializable property keys and their current values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTSessionCopySerializableProperties(_ session: VTSession, allocator: CFAllocator?, dictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus
```

#### Discussion

The serializable properties are those which can be saved and applied to a different session. The caller must release the returned dictionary.

## Parameters

- `session`: The session object.
- `allocator`: An allocator suitable for use when copying property values.
- `dictionaryOut`: A pointer to the properties dictionary.

## See Also

- [func VTSessionCopyProperty(VTSession, key: CFString, allocator: CFAllocator?, valueOut: UnsafeMutableRawPointer?) -> OSStatus](vtsessioncopyproperty(_:key:allocator:valueout:).md)
  Retrieves a property on a Video Toolbox session.
- [func VTSessionCopySupportedPropertyDictionary(VTSession, supportedPropertyDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](vtsessioncopysupportedpropertydictionary(_:supportedpropertydictionaryout:).md)
  Retrieves a dictionary enumerating all the supported properties of a video toolbox session.
- [Supported Property Dictionary Constants](supported-dictionary-constants.md)
  Property dictionary key and constant values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsessioncopyserializableproperties(_:allocator:dictionaryout:))*