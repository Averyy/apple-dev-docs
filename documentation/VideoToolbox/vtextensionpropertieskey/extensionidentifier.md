# extensionIdentifier

**Framework**: Videotoolbox  
**Kind**: property

A dictionary key for the video decoder extension identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let extensionIdentifier: VTExtensionPropertiesKey
```

#### Discussion

This key points to a `CFStringRef` value with the extension identifier, corresponding to the ClassImplementationID value from the EXAppExtensionAttributes dictionary in the Info.plist file.

## See Also

- [static let containingBundleName: VTExtensionPropertiesKey](vtextensionpropertieskey/containingbundlename.md)
  A dictionary key for the extension host application localized name.
- [static let containingBundleURL: VTExtensionPropertiesKey](vtextensionpropertieskey/containingbundleurl.md)
  A dictionary key for the URL of the extension host application.
- [static let extensionName: VTExtensionPropertiesKey](vtextensionpropertieskey/extensionname.md)
  A dictionary key for the localized extension name.
- [static let extensionURL: VTExtensionPropertiesKey](vtextensionpropertieskey/extensionurl.md)
  A dictionary key for the URL of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey/extensionidentifier)*