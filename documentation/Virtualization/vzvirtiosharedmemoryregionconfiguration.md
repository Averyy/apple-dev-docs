# VZVirtioSharedMemoryRegionConfiguration

**Framework**: Virtualization  
**Kind**: class

The configuration of a Virtio shared memory region.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZVirtioSharedMemoryRegionConfiguration
```

#### Overview

A `VZVirtioSharedMemoryRegionConfiguration` represents a memory region that’s continuously shared between the custom Virtio device implementation and the guest. A shared memory region is identified by an ID, whose meaning is specific to the device.

After configuration,  the framework advertises the shared memory region to the guest. During runtime, you can use the [`mapMemory(_:atOffset:size:completionHandler:)`](vzvirtiosharedmemoryregion/mapmemory(_:atoffset:size:completionhandler:).md) and [`unmapMemory(atOffset:size:completionHandler:)`](vzvirtiosharedmemoryregion/unmapmemory(atoffset:size:completionhandler:).md) APIs to map and unmap host memory into the shared memory region. How a device uses a shared memory region is specific to the device.

## Topics

### Initializers
- [init(regionID: UInt8, size: UInt64)](vzvirtiosharedmemoryregionconfiguration/init(regionid:size:).md)
  Initializes a shared memory region with a shared memory region ID and size.
### Instance Properties
- [var regionID: UInt8](vzvirtiosharedmemoryregionconfiguration/regionid.md)
  The shared memory region ID.
- [var size: UInt64](vzvirtiosharedmemoryregionconfiguration/size.md)
  The size of the shared memory region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZCustomVirtioDeviceConfiguration](vzcustomvirtiodeviceconfiguration.md)
  An object that defines a custom Virtio Device configuration.
- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZVirtioSharedMemoryRegion](vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.
- [class VZVirtioSharedMemoryRegion](vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosharedmemoryregionconfiguration)*