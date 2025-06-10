# iovmUnmapMemory

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn iovmUnmapMemory(IOMemoryDescriptor *memory, IODMACommand *dmaCommand, uint64_t mapAddress, uint64_t mapLength);
```

## See Also

- [- mapToPhysicalAddress](iomapper/1532966-maptophysicaladdress.md)
- [- iovmMapMemory](iomapper/1532977-iovmmapmemory.md)
- [- iovmInsert](iomapper/1532983-iovminsert.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper/1532968-iovmunmapmemory)*