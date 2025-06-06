# VTSessionSetProperties(_:propertyDictionary:)

**Framework**: Videotoolbox  
**Kind**: func

Sets multiple properties at once.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTSessionSetProperties(_ session: VTSession, propertyDictionary: CFDictionary) -> OSStatus
```

#### Discussion

Sets the properties specified by keys in `propertyDictionary` to the corresponding values.

## Topics

### Related Documentation
- [Compression Properties](compression-properties.md)
  Properties that you use to configure a compression session.
- [Decompression Properties](decompression-properties.md)
  Properties used to configure a VideoToolbox decompression session.
- [Pixel Transfer Properties](pixel-transfer-properties.md)
  Properties used to configure a VideoToolbox pixel transfer session.

## See Also

- [func VTSessionSetProperty(VTSession, key: CFString, value: CFTypeRef?) -> OSStatus](vtsessionsetproperty(_:key:value:).md)
  Sets a property on a VideoToolbox session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtsessionsetproperties(_:propertydictionary:))*