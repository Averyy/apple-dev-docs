# VZMacPlatformConfiguration

**Framework**: Virtualization  
**Kind**: class

The platform configuration for booting macOS on Apple silicon.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacPlatformConfiguration
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Overview

When creating a VM, the [`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md) and [`auxiliaryStorage`](vzmacplatformconfiguration/auxiliarystorage.md) depend on the restore image that you use to install macOS.

To choose the hardware model, start from `VZMacOSRestoreImage`.[`mostFeaturefulSupportedConfiguration`](vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md) to get a supported configuration, then use its `VZMacOSConfigurationRequirements`.[`hardwareModel`](vzmacosconfigurationrequirements/hardwaremodel.md) property to get the hardware model.

Use the hardware model to set up `VZMacPlatformConfiguration` and to initialize a new auxiliary storage with [`init(creatingStorageAt:hardwareModel:options:)`](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md).

When you save a VM to disk and load it again, you must restore the [`hardwareModel`](vzmacosconfigurationrequirements/hardwaremodel.md), [`machineIdentifier`](vzmacplatformconfiguration/machineidentifier.md) and [`auxiliaryStorage`](vzmacplatformconfiguration/auxiliarystorage.md) properties to their original values.

If you create multiple VMs from the same configuration, each should have a unique `auxiliaryStorage` and `machineIdentifier`.

## Topics

### Creating a platform configuration
- [init()](vzmacplatformconfiguration/init.md)
  Creates a new Mac platform configuration.
### Getting platform properties
- [var auxiliaryStorage: VZMacAuxiliaryStorage?](vzmacplatformconfiguration/auxiliarystorage.md)
  The Mac auxiliary storage.
- [var hardwareModel: VZMacHardwareModel](vzmacplatformconfiguration/hardwaremodel.md)
  The Mac hardware model.
- [var machineIdentifier: VZMacMachineIdentifier](vzmacplatformconfiguration/machineidentifier.md)
  The Mac machine identifier.

## Relationships

### Inherits From
- [VZPlatformConfiguration](vzplatformconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZMacOSVirtualMachineStartOptions](vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.
- [class VZMacHardwareModel](vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
- [class VZMacMachineIdentifier](vzmacmachineidentifier.md)
  A unique identifier for a VM.
- [class VZMacAuxiliaryStorage](vzmacauxiliarystorage.md)
  An object that contains information the boot loader needs for booting macOS as a guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacplatformconfiguration)*