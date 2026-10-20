# doAsyncReadWrite

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15.2+

## Declaration

```cpp
virtual IOReturn doAsyncReadWrite(IOMemoryDescriptor *buffer, UInt64 block, UInt64 nblks, IOStorageAttributes *attributes, IOStorageCompletion *completion);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobdservices/3516729-doasyncreadwrite)*