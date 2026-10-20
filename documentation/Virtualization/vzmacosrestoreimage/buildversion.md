# buildVersion

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The build version this restore image contains.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var buildVersion: String { get }
```

```objc
@property (copy, readonly) NSString * buildVersion;
```

## See Also

### Getting Information About the Restore Image
- [var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements?](./mostfeaturefulsupportedconfiguration.md)
  This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.
- [var operatingSystemVersion: OperatingSystemVersion](./operatingsystemversion.md)
  The operating system version this restore image contains.
- [var url: URL](./url.md)
  The URL of this restore image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/buildversion)*