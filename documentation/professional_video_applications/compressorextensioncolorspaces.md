# CompressorExtensionColorSpaces

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An interface you use to specify the supported color spaces in an extension.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
protocol CompressorExtensionColorSpaces
```

```objc
@protocol CompressorExtensionColorSpaces
```

## Topics

### Supporting Color Spaces
- [func supportedColorSpaces() -> [NSNumber]!](./compressorextensioncolorspaces/supportedcolorspaces%28%29.md)
  Returns the supported color spaces in an extension.
- [struct eCEColorSpace](./ececolorspace.md)
  The list of color spaces an encoder extension can support.

## See Also

### Encoder Extension Settings
- [CompressorExtensionSettings](./compressorextensionsettings.md)
  A set of methods you use to manage the extension UI that displays the current encoder settings for users to view and customize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensioncolorspaces)*