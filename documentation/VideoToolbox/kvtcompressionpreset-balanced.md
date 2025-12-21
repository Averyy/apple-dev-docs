# kVTCompressionPreset_Balanced

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
let kVTCompressionPreset_Balanced: CFString
```

#### Discussion

A preset to provide a balanced compression quality and encoding speed.

An encoder configured using this preset is expected to achieve a higher quality than an encoder configured with the preset kVTCompressionPreset_HighSpeed. The preset kVTCompressionPreset_HighSpeed may be preferred for a faster encoding. The preset kVTCompressionPreset_HighQuality may be preferred for a higher compression quality.

```None
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_HighSpeed, kVTCompressionPreset_VideoConferencing.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_balanced)*