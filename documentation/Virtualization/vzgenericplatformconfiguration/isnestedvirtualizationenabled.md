# isNestedVirtualizationEnabled

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether nested virtualization is in an enabled state.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var isNestedVirtualizationEnabled: Bool { get set }
```

```objc
@property (readwrite, getter=isNestedVirtualizationEnabled) BOOL nestedVirtualizationEnabled;
```

## See Also

### Identifying the platform configuration
- [var machineIdentifier: VZGenericMachineIdentifier](./machineidentifier.md)
  A value that represents a unique identifier for the virtual machine.
- [class var isNestedVirtualizationSupported: Bool](./isnestedvirtualizationsupported.md)
  A Boolean value that describes whether the platform configuration supports nested virtualization.
- [class VZGenericMachineIdentifier](../vzgenericmachineidentifier.md)
  An object that represents a unique identifier for a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericplatformconfiguration/isnestedvirtualizationenabled)*