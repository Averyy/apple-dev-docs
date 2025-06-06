# minimumSupportedCPUCount

**Framework**: Virtualization  
**Kind**: property

The minimum supported number of CPUs for this configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var minimumSupportedCPUCount: Int { get }
```

#### Discussion

This property specifies the minimum number of CPUs required by the associated macOS configuration.

You associate a [`VZMacOSConfigurationRequirements`](vzmacosconfigurationrequirements.md) with a specific [`VZMacOSRestoreImage`](vzmacosrestoreimage.md) object, which results in a specific macOS configuration.

Installing or running the associated configuration of macOS on a virtual machine with fewer than the specified number of CPUs results in undefined behavior.

## See Also

- [var hardwareModel: VZMacHardwareModel](vzmacosconfigurationrequirements/hardwaremodel.md)
  The hardware model for this configuration.
- [var minimumSupportedMemorySize: UInt64](vzmacosconfigurationrequirements/minimumsupportedmemorysize.md)
  The minimum supported memory size for this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosconfigurationrequirements/minimumsupportedcpucount)*