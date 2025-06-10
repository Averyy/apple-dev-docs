# kVTCompressionPropertyKey_SupportedPresetDictionaries

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
let kVTCompressionPropertyKey_SupportedPresetDictionaries: CFString
```

#### Discussion

```None
Where supported by video encoders, returns a dictionary whose keys are the available compression presets (prefixed by `kVTCompressionPreset_`) and the values are dictionaries containing the corresponding settings property key/value pairs.
```

Clients can select a compression preset for their encoding needs and use its encoder settings to configure the encoder. Clients may also use the encoder settings as a base configuration that they can customize as they require.

```None
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_Balanced, kVTCompressionPreset_HighSpeed, kVTCompressionPreset_VideoConferencing.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_supportedpresetdictionaries)*