# kVTCompressionPropertyKey_MaxKeyFrameInterval

**Framework**: Videotoolbox  
**Kind**: var

The maximum interval between key frames, also known as the key frame rate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString
```

#### Discussion

Key frames, also known as sync frames, reset inter-frame dependencies; decoding a key frame is sufficient to prepare a decoder for correctly decoding the difference frames that follow. Video encoders are allowed to generate key frames more frequently if doing so results in more efficient compression. The default key frame interval is 0, which indicates that the video encoder should choose where to place all key frames. A key frame interval of 1 indicates that every frame must be a keyframe, 2 indicates that at least every other frame must be a keyframe, and so on.

This key can be set in conjunction with [`kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration`](kvtcompressionpropertykey_maxkeyframeintervalduration.md), which requires a keyframe every  frames or every  seconds, whichever comes first.

## See Also

- [let kVTCompressionPropertyKey_AllowFrameReordering: CFString](kvtcompressionpropertykey_allowframereordering.md)
  A Boolean value that indicates whether frame reordering is enabled.
- [let kVTCompressionPropertyKey_AllowOpenGOP: CFString](kvtcompressionpropertykey_allowopengop.md)
  Enables Open GOP (Group Of Pictures) encoding.
- [let kVTCompressionPropertyKey_AllowTemporalCompression: CFString](kvtcompressionpropertykey_allowtemporalcompression.md)
  A Boolean value indicating whether temporal compression is enabled.
- [let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString](kvtcompressionpropertykey_maxkeyframeintervalduration.md)
  The maximum duration from one key frame to the next in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxkeyframeinterval)*