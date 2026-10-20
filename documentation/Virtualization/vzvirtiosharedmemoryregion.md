# VZVirtioSharedMemoryRegion

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZVirtioSharedMemoryRegion
```

```objc
@interface VZVirtioSharedMemoryRegion : NSObject
```

#### Overview

Don’t instantiate a `VZVirtioSharedMemoryRegion` directly.

Virtio shared memory regions are first configured on the [`VZCustomVirtioDeviceConfiguration`](./vzcustomvirtiodeviceconfiguration.md) through [`VZVirtioSharedMemoryRegionConfiguration`](./vzvirtiosharedmemoryregionconfiguration.md). When you create a [`VZCustomVirtioDevice`](./vzcustomvirtiodevice.md), the shared memory region is available through the [`sharedMemoryRegions`](./vzcustomvirtiodevice/sharedmemoryregions.md) property.

Use this class to manage the shared memory region during virtual machine runtime to map and unmap host memory into and from the shared memory region.

## Topics

### Instance Properties
- [var regionID: UInt8](./vzvirtiosharedmemoryregion/regionid.md)
  The shared memory region ID.
- [var size: UInt64](./vzvirtiosharedmemoryregion/size.md)
  The size of the shared memory region.
### Instance Methods
- [func mapMemory(UnsafeMutableRawPointer, atOffset: UInt64, size: UInt64, completionHandler: ((any Error)?) -> Void)](./vzvirtiosharedmemoryregion/mapmemory%28_,atoffset,size,completionhandler%29.md)
  Maps a chunk of host memory into the shared memory region.
- [func unmapMemory(atOffset: UInt64, size: UInt64, completionHandler: ((any Error)?) -> Void)](./vzvirtiosharedmemoryregion/unmapmemory%28atoffset,size,completionhandler%29.md)
  Unmaps a chunk of host memory from the shared memory region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZVirtioSharedMemoryRegionConfiguration](./vzvirtiosharedmemoryregionconfiguration.md)
  The configuration of a Virtio shared memory region.
- [class VZCustomVirtioDevice](./vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
### Managing shared memory
- [class VZVirtioSharedMemoryRegionConfiguration](./vzvirtiosharedmemoryregionconfiguration.md)
  The configuration of a Virtio shared memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosharedmemoryregion)*