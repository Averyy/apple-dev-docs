# containingBundleName

**Framework**: Video Toolbox  
**Kind**: property  
**Role**: Type Property

A dictionary key for the extension host application localized name.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let containingBundleName: VTExtensionPropertiesKey
```

```c
extern VTExtensionPropertiesKey const kVTExtensionProperties_ContainingBundleNameKey;
```

#### Discussion

This key points to a `CFStringRef` value with the localized name of the application hosting the extension.

## See Also

### Keys
- [static let containingBundleURL: VTExtensionPropertiesKey](./containingbundleurl.md)
  A dictionary key for the URL of the extension host application.
- [static let extensionIdentifier: VTExtensionPropertiesKey](./extensionidentifier.md)
  A dictionary key for the video decoder extension identifier.
- [static let extensionName: VTExtensionPropertiesKey](./extensionname.md)
  A dictionary key for the localized extension name.
- [static let extensionURL: VTExtensionPropertiesKey](./extensionurl.md)
  A dictionary key for the URL of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey/containingbundlename)*