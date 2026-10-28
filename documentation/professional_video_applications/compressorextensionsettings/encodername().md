# encoderName()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the encoder extension name to display in the Compressor app interface.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func encoderName() -> String!
```

```objc
- (NSString *) encoderName;
```

## Return Value

A string containing the encoder extension name.

## See Also

### Getting Extension Settings and Details
- [func settingsString() -> String!](./settingsstring%28%29.md)
  Returns the current encoder settings string.
- [func settingsAttributes() -> [AnyHashable : Any]!](./settingsattributes%28%29.md)
  Returns a set of audio and video encoding attributes to display on the Compressor app interface.
- [func settingsDescription() -> String!](./settingsdescription%28%29.md)
  Returns a description of the current encoder settings to display in the Compressor app interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettings/encodername())*