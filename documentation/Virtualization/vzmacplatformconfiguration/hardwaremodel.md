# hardwareModel

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The Mac hardware model.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@NSCopying
var hardwareModel: VZMacHardwareModel { get set }
```

```objc
@property (copy) VZMacHardwareModel * hardwareModel;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

## Discussion

When creating a VM, the [`hardwareModel`](./hardwaremodel.md) depends on the restore image that you use to install macOS.

To choose the hardware model, start from `VZMacOSRestoreImage`.[`mostFeaturefulSupportedConfiguration`](../vzmacosrestoreimage/mostfeaturefulsupportedconfiguration.md) to get a supported configuration, then use its `VZMacOSConfigurationRequirements`.[`hardwareModel`](../vzmacosconfigurationrequirements/hardwaremodel.md) property to get the hardware model.

## See Also

### Getting platform properties
- [var auxiliaryStorage: VZMacAuxiliaryStorage?](./auxiliarystorage.md)
  The Mac auxiliary storage.
- [var machineIdentifier: VZMacMachineIdentifier](./machineidentifier.md)
  The Mac machine identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacplatformconfiguration/hardwaremodel)*