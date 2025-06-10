# withEntries

**Framework**: Kernel  
**Kind**: instm

Static method that creates a new IODataQueue instance with the specified number of entries of the given size.

## Declaration

```swift
static IODataQueue *withEntries(
 UInt32numEntries,
 UInt32entrySize);
```

#### Return_value

Reeturns the newly allocated IODataQueue instance. Zero is returned on failure.

#### Overview

This method will create a new IODataQueue instance with enough capacity for numEntries of entrySize. It does account for the IODataQueueEntry overhead for each entry. Note that the numEntries and entrySize are simply used to determine the data region size. They do not actually restrict the size of number of entries that can be added to the queue.

This method allocates a new IODataQueue instance and then calls initWithEntries() with the given numEntries and entrySize parameters. If the initWithEntries() fails, the new instance is released and zero is returned.

## Parameters

- `numEntries`: Number of entries to allocate space for.
- `entrySize`: Size of each entry.

## See Also

- [enqueue](iodataqueue/1810927-enqueue.md)
  Enqueues a new entry on the queue.
- [getMemoryDescriptor](iodataqueue/1810939-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithCapacity](iodataqueue/1810950-initwithcapacity.md)
  Initializes an IODataQueue instance with the capacity specified in the size parameter.
- [initWithEntries](iodataqueue/1810963-initwithentries.md)
  Initializes an IODataQueue instance with the specified number of entries of the given size.
- [sendDataAvailableNotification](iodataqueue/1810980-senddataavailablenotification.md)
  Sends a dataAvailableNotification message to the specified mach port.
- [setNotificationPort](iodataqueue/1810994-setnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [withCapacity](iodataqueue/1811001-withcapacity.md)
  Static method that creates a new IODataQueue instance with the capacity specified in the size parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueue/1811020-withentries)*