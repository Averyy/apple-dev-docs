# memoryBalloonDevices

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

An array that you configure with a memory balloon device, used to update the memory in the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var memoryBalloonDevices: [VZMemoryBalloonDeviceConfiguration] { get set }
```

```objc
@property (copy, readwrite) NSArray<VZMemoryBalloonDeviceConfiguration *> * memoryBalloonDevices;
```

#### Discussion

Use this property to request a memory balloon device from the VM. The VM initially reserves the amount of memory in the [`memorySize`](./memorysize.md) property for the guest operating system. A balloon memory device asks the guest system to return memory pages that it isn’t using to the VM. You might use the device to reclaim memory when the amount of free memory on the host system runs low.

The default value of this property is an empty array, which doesn’t result in the creation of a balloon memory device. To create a balloon memory device, add a single [`VZVirtioTraditionalMemoryBalloonDeviceConfiguration`](../vzvirtiotraditionalmemoryballoondeviceconfiguration.md) object to the array. In response, the VM creates a [`VZVirtioTraditionalMemoryBalloonDevice`](../vzvirtiotraditionalmemoryballoondevice.md) object and adds it to its [`memoryBalloonDevices`](../vzvirtualmachine/memoryballoondevices.md) property. Use that object to change the amount of memory reserved for the guest system.

## See Also

### Sizing the memory partition
- [var memorySize: UInt64](./memorysize.md)
  The amount of physical memory the guest operating system recognizes.
- [class var minimumAllowedMemorySize: UInt64](./minimumallowedmemorysize.md)
  The minimum amount of memory that you may configure for the VM.
- [class var maximumAllowedMemorySize: UInt64](./maximumallowedmemorysize.md)
  The maximum amount of memory that you may configure for the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration/memoryballoondevices)*