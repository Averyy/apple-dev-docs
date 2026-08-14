# kVTVideoEncoderSpecification_EncoderID

**Framework**: Video Toolbox  
**Kind**: var

A key that indicates a particular video encoder to use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTVideoEncoderSpecification_EncoderID: CFString
```

#### Discussion

To specify a particular video encoder when creating a compression session, pass an encoder specification [`CFDictionary`](https://developer.apple.com/documentation/corefoundation/cfdictionary) containing this key and the encoder ID as its value. You can get the encoder ID string from the `kVTVideoEncoderList_EncoderID` entry in the array returned by [`VTCopyVideoEncoderList(_:_:)`](vtcopyvideoencoderlist(_:_:).md).

## See Also

- [let kVTCompressionPropertyKey_EncoderID: CFString](kvtcompressionpropertykey_encoderid.md)
  Specifies a particular video encoder by its ID string.
- [let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated video encoding is allowed, if available.
- [let kVTVideoEncoderSpecification_EnableLowLatencyRateControl: CFString](kvtvideoencoderspecification_enablelowlatencyratecontrol.md)
  Specifies to select an encoder that supports low-latency operation and enables low-latency mode.
- [let kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_preferredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_requiredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated encoding is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_encoderid)*