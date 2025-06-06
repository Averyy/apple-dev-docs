# TXTRecordGetItemAtIndex(_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Allows you to retrieve a key name and value pointer, given an index into a TXT Record.

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
func TXTRecordGetItemAtIndex(_ txtLen: UInt16, _ txtRecord: UnsafeRawPointer!, _ itemIndex: UInt16, _ keyBufLen: UInt16, _ key: UnsafeMutablePointer<CChar>!, _ valueLen: UnsafeMutablePointer<UInt8>!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success. Returns kDNSServiceErr_NoMemory if keyBufLen is too short. Returns kDNSServiceErr_Invalid if index is greater than TXTRecordGetCount()-1.

#### Discussion

Legal index values range from zero to TXTRecordGetCount()-1. It’s also possible to iterate through keys in a TXT record by simply calling TXTRecordGetItemAtIndex() repeatedly, beginning with index zero and increasing until TXTRecordGetItemAtIndex() returns kDNSServiceErr_Invalid.

On return:

For keys with no value, *value is set to NULL and *valueLen is zero.

For keys with empty value, *value is non-NULL and *valueLen is zero.

For keys with non-empty value, *value is non-NULL and *valueLen is non-zero.

## Parameters

- `txtLen`: The size of the received TXT Record.
- `txtRecord`: Pointer to the received TXT Record bytes.
- `itemIndex`: An index into the TXT Record.
- `keyBufLen`: The size of the string buffer being supplied.
- `key`: A string buffer used to store the key name. On return, the buffer contains a null-terminated C string giving the key name. DNS-SD TXT keys are usually 9 characters or fewer. To hold the maximum possible key name, the buffer should be 256 bytes long.
- `valueLen`: On output, will be set to the size of the “value” data.
- `value`: On output, *value is set to point to location within TXT Record bytes that holds the value data.

## See Also

- [DNSServiceCreateDelegateConnection](dnsservicecreatedelegateconnection.md)
  Create a delegate connection to the daemon allowing efficient registration of multiple individual records.
- [func DNSServiceSetDispatchQueue(DNSServiceRef!, dispatch_queue_t!) -> DNSServiceErrorType](dnsservicesetdispatchqueue(_:_:).md)
  Allows you to schedule a DNSServiceRef on a serial dispatch queue for receiving asynchronous callbacks.
- [func TXTRecordContainsKey(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!) -> Int32](txtrecordcontainskey(_:_:_:).md)
  Allows you to determine if a given TXT Record contains a specified key.
- [func TXTRecordGetCount(UInt16, UnsafeRawPointer!) -> UInt16](txtrecordgetcount(_:_:).md)
  Returns the number of keys stored in the TXT Record.
- [func TXTRecordGetValuePtr(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!, UnsafeMutablePointer<UInt8>!) -> UnsafeRawPointer!](txtrecordgetvalueptr(_:_:_:_:).md)
  Allows you to retrieve the value for a given key from a TXT Record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecordgetitematindex(_:_:_:_:_:_:_:))*