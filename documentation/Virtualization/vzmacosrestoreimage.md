# VZMacOSRestoreImage

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that describes a version of macOS to install on to a virtual machine.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacOSRestoreImage
```

```objc
@interface VZMacOSRestoreImage : NSObject
```

## Mentions

- [Installing macOS on a Virtual Machine](./installing-macos-on-a-virtual-machine.md)
- [Using iCloud with macOS virtual machines](./using-icloud-with-macos-virtual-machines.md)

#### Overview

To set up a new VM compatible with the restore image, use [`mostFeaturefulSupportedConfiguration`](./vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md) to obtain the [`hardwareModel`](./vzmacplatformconfiguration/hardwaremodel.md) of the [`VZMacPlatformConfiguration`](./vzmacplatformconfiguration.md). Then, create a [`VZMacOSRestoreImage`](./vzmacosrestoreimage.md) object by loading an installation media file. Initialize a [`VZMacOSInstaller`](./vzmacosinstaller.md) object with this `VZMacOSRestoreImage` object to install the operating system onto a VM.

> ❗ **Important**:  Loading a restore image requires the app to have the [`com.apple.security.virtualization`](../BundleResources/entitlements/com.apple.security.virtualization.md) entitlement.

## Topics

### Getting Information About the Restore Image
- [var buildVersion: String](./vzmacosrestoreimage/buildversion.md)
  The build version this restore image contains.
- [var isSupported: Bool](./vzmacosrestoreimage/issupported.md)
  A Boolean value that indicates whether the current host supports this restore image.
- [var mostFeaturefulSupportedConfiguration: VZMacOSConfigurationRequirements?](./vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md)
  This object represents the most fully featured configuration that’s supported by both the current host and by this restore image.
- [var operatingSystemVersion: OperatingSystemVersion](./vzmacosrestoreimage/operatingsystemversion.md)
  The operating system version this restore image contains.
- [var url: URL](./vzmacosrestoreimage/url.md)
  The URL of this restore image.
### Controlling the Restoration Process
- [class func fetchLatestSupported(completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](./vzmacosrestoreimage/fetchlatestsupported%28completionhandler%29.md)
  Fetches the latest restore image supported by this host from the network.
- [class func load(from: URL, completionHandler: (Result<VZMacOSRestoreImage, any Error>) -> Void)](./vzmacosrestoreimage/load%28from,completionhandler%29.md)
  Load a restore image from a file on the local file system.
- [class var latestSupported: VZMacOSRestoreImage](./vzmacosrestoreimage/latestsupported.md)
  Fetches the latest restore image supported by this host from the network.
- [class func image(from: URL) async throws -> VZMacOSRestoreImage](./vzmacosrestoreimage/image%28from%29.md)
  Load a restore image from a file on the local file system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZMacHardwareModel](./vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
### Installers
- [class VZMacOSInstaller](./vzmacosinstaller.md)
  An object you use to install macOS on the specified virtual machine.
- [class VZMacOSConfigurationRequirements](./vzmacosconfigurationrequirements.md)
  An object that describes the parameter constraints required by a specific configuration of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosrestoreimage)*