# TXTRecordContainsKey(_:_:_:)

**Framework**: dnssd  
**Kind**: func

Allows you to determine if a given TXT Record contains a specified key.

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
func TXTRecordContainsKey(_ txtLen: UInt16, _ txtRecord: UnsafeRawPointer!, _ key: UnsafePointer<CChar>!) -> Int32
```

#### Return Value

Returns 1 if the TXT Record contains the specified key. Otherwise, it returns 0.

## Parameters

- `txtLen`: The size of the received TXT Record.
- `txtRecord`: Pointer to the received TXT Record bytes.
- `key`: A null-terminated ASCII string containing the key name.

## See Also

- [DNSServiceCreateDelegateConnection](dnsservicecreatedelegateconnection.md)
  Create a delegate connection to the daemon allowing efficient registration of multiple individual records.
- [func DNSServiceSetDispatchQueue(DNSServiceRef!, dispatch_queue_t!) -> DNSServiceErrorType](dnsservicesetdispatchqueue(_:_:).md)
  Allows you to schedule a DNSServiceRef on a serial dispatch queue for receiving asynchronous callbacks.
- [func TXTRecordGetCount(UInt16, UnsafeRawPointer!) -> UInt16](txtrecordgetcount(_:_:).md)
  Returns the number of keys stored in the TXT Record.
- [func TXTRecordGetItemAtIndex(UInt16, UnsafeRawPointer!, UInt16, UInt16, UnsafeMutablePointer<CChar>!, UnsafeMutablePointer<UInt8>!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> DNSServiceErrorType](txtrecordgetitematindex(_:_:_:_:_:_:_:).md)
  Allows you to retrieve a key name and value pointer, given an index into a TXT Record.
- [func TXTRecordGetValuePtr(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!, UnsafeMutablePointer<UInt8>!) -> UnsafeRawPointer!](txtrecordgetvalueptr(_:_:_:_:).md)
  Allows you to retrieve the value for a given key from a TXT Record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecordcontainskey(_:_:_:))*