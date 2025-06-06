# auxiliaryStorage

**Framework**: Virtualization  
**Kind**: property

The Mac auxiliary storage.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var auxiliaryStorage: VZMacAuxiliaryStorage? { get set }
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Discussion

When creating a VM, the hardware model of the `auxiliaryStorage` must match the hardware model of the `hardwareModel` property. Defaults to `nil`, but you must set a value for a configuration to be valid.

## See Also

- [var hardwareModel: VZMacHardwareModel](vzmacplatformconfiguration/hardwaremodel.md)
  The Mac hardware model.
- [var machineIdentifier: VZMacMachineIdentifier](vzmacplatformconfiguration/machineidentifier.md)
  The Mac machine identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacplatformconfiguration/auxiliarystorage)*