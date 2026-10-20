# readCD

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15.2+

## Declaration

```cpp
virtual IOReturn readCD(IOService *client, UInt64 byteStart, IOMemoryDescriptor *buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageAttributes *attributes, UInt64 *actualByteCount);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/3516775-readcd)*