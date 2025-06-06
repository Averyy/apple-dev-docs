# IODataQueueAllocateNotificationPort()

**Framework**: IOKit  
**Kind**: func

Allocates and returns a new mach port able to receive data available notifications from an IODataQueue.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
func IODataQueueAllocateNotificationPort() -> mach_port_t
```

#### Return_value

Returns a newly allocated mach port on success. On failure, it returns MACH_PORT_NULL.

#### Discussion

This port is intended to be passed down into the kernel and into an IODataQueue to allow it to send the appropriate notification. The returned mach port is allocated with a queue limit of one message. This allows only one mach message to be queued up at a time. The IODataQueue code is written with the restriction in mind and will only queue up a message if no messages alread have been sent.

## See Also

- [func IODataQueueDataAvailable(UnsafeMutablePointer<IODataQueueMemory>!) -> Bool](1514386-iodataqueuedataavailable.md)
  Used to determine if more data is avilable on the queue.
- [func IODataQueueDequeue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<UInt32>!) -> IOReturn](1514287-iodataqueuedequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [func IODataQueueEnqueue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UInt32) -> IOReturn](1514482-iodataqueueenqueue.md)
  Enqueues a new entry on the queue.
- [func IODataQueuePeek(UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>!](1514649-iodataqueuepeek.md)
  Used to peek at the next entry on the queue.
- [func IODataQueueSetNotificationPort(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514301-iodataqueuesetnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [func IODataQueueWaitForAvailableData(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514696-iodataqueuewaitforavailabledata.md)
  Wait for an incoming dataAvailable message on the given notifyPort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514495-iodataqueueallocatenotificationp)*