# audioEnabled

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether audio is enabled for the source media.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
var audioEnabled: Bool { get set }
```

```objc
@property BOOL audioEnabled;
```

## Discussion

The Compressor app sets this value based on the source media attributes. Use this value to specify the [`kCEAudioEnabledKey`](../kceaudioenabledkey.md).

## See Also

### Configuring Extension Settings
- [func setSettingsString(String!)](./setsettingsstring%28_%29.md)
  Sets the encoder settings based on the string value supplied.
- [var videoEnabled: Bool](./videoenabled.md)
  A Boolean value that indicates whether video is enabled for the source media.
- [typealias CompressorExtensionSettingsPtr](../compressorextensionsettingsptr.md)
  The type alias for referencing the `CompressorExtensionSettings`  object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettings/audioenabled)*