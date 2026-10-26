# settingsString()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the current encoder settings string.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func settingsString() -> String!
```

```objc
- (NSString *) settingsString;
```

#### Return Value

A UTF-8 XML escaped string with the current encoder settings.

#### Discussion

When the current encoder settings are updated, the Compressor app calls this method to receive and store the updated settings on its end to keep the settings persistent across extension sessions.

## See Also

### Getting Extension Settings and Details
- [func settingsAttributes() -> [AnyHashable : Any]!](./settingsattributes%28%29.md)
  Returns a set of audio and video encoding attributes to display on the Compressor app interface.
- [func settingsDescription() -> String!](./settingsdescription%28%29.md)
  Returns a description of the current encoder settings to display in the Compressor app interface.
- [func encoderName() -> String!](./encodername%28%29.md)
  Returns the encoder extension name to display in the Compressor app interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettings/settingsstring())*