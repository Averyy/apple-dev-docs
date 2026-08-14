# VZGenericMachineIdentifier

**Framework**: Virtualization  
**Kind**: class

An object that represents a unique identifier for a virtual machine.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZGenericMachineIdentifier
```

#### Overview

Use the data representation in [`dataRepresentation`](vzgenericmachineidentifier/datarepresentation.md) to save the VM’s identifier. To restore a previously saved identifier use [`init(dataRepresentation:)`](vzgenericmachineidentifier/init(datarepresentation:).md).

## Topics

### Creating a Machine Identifier
- [init()](vzgenericmachineidentifier/init.md)
  Creates a new unique identifier for a VM.
- [init?(dataRepresentation: Data)](vzgenericmachineidentifier/init(datarepresentation:).md)
  Creates a new unique identifier for a VM with the provided data.
### Getting Information About the Machine Identifier
- [var dataRepresentation: Data](vzgenericmachineidentifier/datarepresentation.md)
  An opaque data representation of the VM’s identifier.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var machineIdentifier: VZGenericMachineIdentifier](vzgenericplatformconfiguration/machineidentifier.md)
  A value that represents a unique identifier for the virtual machine.
- [var isNestedVirtualizationEnabled: Bool](vzgenericplatformconfiguration/isnestedvirtualizationenabled.md)
  A Boolean value that indicates whether nested virtualization is in an enabled state.
- [class var isNestedVirtualizationSupported: Bool](vzgenericplatformconfiguration/isnestedvirtualizationsupported.md)
  A Boolean value that describes whether the platform configuration supports nested virtualization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericmachineidentifier)*