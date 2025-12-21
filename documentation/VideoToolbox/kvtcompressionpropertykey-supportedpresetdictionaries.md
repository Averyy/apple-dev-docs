# kVTCompressionPropertyKey_SupportedPresetDictionaries

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
let kVTCompressionPropertyKey_SupportedPresetDictionaries: CFString
```

#### Discussion

Where supported by video encoders, returns a dictionary whose keys are the available compression presets (prefixed by `kVTCompressionPreset_`) and the values are dictionaries containing the corresponding settings property key/value pairs.

Clients can select a compression preset for their encoding needs and use its encoder settings to configure the encoder. Clients may also use the encoder settings as a base configuration that they can customize as they require.

```None
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_Balanced, kVTCompressionPreset_HighSpeed, kVTCompressionPreset_VideoConferencing.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_supportedpresetdictionaries)*