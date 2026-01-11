# kVTCompressionPropertyKey_SpatialAdaptiveQPLevel

**Framework**: Video Toolbox  
**Kind**: var

A value that controls spatial adaptation of the quantization parameter (QP) based on per-frame statistics.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let kVTCompressionPropertyKey_SpatialAdaptiveQPLevel: CFString
```

#### Discussion

If set to [`kVTQPModulationLevel_Disable`](kvtqpmodulationlevel_disable.md), spatial QP adaptation is not applied based on per-frame statistics. If set to [`kVTQPModulationLevel_Default`](kvtqpmodulationlevel_default.md), video encoder is allowed to apply spatial QP adaptation for each macro block (or coding unit) within a video frame. QP adaptation is based on spatial characteristics of a frame and the level of spatial QP adaptation is decided internally by the rate controller.

## Topics

### Levels
- [var kVTQPModulationLevel_Default: Int](kvtqpmodulationlevel_default.md)
- [var kVTQPModulationLevel_Disable: Int](kvtqpmodulationlevel_disable.md)

## See Also

- [let kVTCompressionPropertyKey_MaxAllowedFrameQP: CFString](kvtcompressionpropertykey_maxallowedframeqp.md)
  The maximum allowed encoded frame QP (Quantization Parameter).
- [let kVTCompressionPropertyKey_MinAllowedFrameQP: CFString](kvtcompressionpropertykey_minallowedframeqp.md)
  The minimum allowed encoded frame QP (Quantization Parameter).
- [let kVTCompressionPropertyKey_SupportsBaseFrameQP: CFString](kvtcompressionpropertykey_supportsbaseframeqp.md)
  A value that indicates whether the encoder supports base frame QP requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_spatialadaptiveqplevel)*