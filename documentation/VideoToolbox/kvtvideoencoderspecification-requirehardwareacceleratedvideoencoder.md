# kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value indicating whether hardware-accelerated encoding is required.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 10.9+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString
```

#### Discussion

This key is set in the `encoderSpecification` passed in to [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:).md).  Set it to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) to require hardware-accelerated encoding.  If hardware acceleration is not possible, the [`VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)`](vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:).md) call fails. Setting this key automatically implies that [`kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder`](kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder.md) is enabled; there is no need to set both.

This key is useful for clients that have their own software encoding implementation or those that may need to configure software and hardware encode sessions differently. Hardware acceleration may be unavailable for a number of reasons:

- The machine does not have hardware acceleration capabilities.
- The requested encoding format or encoding configuration is not supported.
- The hardware encoding resources on the machine are busy.

## See Also

- [let kVTCompressionPropertyKey_SupportsBaseFrameQP: CFString](kvtcompressionpropertykey_supportsbaseframeqp.md)
  A value that indicates whether the encoder supports base frame QP requests.
- [let kVTCompressionPropertyKey_UsingGPURegistryID: CFString](kvtcompressionpropertykey_usinggpuregistryid.md)
- [let kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder: CFString](kvtcompressionpropertykey_usinghardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether a hardware-accelerated video encoder is used.
- [let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated video encoding is allowed, if available.
- [let kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_preferredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_requiredencodergpuregistryid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder)*