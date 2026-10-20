# containingBundleURL

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

A dictionary key for the URL of the extension host application.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let containingBundleURL: VTExtensionPropertiesKey
```

```c
extern VTExtensionPropertiesKey const kVTExtensionProperties_ContainingBundleURLKey;
```

#### Discussion

This key points to a `CFURLRef` value with the URL of the extension host application.

## See Also

### Keys
- [static let containingBundleName: VTExtensionPropertiesKey](./containingbundlename.md)
  A dictionary key for the extension host application localized name.
- [static let extensionIdentifier: VTExtensionPropertiesKey](./extensionidentifier.md)
  A dictionary key for the video decoder extension identifier.
- [static let extensionName: VTExtensionPropertiesKey](./extensionname.md)
  A dictionary key for the localized extension name.
- [static let extensionURL: VTExtensionPropertiesKey](./extensionurl.md)
  A dictionary key for the URL of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey/containingbundleurl)*