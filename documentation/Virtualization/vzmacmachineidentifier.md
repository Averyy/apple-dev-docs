# VZMacMachineIdentifier

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A unique identifier for a VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacMachineIdentifier
```

```objc
@interface VZMacMachineIdentifier : NSObject
```

#### Overview

This value uniquely identifies a virtual Mac hardware instance. Two VMs running concurrently shouldn’t use the same identifier.

When serializing the VM to disk, you can preserve the identifier in a binary representation by serializing the data in the `VZMacMachineIdentifier`.[`dataRepresentation`](./vzmachardwaremodel/datarepresentation.md) property. Conversely, you can recreate the identifier with [`init(dataRepresentation:)`](./vzmacmachineidentifier/init%28datarepresentation%29.md) from the binary representation.

You can compare the contents of two identifiers with [`isEqual(to:)`](../ObjectiveC/nsobject-swift.class/isequal%28to%29.md).

## Topics

### Creating a machine identifier
- [init?(dataRepresentation: Data)](./vzmacmachineidentifier/init%28datarepresentation%29.md)
  Create a machine identifier described by the specified data representation.
- [init()](./vzmacmachineidentifier/init%28%29.md)
  Creates a new unique machine identifier.
### Machine data representation
- [var dataRepresentation: Data](./vzmacmachineidentifier/datarepresentation.md)
  Returns the opaque data representation of the machine identifier.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Platform components
- [class VZVirtualMachineConfiguration](./vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZMacOSVirtualMachineStartOptions](./vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [class VZMacPlatformConfiguration](./vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZPlatformConfiguration](./vzplatformconfiguration.md)
  The base class for a platform configuration.
- [class VZMacHardwareModel](./vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
- [class VZMacAuxiliaryStorage](./vzmacauxiliarystorage.md)
  An object that contains information the boot loader needs for booting macOS as a guest operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacmachineidentifier)*