# operatingSystemVersion

**Framework**: Virtualization  
**Kind**: property

The operating system version this restore image contains.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var operatingSystemVersion: OperatingSystemVersion { get }
```

## See Also

- [var buildVersion: String](vzmacosrestoreimage/buildversion.md)
  The build version this restore image contains.
- [var isSupported: Bool](vzmacosrestoreimage/issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements?](vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md)
  This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.
- [var url: URL](vzmacosrestoreimage/url.md)
  The URL of this restore image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/operatingsystemversion)*