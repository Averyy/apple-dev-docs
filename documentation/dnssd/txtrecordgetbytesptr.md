# TXTRecordGetBytesPtr(_:)

**Framework**: dnssd  
**Kind**: func

Allows you to retrieve a pointer to the raw bytes within a TXTRecordRef.

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
func TXTRecordGetBytesPtr(_ txtRecord: UnsafePointer<TXTRecordRef>!) -> UnsafeRawPointer!
```

#### Return Value

Returns a pointer to the raw bytes inside the TXTRecordRef which you can pass directly to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md) or to [`DNSServiceUpdateRecord(_:_:_:_:_:_:)`](dnsserviceupdaterecord(_:_:_:_:_:_:).md).

## Parameters

- `txtRecord`: A TXTRecordRef initialized by calling TXTRecordCreate().

## See Also

- [func TXTRecordCreate(UnsafeMutablePointer<TXTRecordRef>!, UInt16, UnsafeMutableRawPointer!)](txtrecordcreate(_:_:_:).md)
  Creates a new empty TXTRecordRef referencing the specified storage.
- [func TXTRecordDeallocate(UnsafeMutablePointer<TXTRecordRef>!)](txtrecorddeallocate(_:).md)
  Releases resources associated with a TXT record.
- [func TXTRecordGetLength(UnsafePointer<TXTRecordRef>!) -> UInt16](txtrecordgetlength(_:).md)
  Allows you to determine the length of the raw bytes within a TXTRecordRef.
- [func TXTRecordRemoveValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](txtrecordremovevalue(_:_:).md)
  Removes a key from a TXTRecordRef.
- [func TXTRecordSetValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!, UInt8, UnsafeRawPointer!) -> DNSServiceErrorType](txtrecordsetvalue(_:_:_:_:).md)
  Adds a key (optionally with value) to a TXTRecordRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecordgetbytesptr(_:))*