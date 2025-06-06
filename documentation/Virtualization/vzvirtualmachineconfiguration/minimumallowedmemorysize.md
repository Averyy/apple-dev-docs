# minimumAllowedMemorySize

**Framework**: Virtualization  
**Kind**: property

The minimum amount of memory that you may configure for the VM.

**Availability**:
- macOS ?+

## Declaration

```swift
class var minimumAllowedMemorySize: UInt64 { get }
```

#### Discussion

The value in the [`memorySize`](vzvirtualmachineconfiguration/memorysize.md) property must be greater than or equal to the value in this property.

## See Also

- [var memorySize: UInt64](vzvirtualmachineconfiguration/memorysize.md)
  The amount of physical memory the guest operating system recognizes.
- [class var maximumAllowedMemorySize: UInt64](vzvirtualmachineconfiguration/maximumallowedmemorysize.md)
  The maximum amount of memory that you may configure for the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDeviceConfiguration]](vzvirtualmachineconfiguration/memoryballoondevices.md)
  An array that you configure with a memory balloon device, used to update the memory in the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/minimumallowedmemorysize)*