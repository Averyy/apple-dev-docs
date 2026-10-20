# VZGenericMachineIdentifier

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that represents a unique identifier for a virtual machine.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZGenericMachineIdentifier
```

```objc
@interface VZGenericMachineIdentifier : NSObject
```

#### Overview

Use the data representation in [`dataRepresentation`](./vzgenericmachineidentifier/datarepresentation.md) to save the VM’s identifier. To restore a previously saved identifier use [`init(dataRepresentation:)`](./vzgenericmachineidentifier/init%28datarepresentation%29.md).

## Topics

### Creating a Machine Identifier
- [init()](./vzgenericmachineidentifier/init%28%29.md)
  Creates a new unique identifier for a VM.
- [init?(dataRepresentation: Data)](./vzgenericmachineidentifier/init%28datarepresentation%29.md)
  Creates a new unique identifier for a VM with the provided data.
### Getting Information About the Machine Identifier
- [var dataRepresentation: Data](./vzgenericmachineidentifier/datarepresentation.md)
  An opaque data representation of the VM’s identifier.

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

### Identifying the platform configuration
- [var machineIdentifier: VZGenericMachineIdentifier](./vzgenericplatformconfiguration/machineidentifier.md)
  A value that represents a unique identifier for the virtual machine.
- [var isNestedVirtualizationEnabled: Bool](./vzgenericplatformconfiguration/isnestedvirtualizationenabled.md)
  A Boolean value that indicates whether nested virtualization is in an enabled state.
- [class var isNestedVirtualizationSupported: Bool](./vzgenericplatformconfiguration/isnestedvirtualizationsupported.md)
  A Boolean value that describes whether the platform configuration supports nested virtualization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericmachineidentifier)*