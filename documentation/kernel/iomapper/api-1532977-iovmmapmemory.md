# iovmMapMemory

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn iovmMapMemory(IOMemoryDescriptor *memory, uint64_t descriptorOffset, uint64_t length, uint32_t mapOptions, const IODMAMapSpecification *mapSpecification, IODMACommand *dmaCommand, const IODMAMapPageList *pageList, uint64_t *mapAddress, uint64_t *mapLength);
```

## See Also

### Mapping Memory Addresses
- [- mapToPhysicalAddress](./api-1532966-maptophysicaladdress.md)
- [- iovmUnmapMemory](./api-1532968-iovmunmapmemory.md)
- [- iovmInsert](./api-1532983-iovminsert.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper/1532977-iovmmapmemory)*