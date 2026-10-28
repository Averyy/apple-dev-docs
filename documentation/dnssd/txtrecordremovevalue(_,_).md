# TXTRecordRemoveValue(_:_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

Removes a key from a TXTRecordRef.

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
func TXTRecordRemoveValue(_ txtRecord: UnsafeMutablePointer<TXTRecordRef>!, _ key: UnsafePointer<CChar>!) -> DNSServiceErrorType
```

```c
DNSServiceErrorType TXTRecordRemoveValue(TXTRecordRef *txtRecord, const char *key);
```

## Return Value

Returns [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) on success. Returns kDNSServiceErr_NoSuchKey if the “key” does not exist in the TXTRecordRef.

## Parameters

- `txtRecord`: A TXTRecordRef initialized by calling TXTRecordCreate().
- `key`: A key name. This value must be an ASCII string that exists in the TXTRecordRef.

## See Also

### TXT Record Construction Functions
- [func TXTRecordCreate(UnsafeMutablePointer<TXTRecordRef>!, UInt16, UnsafeMutableRawPointer!)](./txtrecordcreate%28_,_,_%29.md)
  Creates a new empty TXTRecordRef referencing the specified storage.
- [func TXTRecordDeallocate(UnsafeMutablePointer<TXTRecordRef>!)](./txtrecorddeallocate%28_%29.md)
  Releases resources associated with a TXT record.
- [func TXTRecordGetBytesPtr(UnsafePointer<TXTRecordRef>!) -> UnsafeRawPointer!](./txtrecordgetbytesptr%28_%29.md)
  Allows you to retrieve a pointer to the raw bytes within a TXTRecordRef.
- [func TXTRecordGetLength(UnsafePointer<TXTRecordRef>!) -> UInt16](./txtrecordgetlength%28_%29.md)
  Allows you to determine the length of the raw bytes within a TXTRecordRef.
- [func TXTRecordSetValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!, UInt8, UnsafeRawPointer!) -> DNSServiceErrorType](./txtrecordsetvalue%28_,_,_,_%29.md)
  Adds a key (optionally with value) to a TXTRecordRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecordremovevalue(_:_:))*