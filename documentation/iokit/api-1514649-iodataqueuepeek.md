# IODataQueuePeek(_:)

**Framework**: IOKit  
**Kind**: func

Used to peek at the next entry on the queue.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
func IODataQueuePeek(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>!
```

#### Return_value

Returns a pointer to the next IODataQueueEntry if one is available. Zero is returned if the queue is empty.

#### Discussion

This function can be used to look at the next entry which allows the entry to be received without having to copy it with IODataQueueDequeue. In order to do this, call IODataQueuePeek to get the entry. Then call IODataQueueDequeue with a NULL data pointer. That will cause the head to be moved to the next entry, but no memory to be copied.

## Parameters

- `dataQueue`: The IODataQueueMemory region mapped from the kernel.

## See Also

- [func IODataQueueAllocateNotificationPort() -> mach_port_t](1514495-iodataqueueallocatenotificationp.md)
  Allocates and returns a new mach port able to receive data available notifications from an IODataQueue.
- [func IODataQueueDataAvailable(UnsafeMutablePointer<IODataQueueMemory>!) -> Bool](1514386-iodataqueuedataavailable.md)
  Used to determine if more data is avilable on the queue.
- [func IODataQueueDequeue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<UInt32>!) -> IOReturn](1514287-iodataqueuedequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [func IODataQueueEnqueue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UInt32) -> IOReturn](1514482-iodataqueueenqueue.md)
  Enqueues a new entry on the queue.
- [func IODataQueueSetNotificationPort(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514301-iodataqueuesetnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [func IODataQueueWaitForAvailableData(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514696-iodataqueuewaitforavailabledata.md)
  Wait for an incoming dataAvailable message on the given notifyPort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514649-iodataqueuepeek)*