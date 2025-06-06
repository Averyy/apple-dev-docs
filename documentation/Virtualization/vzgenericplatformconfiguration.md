# VZGenericPlatformConfiguration

**Framework**: Virtualization  
**Kind**: class

The platform configuration for a generic Intel or ARM virtual machine.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZGenericPlatformConfiguration
```

## Topics

### Creating a platform configuration
- [init()](vzgenericplatformconfiguration/init.md)
  Returns a new generic platform configuration.
### Identifying the platform configuration
- [var machineIdentifier: VZGenericMachineIdentifier](vzgenericplatformconfiguration/machineidentifier.md)
  A value that represents a unique identifier for the virtual machine.
- [var isNestedVirtualizationEnabled: Bool](vzgenericplatformconfiguration/isnestedvirtualizationenabled.md)
  A Boolean value that indicates whether nested virtualization is in an enabled state.
- [class var isNestedVirtualizationSupported: Bool](vzgenericplatformconfiguration/isnestedvirtualizationsupported.md)
  A Boolean value that describes whether the platform configuration supports nested virtualization.
- [class VZGenericMachineIdentifier](vzgenericmachineidentifier.md)
  An object that represents a unique identifier for a virtual machine.

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
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.
- [class VZPlatformConfiguration](vzplatformconfiguration.md)
  The base class for a platform configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericplatformconfiguration)*