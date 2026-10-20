# VTSessionSetProperty(_:key:value:)

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Sets a property on a VideoToolbox session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTSessionSetProperty(_ session: VTSession, key propertyKey: CFString, value propertyValue: CFTypeRef?) -> OSStatus
```

```c
extern OSStatus VTSessionSetProperty(VTSessionRef session, CFStringRef propertyKey, CFTypeRef propertyValue);
```

#### Discussion

Setting a property value to `NULL` restores the default value.

## Topics

### Related Documentation
- [Compression Properties](./compression-properties.md)
  Properties that you use to configure a compression session.
- [Decompression Properties](./decompression-properties.md)
  Properties used to configure a VideoToolbox decompression session.
- [Pixel Transfer Properties](./pixel-transfer-properties.md)
  Properties used to configure a VideoToolbox pixel transfer session.

## See Also

### Setting Properties
- [func VTSessionSetProperties(VTSession, propertyDictionary: CFDictionary) -> OSStatus](./vtsessionsetproperties%28_,propertydictionary%29.md)
  Sets multiple properties at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsessionsetproperty(_:key:value:))*