# extensionName

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

A dictionary key for the localized extension name.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let extensionName: VTExtensionPropertiesKey
```

```c
extern VTExtensionPropertiesKey const kVTExtensionProperties_ExtensionNameKey;
```

## Discussion

This key points to a `CFStringRef` value with the localized extension name.

## See Also

### Keys
- [static let containingBundleName: VTExtensionPropertiesKey](./containingbundlename.md)
  A dictionary key for the extension host application localized name.
- [static let containingBundleURL: VTExtensionPropertiesKey](./containingbundleurl.md)
  A dictionary key for the URL of the extension host application.
- [static let extensionIdentifier: VTExtensionPropertiesKey](./extensionidentifier.md)
  A dictionary key for the video decoder extension identifier.
- [static let extensionURL: VTExtensionPropertiesKey](./extensionurl.md)
  A dictionary key for the URL of the extension.
- [kVTExtensionProperties_CodecNameKey](../kvtextensionproperties_codecnamekey.md)
  A dictionary key for the user readable name string of the codec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey/extensionname)*