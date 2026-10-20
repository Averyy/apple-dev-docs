# doAsyncReadCD

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn doAsyncReadCD(IOMemoryDescriptor *buffer, UInt32 block, UInt32 nblks, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageCompletion completion);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdblockstoragedevice/1578555-doasyncreadcd)*