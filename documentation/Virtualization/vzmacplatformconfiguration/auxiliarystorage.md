# auxiliaryStorage

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The Mac auxiliary storage.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var auxiliaryStorage: VZMacAuxiliaryStorage? { get set }
```

```objc
@property (strong, nullable) VZMacAuxiliaryStorage * auxiliaryStorage;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

#### Discussion

When creating a VM, the hardware model of the `auxiliaryStorage` must match the hardware model of the `hardwareModel` property. Defaults to `nil`, but you must set a value for a configuration to be valid.

## See Also

### Getting platform properties
- [var hardwareModel: VZMacHardwareModel](./hardwaremodel.md)
  The Mac hardware model.
- [var machineIdentifier: VZMacMachineIdentifier](./machineidentifier.md)
  The Mac machine identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacplatformconfiguration/auxiliarystorage)*