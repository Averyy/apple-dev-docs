# setSettingsString(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the encoder settings based on the string value supplied.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func setSettingsString(_ settings: String!)
```

```objc
- (void) setSettingsString:(NSString *) settings;
```

## Parameters

- `settings`: Updated values for encoder settings in UTF_8 XML format. If the string value is `NULL`, set it to the default values.

## See Also

### Configuring Extension Settings
- [var audioEnabled: Bool](./audioenabled.md)
  A Boolean value that indicates whether audio is enabled for the source media.
- [var videoEnabled: Bool](./videoenabled.md)
  A Boolean value that indicates whether video is enabled for the source media.
- [typealias CompressorExtensionSettingsPtr](../compressorextensionsettingsptr.md)
  The type alias for referencing the `CompressorExtensionSettings`  object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettings/setsettingsstring(_:))*