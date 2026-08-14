# kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value indicating whether hardware-accelerated video encoding is allowed, if available.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 10.9+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString
```

#### Discussion

This key is set in the `encoderSpecification` passed in to [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:).md).  Set it to [`kCFBooleanTrue`](https://developer.apple.com/documentation/corefoundation/kcfbooleantrue) to allow hardware-accelerated encoding.  To specifically prevent hardware encoding, set this property to [`kCFBooleanFalse`](https://developer.apple.com/documentation/corefoundation/kcfbooleanfalse).

This setting is useful for clients doing realtime encoding operations because it allows VideoToolbox to choose the optimal encoding path.

## See Also

- [let kVTCompressionPropertyKey_EncoderID: CFString](kvtcompressionpropertykey_encoderid.md)
  Specifies a particular video encoder by its ID string.
- [let kVTVideoEncoderSpecification_EnableLowLatencyRateControl: CFString](kvtvideoencoderspecification_enablelowlatencyratecontrol.md)
  Specifies to select an encoder that supports low-latency operation and enables low-latency mode.
- [let kVTVideoEncoderSpecification_EncoderID: CFString](kvtvideoencoderspecification_encoderid.md)
  A key that indicates a particular video encoder to use.
- [let kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_preferredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_requiredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated encoding is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder)*