# maximumAllowedSharedMemoryRegionCount

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The maximum number of Virtio shared memory regions the framework allows.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class var maximumAllowedSharedMemoryRegionCount: Int { get }
```

```objc
@property (class, readonly) NSUInteger maximumAllowedSharedMemoryRegionCount;
```

## See Also

### Related Documentation
- [var sharedMemoryRegions: [VZVirtioSharedMemoryRegionConfiguration]](./sharedmemoryregions.md)
  The list of shared memory regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration/maximumallowedsharedmemoryregioncount)*