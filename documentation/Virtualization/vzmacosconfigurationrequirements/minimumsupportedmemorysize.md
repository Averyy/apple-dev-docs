# minimumSupportedMemorySize

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The minimum supported memory size for this configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var minimumSupportedMemorySize: UInt64 { get }
```

```objc
@property (readonly) uint64_t minimumSupportedMemorySize;
```

## Discussion

This property specifies the minimum amount of memory required by the associated macOS configuration.

You associate a [`VZMacOSConfigurationRequirements`](../vzmacosconfigurationrequirements.md) with a specific [`VZMacOSRestoreImage`](../vzmacosrestoreimage.md) object, which results in a specific macOS configuration.

Installing or running the associated configuration of macOS on a VM with less than this amount of memory results in undefined behavior.

## See Also

### Configuration Requirements
- [var hardwareModel: VZMacHardwareModel](./hardwaremodel.md)
  The hardware model for this configuration.
- [var minimumSupportedCPUCount: Int](./minimumsupportedcpucount.md)
  The minimum supported number of CPUs for this configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosconfigurationrequirements/minimumsupportedmemorysize)*