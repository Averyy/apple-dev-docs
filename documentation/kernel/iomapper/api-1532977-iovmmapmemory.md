# iovmMapMemory

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn iovmMapMemory(IOMemoryDescriptor *memory, uint64_t descriptorOffset, uint64_t length, uint32_t mapOptions, const IODMAMapSpecification *mapSpecification, IODMACommand *dmaCommand, const IODMAMapPageList *pageList, uint64_t *mapAddress, uint64_t *mapLength);
```

## See Also

- [- mapToPhysicalAddress](iomapper/1532966-maptophysicaladdress.md)
- [- iovmUnmapMemory](iomapper/1532968-iovmunmapmemory.md)
- [- iovmInsert](iomapper/1532983-iovminsert.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper/1532977-iovmmapmemory)*