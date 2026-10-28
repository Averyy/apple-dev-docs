# settingsAttributes()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a set of audio and video encoding attributes to display on the Compressor app interface.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func settingsAttributes() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) settingsAttributes;
```

## Return Value

A dictionary containing values for the keys defined in Encoder Attribute Keys.

## Discussion

The Compressor app calls this method to get the encoder setting attributes to render on its interface and for configuring the decoder object.

## See Also

### Getting Extension Settings and Details
- [func settingsString() -> String!](./settingsstring%28%29.md)
  Returns the current encoder settings string.
- [func settingsDescription() -> String!](./settingsdescription%28%29.md)
  Returns a description of the current encoder settings to display in the Compressor app interface.
- [func encoderName() -> String!](./encodername%28%29.md)
  Returns the encoder extension name to display in the Compressor app interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionsettings/settingsattributes())*