# writeCD

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual void writeCD(IOService *client, UInt64 byteStart, IOMemoryDescriptor *buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageAttributes *attributes, IOStorageCompletion *completion);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdblockstoragedriver/1572083-writecd)*