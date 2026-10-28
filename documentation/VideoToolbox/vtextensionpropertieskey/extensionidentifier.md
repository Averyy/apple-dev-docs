# extensionIdentifier

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

A dictionary key for the video decoder extension identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let extensionIdentifier: VTExtensionPropertiesKey
```

```c
extern VTExtensionPropertiesKey const kVTExtensionProperties_ExtensionIdentifierKey;
```

## Discussion

This key points to a `CFStringRef` value with the extension identifier, corresponding to the ClassImplementationID value from the EXAppExtensionAttributes dictionary in the Info.plist file.

## See Also

### Keys
- [static let containingBundleName: VTExtensionPropertiesKey](./containingbundlename.md)
  A dictionary key for the extension host application localized name.
- [static let containingBundleURL: VTExtensionPropertiesKey](./containingbundleurl.md)
  A dictionary key for the URL of the extension host application.
- [static let extensionName: VTExtensionPropertiesKey](./extensionname.md)
  A dictionary key for the localized extension name.
- [static let extensionURL: VTExtensionPropertiesKey](./extensionurl.md)
  A dictionary key for the URL of the extension.
- [kVTExtensionProperties_CodecNameKey](../kvtextensionproperties_codecnamekey.md)
  A dictionary key for the user readable name string of the codec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey/extensionidentifier)*