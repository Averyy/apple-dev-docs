# isNestedVirtualizationSupported

**Framework**: Virtualization  
**Kind**: property

A Boolean value that describes whether the platform configuration supports nested virtualization.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class var isNestedVirtualizationSupported: Bool { get }
```

#### Discussion

> ❗ **Important**:  Nested virtualization is available for Mac with the M3 chip, and later.

 Nested virtualization is available for Mac with the M3 chip, and later.

Use this property to check whether support is available for the platform. As the following example shows, if the framework supports nested virtualization on the host, use [`isNestedVirtualizationEnabled`](vzgenericplatformconfiguration/isnestedvirtualizationenabled.md) to enable the feature:

## See Also

- [var machineIdentifier: VZGenericMachineIdentifier](vzgenericplatformconfiguration/machineidentifier.md)
  A value that represents a unique identifier for the virtual machine.
- [var isNestedVirtualizationEnabled: Bool](vzgenericplatformconfiguration/isnestedvirtualizationenabled.md)
  A Boolean value that indicates whether nested virtualization is in an enabled state.
- [class VZGenericMachineIdentifier](vzgenericmachineidentifier.md)
  An object that represents a unique identifier for a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericplatformconfiguration/isnestedvirtualizationsupported)*