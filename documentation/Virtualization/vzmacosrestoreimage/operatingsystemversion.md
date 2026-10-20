# operatingSystemVersion

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The operating system version this restore image contains.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var operatingSystemVersion: OperatingSystemVersion { get }
```

```objc
@property (readonly) NSOperatingSystemVersion operatingSystemVersion;
```

## See Also

### Getting Information About the Restore Image
- [var buildVersion: String](./buildversion.md)
  The build version this restore image contains.
- [var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements?](./mostfeaturefulsupportedconfiguration.md)
  This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.
- [var url: URL](./url.md)
  The URL of this restore image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/operatingsystemversion)*