# VZMacHardwareModel

**Framework**: Virtualization  
**Kind**: class

A specification for the hardware elements and configurations present in a particular Mac hardware model.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacHardwareModel
```

## Mentions

- [Using iCloud with macOS virtual machines](using-icloud-with-macos-virtual-machines.md)
- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Overview

The Mac hardware model abstracts a set of virtualized hardware elements and configurations.

A version of macOS may only run on certain hardware models. Additionally, the host may also only provide certain hardware models based on the version of macOS and the underlying hardware.

The [`isSupported`](vzmachardwaremodel/issupported.md) property allows you to discover if the current host supports a particular hardware model.

Choosing the hardware model starts from a restore image with [`VZMacOSRestoreImage`](vzmacosrestoreimage.md). A restore image describes its supported configuration requirements through its [`mostFeaturefulSupportedConfiguration`](vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md) property.

A configuration requirements object has a corresponding hardware model that you can use to configure a VM that meets the requirements. After obtaining the hardware model, use the platform configuration’s [`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md) to configure the Mac platform object and use [`init(creatingStorageAt:hardwareModel:options:)`](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md) to create its auxiliary storage.

After creating the VM, use [`VZMacOSInstaller`](vzmacosinstaller.md) to install macOS on it.

If you serialize the VM on disk, preserve the hardware model used for installation for subsequent boots. The [`dataRepresentation`](vzmachardwaremodel/datarepresentation.md) property provides a unique binary representation that you serialize to the file system. You can recreate the hardware model from the serialized binary representation with [`init(dataRepresentation:)`](vzmachardwaremodel/init(datarepresentation:).md).

## Topics

### Creating the hardware model
- [init?(dataRepresentation: Data)](vzmachardwaremodel/init(datarepresentation:).md)
  Creates an instance of the hardware model described by the specified data representation.
### Configuring the hardware model
- [var dataRepresentation: Data](vzmachardwaremodel/datarepresentation.md)
  Returns the opaque data representation of the hardware model.
- [var isSupported: Bool](vzmachardwaremodel/issupported.md)
  A Boolean value that indicates whether the host supports this hardware model.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacOSInstaller](vzmacosinstaller.md)
  An object you use to install macOS on the specified virtual machine.
- [class VZMacOSRestoreImage](vzmacosrestoreimage.md)
  An object that describes a version of macOS to install on to a virtual machine.
- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZMacOSVirtualMachineStartOptions](vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.
- [class VZMacMachineIdentifier](vzmacmachineidentifier.md)
  A unique identifier for a VM.
- [class VZMacAuxiliaryStorage](vzmacauxiliarystorage.md)
  An object that contains information the boot loader needs for booting macOS as a guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmachardwaremodel)*