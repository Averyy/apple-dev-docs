# kVTExtensionProperties_CodecNameKey

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

A dictionary key for the user readable name string of the codec.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern VTExtensionPropertiesKey const kVTExtensionProperties_CodecNameKey;
```

#### Discussion

This key points to a `CFStringRef` with the name of the codec from the supplied format description. This name will be the one listed in the extension CodecInfo array with the key CodecName.

## See Also

### Keys
- [static let containingBundleName: VTExtensionPropertiesKey](./vtextensionpropertieskey/containingbundlename.md)
  A dictionary key for the extension host application localized name.
- [static let containingBundleURL: VTExtensionPropertiesKey](./vtextensionpropertieskey/containingbundleurl.md)
  A dictionary key for the URL of the extension host application.
- [static let extensionIdentifier: VTExtensionPropertiesKey](./vtextensionpropertieskey/extensionidentifier.md)
  A dictionary key for the video decoder extension identifier.
- [static let extensionName: VTExtensionPropertiesKey](./vtextensionpropertieskey/extensionname.md)
  A dictionary key for the localized extension name.
- [static let extensionURL: VTExtensionPropertiesKey](./vtextensionpropertieskey/extensionurl.md)
  A dictionary key for the URL of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtextensionproperties_codecnamekey)*