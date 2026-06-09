# sharedMemoryRegions

**Framework**: Virtualization  
**Kind**: property

An array of shared memory regions that this device exposes to the guest.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var sharedMemoryRegions: [VZVirtioSharedMemoryRegion] { get }
```

## See Also

- [class VZVirtioSharedMemoryRegion](vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/sharedmemoryregions)*