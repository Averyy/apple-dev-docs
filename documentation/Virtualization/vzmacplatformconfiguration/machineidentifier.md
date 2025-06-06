# machineIdentifier

**Framework**: Virtualization  
**Kind**: property

The Mac machine identifier.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@NSCopying
var machineIdentifier: VZMacMachineIdentifier { get set }
```

#### Discussion

This value uniquely identifies an instance of a VM. Running two VMs concurrently with the same identifier results in undefined behavior in the guest operating system.

## See Also

- [var auxiliaryStorage: VZMacAuxiliaryStorage?](vzmacplatformconfiguration/auxiliarystorage.md)
  The Mac auxiliary storage.
- [var hardwareModel: VZMacHardwareModel](vzmacplatformconfiguration/hardwaremodel.md)
  The Mac hardware model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacplatformconfiguration/machineidentifier)*