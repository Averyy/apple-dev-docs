# doAsyncReadWrite

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn doAsyncReadWrite(IOMemoryDescriptor *buffer, UInt64 block, UInt64 nblks, IOStorageAttributes *attributes, IOStorageCompletion *completion);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedevice/1568473-doasyncreadwrite)*