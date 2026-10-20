# mostFeaturefulSupportedConfiguration

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@NSCopying
var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements? { get }
```

```objc
@property (copy, readonly, nullable) VZMacOSConfigurationRequirements * mostFeaturefulSupportedConfiguration;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

## See Also

### Getting Information About the Restore Image
- [var buildVersion: String](./buildversion.md)
  The build version this restore image contains.
- [var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var operatingSystemVersion: OperatingSystemVersion](./operatingsystemversion.md)
  The operating system version this restore image contains.
- [var url: URL](./url.md)
  The URL of this restore image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/mostfeaturefulsupportedconfiguration)*