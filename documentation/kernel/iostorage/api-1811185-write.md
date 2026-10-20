# write()

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
#ifdef __LP64__
 virtual void write(
 IOService *client, 
 UInt64 byteStart, 
 IOMemoryDescriptor *buffer, 
 IOStorageAttributes *attributes, 
 IOStorageCompletion *completion) = 0; 
#else /* !__LP64__ */
virtual void write(
 IOService *client, 
 UInt64 byteStart, 
 IOMemoryDescriptor *buffer, 
 IOStorageAttributes *attributes, 
 IOStorageCompletion *completion); 
#endif 
/* !__LP64__ */
```

#### Overview

Write data into the storage object at the specified byte offset from the specified buffer, asynchronously. When the write completes, the caller will be notified via the specified completion action.

The buffer will be retained for the duration of the write.

## Parameters

- `client`: Client requesting the write.
- `byteStart`: Starting byte offset for the data transfer.
- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `attributes`: Attributes of the data transfer. See IOStorageAttributes. It is the responsibility of the callee to maintain the information for the duration of the data transfer, as necessary.
- `completion`: Completion routine to call once the data transfer is complete. It is the responsibility of the callee to maintain the information for the duration of the data transfer, as necessary.

## See Also

### Miscellaneous
- [complete](./api-1810767-complete.md)
- [copyPhysicalExtent](./api-1810820-copyphysicalextent.md)
- [handleClose](./api-1810866-handleclose.md)
- [handleIsOpen](./api-1810905-handleisopen.md)
- [handleOpen](./api-1810948-handleopen.md)
- [lockPhysicalExtents](./api-1810985-lockphysicalextents.md)
- [open](./api-1811013-open.md)
- [read()](./api-1811038-read.md)
- [read()](./api-1811068-read.md)
- [synchronizeCache](./api-1811091-synchronizecache.md)
- [unlockPhysicalExtents](./api-1811117-unlockphysicalextents.md)
- [unmap](./api-1811145-unmap.md)
- [write()](./api-1811168-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostorage/1811185-write)*