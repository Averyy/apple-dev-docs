# isSupported

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the current host supports this restore image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var isSupported: Bool { get }
```

```objc
@property (readonly, getter=isSupported) BOOL supported;
```

## See Also

### Getting Information About the Restore Image
- [var buildVersion: String](./buildversion.md)
  The build version this restore image contains.
- [var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements?](./mostfeaturefulsupportedconfiguration.md)
  This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.
- [var operatingSystemVersion: OperatingSystemVersion](./operatingsystemversion.md)
  The operating system version this restore image contains.
- [var url: URL](./url.md)
  The URL of this restore image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/issupported)*