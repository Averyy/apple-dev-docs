# machineIdentifier

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A value that represents a unique identifier for the virtual machine.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@NSCopying
var machineIdentifier: VZGenericMachineIdentifier { get set }
```

```objc
@property (copy) VZGenericMachineIdentifier * machineIdentifier;
```

## See Also

### Identifying the platform configuration
- [var isNestedVirtualizationEnabled: Bool](./isnestedvirtualizationenabled.md)
  A Boolean value that indicates whether nested virtualization is in an enabled state.
- [class var isNestedVirtualizationSupported: Bool](./isnestedvirtualizationsupported.md)
  A Boolean value that describes whether the platform configuration supports nested virtualization.
- [class VZGenericMachineIdentifier](../vzgenericmachineidentifier.md)
  An object that represents a unique identifier for a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericplatformconfiguration/machineidentifier)*