# CompressorExtensionSettingsPtr

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

The type alias for referencing the `CompressorExtensionSettings`  object.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
typealias CompressorExtensionSettingsPtr = any NSObjectProtocol & CompressorExtensionSettings
```

```c
typedef NSObject<CompressorExtensionSettings> * CompressorExtensionSettingsPtr;
```

## See Also

### Configuring Extension Settings
- [func setSettingsString(String!)](./compressorextensionsettings/setsettingsstring%28_%29.md)
  Sets the encoder settings based on the string value supplied.
- [var audioEnabled: Bool](./compressorextensionsettings/audioenabled.md)
  A Boolean value that indicates whether audio is enabled for the source media.
- [var videoEnabled: Bool](./compressorextensionsettings/videoenabled.md)
  A Boolean value that indicates whether video is enabled for the source media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettingsptr)*