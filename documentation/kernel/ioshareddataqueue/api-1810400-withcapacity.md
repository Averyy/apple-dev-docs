# withCapacity

**Framework**: Kernel  
**Kind**: instm

Static method that creates a new IOSharedDataQueue instance with the capacity specified in the size parameter.

## Declaration

```swift
static IOSharedDataQueue *withCapacity(
 UInt32size);
```

#### Return_value

Returns the newly allocated IOSharedDataQueue instance. Zero is returned on failure.

#### Overview

The actual size of the entire data queue memory region (to be shared into a user process) is equal to the capacity plus the IODataQueueMemory overhead. This overhead value can be determined from the DATA_QUEUE_MEMORY_HEADER_SIZE macro in <IOKit/IODataQueueShared.h>. The size of the data queue memory region must include space for the overhead of each IODataQueueEntry. This entry overhead can be determined from the DATA_QUEUE_ENTRY_HEADER_SIZE macro in <IOKit/IODataQueueShared.h>.

This method allocates a new IODataQueue instance and then calls initWithCapacity() with the given size parameter. If the initWithCapacity() fails, the new instance is released and zero is returned.

## Parameters

- `size`: The size of the data queue memory region.

## See Also

- [dequeue](ioshareddataqueue/1810190-dequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [getMemoryDescriptor](ioshareddataqueue/1810240-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithCapacity](ioshareddataqueue/1810293-initwithcapacity.md)
  Initializes an IOSharedDataQueue instance with the capacity specified in the size parameter.
- [peek](ioshareddataqueue/1810347-peek.md)
  Used to peek at the next entry on the queue.
- [withEntries](ioshareddataqueue/1810447-withentries.md)
  Static method that creates a new IOSharedDataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioshareddataqueue/1810400-withcapacity)*