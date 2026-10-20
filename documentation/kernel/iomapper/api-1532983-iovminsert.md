# iovmInsert

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn iovmInsert(uint32_t options, uint64_t mapAddress, uint64_t offset, uint64_t physicalAddress, uint64_t length);
```

## See Also

### Mapping Memory Addresses
- [- mapToPhysicalAddress](./api-1532966-maptophysicaladdress.md)
- [- iovmMapMemory](./api-1532977-iovmmapmemory.md)
- [- iovmUnmapMemory](./api-1532968-iovmunmapmemory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper/1532983-iovminsert)*