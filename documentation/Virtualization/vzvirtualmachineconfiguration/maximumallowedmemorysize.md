# maximumAllowedMemorySize

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The maximum amount of memory that you may configure for the VM.

**Availability**:
- macOS

## Declaration

```swift
class var maximumAllowedMemorySize: UInt64 { get }
```

```objc
@property (class, readonly) uint64_t maximumAllowedMemorySize;
```

## Discussion

The value in the [`memorySize`](./memorysize.md) property must be less than or equal to the value in this property.

## See Also

### Sizing the memory partition
- [var memorySize: UInt64](./memorysize.md)
  The amount of physical memory the guest operating system recognizes.
- [class var minimumAllowedMemorySize: UInt64](./minimumallowedmemorysize.md)
  The minimum amount of memory that you may configure for the VM.
- [var memoryBalloonDevices: [VZMemoryBalloonDeviceConfiguration]](./memoryballoondevices.md)
  An array that you configure with a memory balloon device, used to update the memory in the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/maximumallowedmemorysize)*