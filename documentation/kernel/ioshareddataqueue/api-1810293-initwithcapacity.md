# initWithCapacity

**Framework**: Kernel  
**Kind**: instm

Initializes an IOSharedDataQueue instance with the capacity specified in the size parameter.

## Declaration

```swift
virtual Boolean initWithCapacity(
 UInt32size);
```

#### Return_value

Returns true on success and false on failure.

#### Overview

The actual size of the entire data queue memory region (to be shared into a user process) is equal to the capacity plus the IODataQueueMemory overhead. This overhead value can be determined from the DATA_QUEUE_MEMORY_HEADER_SIZE and DATA_QUEUE_MEMORY_APPENDIX_SIZE macro in <IOKit/IODataQueueShared.h>. The size of the data queue memory region must include space for the overhead of each IODataQueueEntry. This entry overhead can be determined from the DATA_QUEUE_ENTRY_HEADER_SIZE macro in <IOKit/IODataQueueShared.h>.

## Parameters

- `size`: The size of the data queue memory region.

## See Also

- [dequeue](ioshareddataqueue/1810190-dequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [getMemoryDescriptor](ioshareddataqueue/1810240-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [peek](ioshareddataqueue/1810347-peek.md)
  Used to peek at the next entry on the queue.
- [withCapacity](ioshareddataqueue/1810400-withcapacity.md)
  Static method that creates a new IOSharedDataQueue instance with the capacity specified in the size parameter.
- [withEntries](ioshareddataqueue/1810447-withentries.md)
  Static method that creates a new IOSharedDataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioshareddataqueue/1810293-initwithcapacity)*