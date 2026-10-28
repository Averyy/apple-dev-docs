# url

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The URL of this restore image.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var url: URL { get }
```

```objc
@property (copy, readonly) NSURL * URL;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

## Discussion

If the restore image loaded using [`image(from:)`](./image%28from%29.md), the value of this property is a file URL.

If you obtain the restore image by fetching it from a server, use [`latestSupported`](./latestsupported.md) and set the value of this property to a network URL for the installation media file.

## See Also

### Getting Information About the Restore Image
- [var buildVersion: String](./buildversion.md)
  The build version this restore image contains.
- [var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements?](./mostfeaturefulsupportedconfiguration.md)
  This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.
- [var operatingSystemVersion: OperatingSystemVersion](./operatingsystemversion.md)
  The operating system version this restore image contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage/url)*