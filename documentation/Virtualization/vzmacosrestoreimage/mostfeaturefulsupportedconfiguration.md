# mostFeaturefulSupportedConfiguration

**Framework**: Virtualization  
**Kind**: property

This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@NSCopying
var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements? { get }
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

## See Also

- [var buildVersion: String](vzmacosrestoreimage/buildversion.md)
  The build version this restore image contains.
- [var isSupported: Bool](vzmacosrestoreimage/issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var operatingSystemVersion: OperatingSystemVersion](vzmacosrestoreimage/operatingsystemversion.md)
  The operating system version this restore image contains.
- [var url: URL](vzmacosrestoreimage/url.md)
  The URL of this restore image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/mostfeaturefulsupportedconfiguration)*