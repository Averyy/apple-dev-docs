# kVTCompressionPreset_HighQuality

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let kVTCompressionPreset_HighQuality: CFString
```

#### Discussion

```None
A preset to achieve a high compression quality.
```

An encoder configured using this preset is expected to achieve a higher quality with a slower encoding than an encoder configured with the preset kVTCompressionPreset_Balanced or kVTCompressionPreset_HighSpeed. The presets kVTCompressionPreset_Balanced and kVTCompressionPreset_HighSpeed may be preferred for a faster encoding.

```None
See also kVTCompressionPreset_Balanced, kVTCompressionPreset_HighSpeed, kVTCompressionPreset_VideoConferencing.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_highquality)*