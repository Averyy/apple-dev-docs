# TXTRecordGetLength(_:)

**Framework**: dnssd  
**Kind**: func

Allows you to determine the length of the raw bytes within a TXTRecordRef.

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
func TXTRecordGetLength(_ txtRecord: UnsafePointer<TXTRecordRef>!) -> UInt16
```

#### Return Value

Returns the size of the raw bytes inside a TXTRecordRef which you can pass directly to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md) or to [`DNSServiceUpdateRecord(_:_:_:_:_:_:)`](dnsserviceupdaterecord(_:_:_:_:_:_:).md). Returns 0 if the TXTRecordRef is empty.

## Parameters

- `txtRecord`: A TXTRecordRef initialized by calling TXTRecordCreate().

## See Also

- [func TXTRecordCreate(UnsafeMutablePointer<TXTRecordRef>!, UInt16, UnsafeMutableRawPointer!)](txtrecordcreate(_:_:_:).md)
  Creates a new empty TXTRecordRef referencing the specified storage.
- [func TXTRecordDeallocate(UnsafeMutablePointer<TXTRecordRef>!)](txtrecorddeallocate(_:).md)
  Releases resources associated with a TXT record.
- [func TXTRecordGetBytesPtr(UnsafePointer<TXTRecordRef>!) -> UnsafeRawPointer!](txtrecordgetbytesptr(_:).md)
  Allows you to retrieve a pointer to the raw bytes within a TXTRecordRef.
- [func TXTRecordRemoveValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](txtrecordremovevalue(_:_:).md)
  Removes a key from a TXTRecordRef.
- [func TXTRecordSetValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!, UInt8, UnsafeRawPointer!) -> DNSServiceErrorType](txtrecordsetvalue(_:_:_:_:).md)
  Adds a key (optionally with value) to a TXTRecordRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecordgetlength(_:))*