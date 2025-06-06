# withEntries

**Framework**: Kernel  
**Kind**: instm

Static method that creates a new IOSharedDataQueue instance with the specified number of entries of the given size.

## Declaration

```swift
static IOSharedDataQueue *withEntries(
 UInt32numEntries,
 UInt32entrySize);
```

#### Return_value

Reeturns the newly allocated IOSharedDataQueue instance. Zero is returned on failure.

#### Overview

This method will create a new IOSharedDataQueue instance with enough capacity for numEntries of entrySize. It does account for the IODataQueueEntry overhead for each entry. Note that the numEntries and entrySize are simply used to determine the data region size. They do not actually restrict the size of number of entries that can be added to the queue.

This method allocates a new IODataQueue instance and then calls initWithEntries() with the given numEntries and entrySize parameters. If the initWithEntries() fails, the new instance is released and zero is returned.

## Parameters

- `numEntries`: Number of entries to allocate space for.
- `entrySize`: Size of each entry.

## See Also

- [dequeue](ioshareddataqueue/1810190-dequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [getMemoryDescriptor](ioshareddataqueue/1810240-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithCapacity](ioshareddataqueue/1810293-initwithcapacity.md)
  Initializes an IOSharedDataQueue instance with the capacity specified in the size parameter.
- [peek](ioshareddataqueue/1810347-peek.md)
  Used to peek at the next entry on the queue.
- [withCapacity](ioshareddataqueue/1810400-withcapacity.md)
  Static method that creates a new IOSharedDataQueue instance with the capacity specified in the size parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioshareddataqueue/1810447-withentries)*