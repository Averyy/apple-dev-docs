# kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration

**Framework**: Video Toolbox  
**Kind**: var

The maximum duration from one key frame to the next in seconds.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString
```

#### Discussion

The default value is `0`, which means no limit.  This property is particularly useful when the frame rate is variable. See [`kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration`](kvtcompressionpropertykey_maxkeyframeintervalduration.md) for more discussion of key frames.

This key can be set in conjunction with [`kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration`](kvtcompressionpropertykey_maxkeyframeintervalduration.md), which requires a keyframe every `X` frames or every `Y` seconds, whichever comes first.

## See Also

- [let kVTCompressionPropertyKey_AllowFrameReordering: CFString](kvtcompressionpropertykey_allowframereordering.md)
  A Boolean value that indicates whether frame reordering is enabled.
- [let kVTCompressionPropertyKey_AllowOpenGOP: CFString](kvtcompressionpropertykey_allowopengop.md)
  Enables Open GOP (Group Of Pictures) encoding.
- [let kVTCompressionPropertyKey_AllowTemporalCompression: CFString](kvtcompressionpropertykey_allowtemporalcompression.md)
  A Boolean value indicating whether temporal compression is enabled.
- [let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString](kvtcompressionpropertykey_maxkeyframeinterval.md)
  The maximum interval between key frames, also known as the key frame rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxkeyframeintervalduration)*