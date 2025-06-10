# kVTCompressionPreset_HighSpeed

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
let kVTCompressionPreset_HighSpeed: CFString
```

#### Discussion

```None
A preset to provide a high-speed encoding.
```

An encoder configured using this preset is expected to achieve a faster encoding at a lower compression quality than an encoder configured with the preset kVTCompressionPreset_HighQuality or kVTCompressionPreset_Balanced. The presets kVTCompressionPreset_HighQuality and kVTCompressionPreset_Balanced may be preferred for a higher compression quality.

```None
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_Balanced, kVTCompressionPreset_VideoConferencing.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_highspeed)*