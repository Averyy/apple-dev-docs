# VZMacOSVirtualMachineStartOptions

**Framework**: Virtualization  
**Kind**: class

A class that describes start options for macOS VMs.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZMacOSVirtualMachineStartOptions
```

## Topics

### Setting recovery mode
- [var startUpFromMacOSRecovery: Bool](vzmacosvirtualmachinestartoptions/startupfrommacosrecovery.md)
  A Boolean value that indicates whether the macOS guest should start in recovery mode.

## Relationships

### Inherits From
- [VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.
- [class VZMacHardwareModel](vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
- [class VZMacMachineIdentifier](vzmacmachineidentifier.md)
  A unique identifier for a VM.
- [class VZMacAuxiliaryStorage](vzmacauxiliarystorage.md)
  An object that contains information the boot loader needs for booting macOS as a guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosvirtualmachinestartoptions)*