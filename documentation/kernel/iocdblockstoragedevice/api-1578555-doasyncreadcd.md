# doAsyncReadCD

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn doAsyncReadCD(IOMemoryDescriptor *buffer, UInt32 block, UInt32 nblks, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageCompletion completion);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdblockstoragedevice/1578555-doasyncreadcd)*