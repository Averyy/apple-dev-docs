# setSettings(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the current encoding settings based on the given setting values.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func setSettings(_ settings: CompressorExtensionSettingsPtr!)
```

```objc
- (void) setSettings:(CompressorExtensionSettingsPtr) settings;
```

#### Discussion

During an encoding process, the Compressor app provides the extension with the current encoder settings. If the `settings` object contains an empty encoder setting string, use default values for the encoder settings.

## Parameters

- `settings`: A pointer to the [`CompressorExtensionSettings`](../compressorextensionsettings.md) object.

## See Also

### Setting Encoding Values
- [func setAnnotations([AnyHashable : Any]!)](./setannotations%28_%29.md)
  Adds annotations to an encoded media file.
- [func setChapters([[AnyHashable : Any]]!)](./setchapters%28_%29.md)
  Sets chapter markers of an encoded file from the contents of the input dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/setsettings(_:))*