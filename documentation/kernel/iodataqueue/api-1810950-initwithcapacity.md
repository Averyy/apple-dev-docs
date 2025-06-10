# initWithCapacity

**Framework**: Kernel  
**Kind**: instm

Initializes an IODataQueue instance with the capacity specified in the size parameter.

## Declaration

```swift
virtual Boolean initWithCapacity(
 UInt32size);
```

#### Return_value

Returns true on success and false on failure.

#### Overview

The actual size of the entire data queue memory region (to be shared into a user process) is equal to the capacity plus the IODataQueueMemory overhead. This overhead value can be determined from the DATA_QUEUE_MEMORY_HEADER_SIZE macro in <IOKit/IODataQueueShared.h>. The size of the data queue memory region must include space for the overhead of each IODataQueueEntry. This entry overhead can be determined from the DATA_QUEUE_ENTRY_HEADER_SIZE macro in <IOKit/IODataQueueShared.h>.

## Parameters

- `size`: The size of the data queue memory region.

## See Also

- [enqueue](iodataqueue/1810927-enqueue.md)
  Enqueues a new entry on the queue.
- [getMemoryDescriptor](iodataqueue/1810939-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithEntries](iodataqueue/1810963-initwithentries.md)
  Initializes an IODataQueue instance with the specified number of entries of the given size.
- [sendDataAvailableNotification](iodataqueue/1810980-senddataavailablenotification.md)
  Sends a dataAvailableNotification message to the specified mach port.
- [setNotificationPort](iodataqueue/1810994-setnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [withCapacity](iodataqueue/1811001-withcapacity.md)
  Static method that creates a new IODataQueue instance with the capacity specified in the size parameter.
- [withEntries](iodataqueue/1811020-withentries.md)
  Static method that creates a new IODataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueue/1810950-initwithcapacity)*