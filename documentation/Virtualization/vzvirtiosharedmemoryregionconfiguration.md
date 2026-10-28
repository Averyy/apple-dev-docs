# VZVirtioSharedMemoryRegionConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The configuration of a Virtio shared memory region.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZVirtioSharedMemoryRegionConfiguration
```

```objc
@interface VZVirtioSharedMemoryRegionConfiguration : NSObject
```

## Overview

A `VZVirtioSharedMemoryRegionConfiguration` represents a memory region that’s continuously shared between the custom Virtio device implementation and the guest. A shared memory region is identified by an ID, whose meaning is specific to the device.

After configuration,  the framework advertises the shared memory region to the guest. During runtime, you can use the [`mapMemory(_:atOffset:size:completionHandler:)`](./vzvirtiosharedmemoryregion/mapmemory%28_,atoffset,size,completionhandler%29.md) and [`unmapMemory(atOffset:size:completionHandler:)`](./vzvirtiosharedmemoryregion/unmapmemory%28atoffset,size,completionhandler%29.md) APIs to map and unmap host memory into the shared memory region. How a device uses a shared memory region is specific to the device.

## Topics

### Initializers
- [init(regionID: UInt8, size: UInt64)](./vzvirtiosharedmemoryregionconfiguration/init%28regionid,size%29.md)
  Initializes a shared memory region with a shared memory region ID and size.
### Instance Properties
- [var regionID: UInt8](./vzvirtiosharedmemoryregionconfiguration/regionid.md)
  The shared memory region ID.
- [var size: UInt64](./vzvirtiosharedmemoryregionconfiguration/size.md)
  The size of the shared memory region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZCustomVirtioDeviceConfiguration](./vzcustomvirtiodeviceconfiguration.md)
  An object that defines a custom Virtio Device configuration.
- [class VZCustomVirtioDevice](./vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZVirtioSharedMemoryRegion](./vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.
### Managing shared memory
- [class VZVirtioSharedMemoryRegion](./vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosharedmemoryregionconfiguration)*