# kVTCompressionPreset_Balanced

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kVTCompressionPreset_Balanced;
```

#### Discussion

A preset to provide a balanced compression quality and encoding speed.

An encoder configured using this preset is expected to achieve a higher quality than an encoder configured with the preset kVTCompressionPreset_HighSpeed. The preset kVTCompressionPreset_HighSpeed may be preferred for a faster encoding. The preset kVTCompressionPreset_HighQuality may be preferred for a higher compression quality.

```
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_HighSpeed, kVTCompressionPreset_VideoConferencing, kVTCompressionPreset_ConsistentQuality.
```

## See Also

### Compression Presets
- [let kVTCompressionPreset_HighQuality: CFString](./kvtcompressionpreset_highquality.md)
- [let kVTCompressionPreset_HighSpeed: CFString](./kvtcompressionpreset_highspeed.md)
- [let kVTCompressionPreset_VideoConferencing: CFString](./kvtcompressionpreset_videoconferencing.md)
- [let kVTCompressionPropertyKey_SupportedPresetDictionaries: CFString](./kvtcompressionpropertykey_supportedpresetdictionaries.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_balanced)*