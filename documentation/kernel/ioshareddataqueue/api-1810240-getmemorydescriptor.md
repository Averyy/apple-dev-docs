# getMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

Returns a memory descriptor covering the IODataQueueMemory region.

## Declaration

```swift
virtual IOMemoryDescriptor *getMemoryDescriptor();
```

#### Return_value

Returns a newly allocated IOMemoryDescriptor for the IODataQueueMemory region. Returns zero on failure.

#### Overview

The IOMemoryDescriptor instance returned by this method is intended to be mapped into a user process. This is the memory region that the IODataQueueClient code operates on.

## See Also

- [dequeue](ioshareddataqueue/1810190-dequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [initWithCapacity](ioshareddataqueue/1810293-initwithcapacity.md)
  Initializes an IOSharedDataQueue instance with the capacity specified in the size parameter.
- [peek](ioshareddataqueue/1810347-peek.md)
  Used to peek at the next entry on the queue.
- [withCapacity](ioshareddataqueue/1810400-withcapacity.md)
  Static method that creates a new IOSharedDataQueue instance with the capacity specified in the size parameter.
- [withEntries](ioshareddataqueue/1810447-withentries.md)
  Static method that creates a new IOSharedDataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioshareddataqueue/1810240-getmemorydescriptor)*