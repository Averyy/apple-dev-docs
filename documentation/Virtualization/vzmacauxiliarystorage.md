# VZMacAuxiliaryStorage

**Framework**: Virtualization  
**Kind**: class

An object that contains information the boot loader needs for booting macOS as a guest operating system.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacAuxiliaryStorage
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Overview

The Mac auxiliary storage contains data used by the boot loader and the guest operating system. It’s necessary to boot a macOS guest OS.

When creating a new VM, use [`init(creatingStorageAt:hardwareModel:options:)`](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md) to create a default initialized auxiliary storage.

The hardware model you use when creating the new auxiliary storage depends on the restore image that you’ll use for installation. From the restore image, use [`mostFeaturefulSupportedConfiguration`](vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md) to get a supported configuration. A configuration has a [`VZMacHardwareModel`](vzmachardwaremodel.md) associated with it.

After initializing the new auxiliary storage, set it on `VZMacPlatformConfiguration`.[`auxiliaryStorage`](vzmacplatformconfiguration/auxiliarystorage.md).

The hardware model in `VZMacPlatformConfiguration`.[`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md) must be identical to the one used to create the empty auxiliary storage., otherwise the behavior isn’t defined.

When installing macOS, the [`VZMacOSInstaller`](vzmacosinstaller.md) lays out data on the auxiliary storage. After installation, the macOS guest uses the auxiliary storage for every subsequent boot.

When moving or performing a backup of a VM, you must move or copy the file containing the auxiliary storage along with the main disk image.

To boot a VM created with `VZMacOSInstaller`, use [`init(contentsOfURL:)`](vzmacauxiliarystorage/init(contentsofurl:).md) to set up the auxiliary storage from the existing file used during installation.

When using an existing file, the hardware model of the `VZMacPlatformConfiguration`.[`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md) must match the hardware model used when creating the original file.

## Topics

### Creating the auxiliary storage
- [init(contentsOfURL: URL)](vzmacauxiliarystorage/init(contentsofurl:).md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(url: URL)](vzmacauxiliarystorage/init(url:).md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(creatingStorageAt: URL, hardwareModel: VZMacHardwareModel, options: VZMacAuxiliaryStorage.InitializationOptions) throws](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md)
  Creates an initialized Mac auxiliary storage instance that describes a specific hardware model at a URL you specify.
- [VZMacAuxiliaryStorage.InitializationOptions](vzmacauxiliarystorage/initializationoptions.md)
  Options you can set when creating new auxiliary storage.
### Configuring the auxiliary storage location
- [var url: URL](vzmacauxiliarystorage/url.md)
  The URL of the auxiliary storage on the local file system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacOSRestoreImage](vzmacosrestoreimage.md)
  An object that describes a version of macOS to install on to a virtual machine.
- [class VZMacOSConfigurationRequirements](vzmacosconfigurationrequirements.md)
  An object that describes the parameter constraints required by a specific configuration of macOS.
- [class VZMacOSInstaller](vzmacosinstaller.md)
  An object you use to install macOS on the specified virtual machine.
- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZMacOSVirtualMachineStartOptions](vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.
- [class VZMacHardwareModel](vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
- [class VZMacMachineIdentifier](vzmacmachineidentifier.md)
  A unique identifier for a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage)*