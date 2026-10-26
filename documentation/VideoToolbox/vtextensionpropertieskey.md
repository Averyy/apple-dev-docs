# VTExtensionPropertiesKey

**Framework**: Video Toolbox  
**Kind**: struct  
**Role**: Structure

A key in a Media Extension extension properties dictionary.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct VTExtensionPropertiesKey
```

```c
typedef CFStringRef VTExtensionPropertiesKey;
```

## Topics

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
- [kVTExtensionProperties_CodecNameKey](./kvtextensionproperties_codecnamekey.md)
  A dictionary key for the user readable name string of the codec.
### Initializers
- [init(rawValue: CFString)](./vtextensionpropertieskey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media Extension
- [VTCopyVideoDecoderExtensionProperties](./vtcopyvideodecoderextensionproperties.md)
  Returns information about the Media Extension video decoder required to decode the specified format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey)*