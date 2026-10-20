# sharedMemoryRegions

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The list of shared memory regions.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var sharedMemoryRegions: [VZVirtioSharedMemoryRegionConfiguration] { get set }
```

```objc
@property (copy, readwrite) NSArray<VZVirtioSharedMemoryRegionConfiguration *> * sharedMemoryRegions;
```

#### Discussion

The list is empty by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration/sharedmemoryregions)*