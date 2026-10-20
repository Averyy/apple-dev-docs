# getMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

Returns a memory descriptor covering the IODataQueueMemory region.

## Declaration

```cpp
virtual IOMemoryDescriptor *getMemoryDescriptor();
```

#### Return Value

Returns a newly allocated IOMemoryDescriptor for the IODataQueueMemory region. Returns zero on failure.

#### Overview

The IOMemoryDescriptor instance returned by this method is intended to be mapped into a user process. This is the memory region that the IODataQueueClient code operates on.

## See Also

### Miscellaneous
- [enqueue](./api-1810927-enqueue.md)
  Enqueues a new entry on the queue.
- [initWithCapacity](./api-1810950-initwithcapacity.md)
  Initializes an IODataQueue instance with the capacity specified in the size parameter.
- [initWithEntries](./api-1810963-initwithentries.md)
  Initializes an IODataQueue instance with the specified number of entries of the given size.
- [sendDataAvailableNotification](./api-1810980-senddataavailablenotification.md)
  Sends a dataAvailableNotification message to the specified mach port.
- [setNotificationPort](./api-1810994-setnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [withCapacity](./api-1811001-withcapacity.md)
  Static method that creates a new IODataQueue instance with the capacity specified in the size parameter.
- [withEntries](./api-1811020-withentries.md)
  Static method that creates a new IODataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueue/1810939-getmemorydescriptor)*