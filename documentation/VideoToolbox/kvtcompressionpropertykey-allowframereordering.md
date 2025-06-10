# kVTCompressionPropertyKey_AllowFrameReordering

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value that indicates whether frame reordering is enabled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_AllowFrameReordering: CFString
```

#### Discussion

In order to encode B frames, a video encoder must reorder frames, which means that the order in which the frames are emitted and stored (the decode order) is different from the order in which they were presented to the video encoder (the display order).  The default value is `true`.  Set this value to `false` to prevent frame reordering.

## See Also

- [let kVTCompressionPropertyKey_AllowOpenGOP: CFString](kvtcompressionpropertykey_allowopengop.md)
  Enables Open GOP (Group Of Pictures) encoding.
- [let kVTCompressionPropertyKey_AllowTemporalCompression: CFString](kvtcompressionpropertykey_allowtemporalcompression.md)
  A Boolean value indicating whether temporal compression is enabled.
- [let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString](kvtcompressionpropertykey_maxkeyframeinterval.md)
  The maximum interval between key frames, also known as the key frame rate.
- [let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString](kvtcompressionpropertykey_maxkeyframeintervalduration.md)
  The maximum duration from one key frame to the next in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_allowframereordering)*