# IODataQueueDequeue(_:_:_:)

**Framework**: IOKit  
**Kind**: func

Dequeues the next available entry on the queue and copies it into the given data pointer.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
func IODataQueueDequeue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ data: UnsafeMutableRawPointer!, _ dataSize: UnsafeMutablePointer<UInt32>!) -> IOReturn
```

#### Return_value

Returns kIOReturnSuccess on success. Other return values possible are: kIOReturnUnderrun - queue is empty, kIOReturnBadArgument - no dataQueue or no dataSize, kIOReturnNoSpace - dataSize is too small for entry.

#### Discussion

This function will dequeue the next available entry on the queue. If a data pointer is provided, it will copy the data into the memory region if there is enough space available as specified in the dataSize parameter. If no data pointer is provided, it will simply move the head value past the current entry.

## Parameters

- `dataQueue`: The IODataQueueMemory region mapped from the kernel.
- `data`: A pointer to the data memory region in which to copy the next entry data on the queue. If this parameter is 0 (NULL), it will simply move to the next entry.
- `dataSize`: A pointer to the size of the data parameter. On return, this contains the size of the actual entry data - even if the original size was not large enough.

## See Also

- [func IODataQueueAllocateNotificationPort() -> mach_port_t](1514495-iodataqueueallocatenotificationp.md)
  Allocates and returns a new mach port able to receive data available notifications from an IODataQueue.
- [func IODataQueueDataAvailable(UnsafeMutablePointer<IODataQueueMemory>!) -> Bool](1514386-iodataqueuedataavailable.md)
  Used to determine if more data is avilable on the queue.
- [func IODataQueueEnqueue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UInt32) -> IOReturn](1514482-iodataqueueenqueue.md)
  Enqueues a new entry on the queue.
- [func IODataQueuePeek(UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>!](1514649-iodataqueuepeek.md)
  Used to peek at the next entry on the queue.
- [func IODataQueueSetNotificationPort(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514301-iodataqueuesetnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [func IODataQueueWaitForAvailableData(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514696-iodataqueuewaitforavailabledata.md)
  Wait for an incoming dataAvailable message on the given notifyPort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514287-iodataqueuedequeue)*