# DNSServiceSetDispatchQueue(_:_:)

**Framework**: dnssd  
**Kind**: func

Allows you to schedule a DNSServiceRef on a serial dispatch queue for receiving asynchronous callbacks.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func DNSServiceSetDispatchQueue(_ service: DNSServiceRef!, _ queue: dispatch_queue_t!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success. Returns kDNSServiceErr_NoMemory if it cannot create a dispatch source Returns kDNSServiceErr_BadParam if the service param is invalid or the queue param is invalid

#### Discussion

It is the client’s responsibility to ensure that the provided dispatch queue is running.

A typical application that uses CFRunLoopRun or dispatch_main on its main thread will usually schedule DNSServiceRefs on its main queue (which is always a serial queue) using “DNSServiceSetDispatchQueue(sdref, dispatch_get_main_queue());”

If there is any error during the processing of events, the application callback will be called with an error code. For shared connections, each subordinate DNSServiceRef will get its own error callback. Currently these error callbacks only happen if the mDNSResponder daemon is manually terminated or crashes, and the error code in this case is kDNSServiceErr_ServiceNotRunning. The application must call DNSServiceRefDeallocate to free the DNSServiceRef when it gets such an error code. These error callbacks are rare and should not normally happen on customer machines, but application code should be written defensively to handle such error callbacks gracefully if they occur.

After using DNSServiceSetDispatchQueue on a DNSServiceRef, calling DNSServiceProcessResult on the same DNSServiceRef will result in undefined behavior and should be avoided.

Once the application successfully schedules a DNSServiceRef on a serial dispatch queue using DNSServiceSetDispatchQueue, it cannot remove the DNSServiceRef from the dispatch queue, or use DNSServiceSetDispatchQueue a second time to schedule the DNSServiceRef onto a different serial dispatch queue. Once scheduled onto a dispatch queue a DNSServiceRef will deliver events to that queue until the application no longer requires that operation and terminates it using DNSServiceRefDeallocate.

## Parameters

- `service`: DNSServiceRef that was allocated and returned to the application, when the application calls one of the DNSService API.
- `queue`: Dispatch queue where the application callback will be scheduled

## See Also

- [DNSServiceCreateDelegateConnection](dnsservicecreatedelegateconnection.md)
  Create a delegate connection to the daemon allowing efficient registration of multiple individual records.
- [func TXTRecordContainsKey(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!) -> Int32](txtrecordcontainskey(_:_:_:).md)
  Allows you to determine if a given TXT Record contains a specified key.
- [func TXTRecordGetCount(UInt16, UnsafeRawPointer!) -> UInt16](txtrecordgetcount(_:_:).md)
  Returns the number of keys stored in the TXT Record.
- [func TXTRecordGetItemAtIndex(UInt16, UnsafeRawPointer!, UInt16, UInt16, UnsafeMutablePointer<CChar>!, UnsafeMutablePointer<UInt8>!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> DNSServiceErrorType](txtrecordgetitematindex(_:_:_:_:_:_:_:).md)
  Allows you to retrieve a key name and value pointer, given an index into a TXT Record.
- [func TXTRecordGetValuePtr(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!, UnsafeMutablePointer<UInt8>!) -> UnsafeRawPointer!](txtrecordgetvalueptr(_:_:_:_:).md)
  Allows you to retrieve the value for a given key from a TXT Record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicesetdispatchqueue(_:_:))*