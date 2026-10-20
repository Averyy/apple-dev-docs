# iovmUnmapMemory

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn iovmUnmapMemory(IOMemoryDescriptor *memory, IODMACommand *dmaCommand, uint64_t mapAddress, uint64_t mapLength);
```

## See Also

### Mapping Memory Addresses
- [- mapToPhysicalAddress](./api-1532966-maptophysicaladdress.md)
- [- iovmMapMemory](./api-1532977-iovmmapmemory.md)
- [- iovmInsert](./api-1532983-iovminsert.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper/1532968-iovmunmapmemory)*