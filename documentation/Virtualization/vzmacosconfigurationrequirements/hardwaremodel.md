# hardwareModel

**Framework**: Virtualization  
**Kind**: property

The hardware model for this configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@NSCopying
var hardwareModel: VZMacHardwareModel { get }
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Discussion

Use a hardware model to configure a new VM that meets a set of specific requirements.

After creating the hardware model, use `VZMacPlatformConfiguration` [`hardwareModel`](vzmacplatformconfiguration/hardwaremodel.md) to configure the Mac platform, and [`init(creatingStorageAt:hardwareModel:options:)`](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md) to create its auxiliary storage.

## See Also

- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZMacAuxiliaryStorage](vzmacauxiliarystorage.md)
  An object that contains information the boot loader needs for booting macOS as a guest operating system.
- [var minimumSupportedCPUCount: Int](vzmacosconfigurationrequirements/minimumsupportedcpucount.md)
  The minimum supported number of CPUs for this configuration.
- [var minimumSupportedMemorySize: UInt64](vzmacosconfigurationrequirements/minimumsupportedmemorysize.md)
  The minimum supported memory size for this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosconfigurationrequirements/hardwaremodel)*