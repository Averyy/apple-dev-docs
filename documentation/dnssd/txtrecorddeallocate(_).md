# TXTRecordDeallocate(_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

Releases resources associated with a TXT record.

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
func TXTRecordDeallocate(_ txtRecord: UnsafeMutablePointer<TXTRecordRef>!)
```

```c
void TXTRecordDeallocate(TXTRecordRef *txtRecord);
```

## Discussion

Releases any resources allocated in the course of preparing a TXT Record using TXTRecordCreate()/TXTRecordSetValue()/TXTRecordRemoveValue(). Ownership of the buffer provided in TXTRecordCreate() returns to the client.

## Parameters

- `txtRecord`: A TXTRecordRef initialized by calling TXTRecordCreate().

## See Also

### TXT Record Construction Functions
- [func TXTRecordCreate(UnsafeMutablePointer<TXTRecordRef>!, UInt16, UnsafeMutableRawPointer!)](./txtrecordcreate%28_,_,_%29.md)
  Creates a new empty TXTRecordRef referencing the specified storage.
- [func TXTRecordGetBytesPtr(UnsafePointer<TXTRecordRef>!) -> UnsafeRawPointer!](./txtrecordgetbytesptr%28_%29.md)
  Allows you to retrieve a pointer to the raw bytes within a TXTRecordRef.
- [func TXTRecordGetLength(UnsafePointer<TXTRecordRef>!) -> UInt16](./txtrecordgetlength%28_%29.md)
  Allows you to determine the length of the raw bytes within a TXTRecordRef.
- [func TXTRecordRemoveValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](./txtrecordremovevalue%28_,_%29.md)
  Removes a key from a TXTRecordRef.
- [func TXTRecordSetValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!, UInt8, UnsafeRawPointer!) -> DNSServiceErrorType](./txtrecordsetvalue%28_,_,_,_%29.md)
  Adds a key (optionally with value) to a TXTRecordRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecorddeallocate(_:))*