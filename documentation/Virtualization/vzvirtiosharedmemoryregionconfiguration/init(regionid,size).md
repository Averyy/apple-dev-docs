# init(regionID:size:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initializes a shared memory region with a shared memory region ID and size.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(regionID: UInt8, size: UInt64)
```

```objc
- (instancetype) initWithRegionID:(uint8_t) regionID size:(uint64_t) size;
```

#### Return Value

An initialized [`VZVirtioSharedMemoryRegionConfiguration`](../vzvirtiosharedmemoryregionconfiguration.md).

## Parameters

- `regionID`: Shared memory region ID.
- `size`: Shared memory region size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosharedmemoryregionconfiguration/init(regionid:size:))*