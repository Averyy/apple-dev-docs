# AsyncReadWrite

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15.2+

## Declaration

```cpp
virtual IOReturn AsyncReadWrite(IOMemoryDescriptor *buffer, UInt64 startBlock, UInt64 blockCount, UInt64 blockSize, IOStorageAttributes *attributes, void *clientData);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice/3516743-asyncreadwrite)*