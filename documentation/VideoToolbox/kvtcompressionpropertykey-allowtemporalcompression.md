# kVTCompressionPropertyKey_AllowTemporalCompression

**Framework**: Video Toolbox  
**Kind**: var

A Boolean value indicating whether temporal compression is enabled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_AllowTemporalCompression: CFString
```

#### Discussion

The default value is `true`.  Set this `value` to false to require key-frame-only compression.

## See Also

- [let kVTCompressionPropertyKey_AllowFrameReordering: CFString](kvtcompressionpropertykey_allowframereordering.md)
  A Boolean value that indicates whether frame reordering is enabled.
- [let kVTCompressionPropertyKey_AllowOpenGOP: CFString](kvtcompressionpropertykey_allowopengop.md)
  Enables Open GOP (Group Of Pictures) encoding.
- [let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString](kvtcompressionpropertykey_maxkeyframeinterval.md)
  The maximum interval between key frames, also known as the key frame rate.
- [let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString](kvtcompressionpropertykey_maxkeyframeintervalduration.md)
  The maximum duration from one key frame to the next in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_allowtemporalcompression)*