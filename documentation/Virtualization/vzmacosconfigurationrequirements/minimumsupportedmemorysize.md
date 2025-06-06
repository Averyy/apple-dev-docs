# minimumSupportedMemorySize

**Framework**: Virtualization  
**Kind**: property

The minimum supported memory size for this configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var minimumSupportedMemorySize: UInt64 { get }
```

#### Discussion

This property specifies the minimum amount of memory required by the associated macOS configuration.

You associate a [`VZMacOSConfigurationRequirements`](vzmacosconfigurationrequirements.md) with a specific [`VZMacOSRestoreImage`](vzmacosrestoreimage.md) object, which results in a specific macOS configuration.

Installing or running the associated configuration of macOS on a VM with less than this amount of memory results in undefined behavior.

## See Also

- [var hardwareModel: VZMacHardwareModel](vzmacosconfigurationrequirements/hardwaremodel.md)
  The hardware model for this configuration.
- [var minimumSupportedCPUCount: Int](vzmacosconfigurationrequirements/minimumsupportedcpucount.md)
  The minimum supported number of CPUs for this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosconfigurationrequirements/minimumsupportedmemorysize)*