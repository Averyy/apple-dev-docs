# kVTVideoEncoderSpecification_EnableLowLatencyRateControl

**Framework**: Video Toolbox  
**Kind**: var

Specifies to select an encoder that supports low-latency operation and enables low-latency mode.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
let kVTVideoEncoderSpecification_EnableLowLatencyRateControl: CFString
```

#### Discussion

Low latency rate control enforces the following behaviors:

- Infinite GOP (all P frames following the beginning IDR).
- No frame reordering (B frame) or looking ahead.
- Only High profiles. The encoder sets the levels automatically.
- Temporal Layer structure.

## See Also

- [let kVTCompressionPropertyKey_EncoderID: CFString](kvtcompressionpropertykey_encoderid.md)
  Specifies a particular video encoder by its ID string.
- [let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated video encoding is allowed, if available.
- [let kVTVideoEncoderSpecification_EncoderID: CFString](kvtvideoencoderspecification_encoderid.md)
  A key that indicates a particular video encoder to use.
- [let kVTVideoEncoderSpecification_PreferredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_preferredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequiredEncoderGPURegistryID: CFString](kvtvideoencoderspecification_requiredencodergpuregistryid.md)
- [let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString](kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder.md)
  A Boolean value indicating whether hardware-accelerated encoding is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_enablelowlatencyratecontrol)*