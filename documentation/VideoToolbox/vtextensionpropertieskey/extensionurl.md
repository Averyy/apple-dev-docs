# extensionURL

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

A dictionary key for the URL of the extension.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let extensionURL: VTExtensionPropertiesKey
```

```c
extern VTExtensionPropertiesKey const kVTExtensionProperties_ExtensionURLKey;
```

#### Discussion

This key points to a `CFURLRef` value with the URL for the extension.

## See Also

### Keys
- [static let containingBundleName: VTExtensionPropertiesKey](./containingbundlename.md)
  A dictionary key for the extension host application localized name.
- [static let containingBundleURL: VTExtensionPropertiesKey](./containingbundleurl.md)
  A dictionary key for the URL of the extension host application.
- [static let extensionIdentifier: VTExtensionPropertiesKey](./extensionidentifier.md)
  A dictionary key for the video decoder extension identifier.
- [static let extensionName: VTExtensionPropertiesKey](./extensionname.md)
  A dictionary key for the localized extension name.
- [kVTExtensionProperties_CodecNameKey](../kvtextensionproperties_codecnamekey.md)
  A dictionary key for the user readable name string of the codec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey/extensionurl)*