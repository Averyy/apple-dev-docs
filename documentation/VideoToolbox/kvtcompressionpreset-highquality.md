# kVTCompressionPreset_HighQuality

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTCompressionPreset_HighQuality: CFString
```

#### Discussion

A preset to achieve a high compression quality.

An encoder configured using this preset is expected to achieve a higher quality with a slower encoding than an encoder configured with the preset kVTCompressionPreset_Balanced or kVTCompressionPreset_HighSpeed. The presets kVTCompressionPreset_Balanced and kVTCompressionPreset_HighSpeed may be preferred for a faster encoding.

```None
See also kVTCompressionPreset_Balanced, kVTCompressionPreset_HighSpeed, kVTCompressionPreset_VideoConferencing.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_highquality)*