# enqueue

**Framework**: Kernel  
**Kind**: instm

Enqueues a new entry on the queue.

## Declaration

```cpp
virtual Boolean enqueue(
 void *data,
 UInt32dataSize);
```

## Return Value

Returns true on success and false on failure. Typically failure means that the queue is full.

## Overview

This method adds a new data entry of dataSize to the queue. It sets the size parameter of the entry pointed to by the tail value and copies the memory pointed to by the data parameter in place in the queue. Once that is done, it moves the tail to the next available location. When attempting to add a new entry towards the end of the queue and there isn't enough space at the end, it wraps back to the beginning.

If the queue is empty when a new entry is added, sendDataAvailableNotification() is called to send a message to the user process that data is now available.

## Parameters

- `data`: Pointer to the data to be added to the queue.
- `dataSize`: Size of the data pointed to by data.

## See Also

### Miscellaneous
- [getMemoryDescriptor](./api-1810939-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueue/1810927-enqueue)*