# dequeue

**Framework**: Kernel  
**Kind**: instm

Dequeues the next available entry on the queue and copies it into the given data pointer.

## Declaration

```swift
virtual Boolean dequeue(
 void *data,
 UInt32 *dataSize);
```

#### Return_value

Returns true on success and false on failure. Typically failure means that the queue is empty.

#### Overview

This function will dequeue the next available entry on the queue. If a data pointer is provided, it will copy the data into the memory region if there is enough space available as specified in the dataSize parameter. If no data pointer is provided, it will simply move the head value past the current entry.

## Parameters

- `data`: A pointer to the data memory region in which to copy the next entry data on the queue. If this parameter is 0 (NULL), it will simply move to the next entry.
- `dataSize`: A pointer to the size of the data parameter. On return, this contains the size of the actual entry data - even if the original size was not large enough.

## See Also

- [getMemoryDescriptor](ioshareddataqueue/1810240-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithCapacity](ioshareddataqueue/1810293-initwithcapacity.md)
  Initializes an IOSharedDataQueue instance with the capacity specified in the size parameter.
- [peek](ioshareddataqueue/1810347-peek.md)
  Used to peek at the next entry on the queue.
- [withCapacity](ioshareddataqueue/1810400-withcapacity.md)
  Static method that creates a new IOSharedDataQueue instance with the capacity specified in the size parameter.
- [withEntries](ioshareddataqueue/1810447-withentries.md)
  Static method that creates a new IOSharedDataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioshareddataqueue/1810190-dequeue)*