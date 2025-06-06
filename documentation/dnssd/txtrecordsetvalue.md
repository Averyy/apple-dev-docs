# TXTRecordSetValue(_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Adds a key (optionally with value) to a TXTRecordRef.

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
func TXTRecordSetValue(_ txtRecord: UnsafeMutablePointer<TXTRecordRef>!, _ key: UnsafePointer<CChar>!, _ valueSize: UInt8, _ value: UnsafeRawPointer!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success. Returns kDNSServiceErr_Invalid if the “key” string contains illegal characters. Returns kDNSServiceErr_NoMemory if adding this key would exceed the available storage.

#### Discussion

If the “key” already exists in the TXTRecordRef, then the current value will be replaced with the new value. Keys may exist in four states with respect to a given TXT record: - Absent (key does not appear at all) - Present with no value (“key” appears alone) - Present with empty value (“key=” appears in TXT record) - Present with non-empty value (“key=value” appears in TXT record) For more details refer to “Data Syntax for DNS-SD TXT Records” in [`dns-sd.org`](https://developer.apple.comhttp://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt)

## Parameters

- `txtRecord`: A TXTRecordRef initialized by calling TXTRecordCreate().
- `key`: A null-terminated string which only contains printable ASCII values (0x20-0x7E), excluding ‘=’ (0x3D). Keys should be 9 characters or fewer (not counting the terminating null).
- `valueSize`: The size of the value.
- `value`: Any binary value. For values that represent textual data, UTF-8 is STRONGLY recommended. For values that represent textual data, valueSize should NOT include the terminating null (if any) at the end of the string. If NULL, then “key” will be added with no value. If non-NULL but valueSize is zero, then “key=” will be added with empty value.

## See Also

- [func TXTRecordCreate(UnsafeMutablePointer<TXTRecordRef>!, UInt16, UnsafeMutableRawPointer!)](txtrecordcreate(_:_:_:).md)
  Creates a new empty TXTRecordRef referencing the specified storage.
- [func TXTRecordDeallocate(UnsafeMutablePointer<TXTRecordRef>!)](txtrecorddeallocate(_:).md)
  Releases resources associated with a TXT record.
- [func TXTRecordGetBytesPtr(UnsafePointer<TXTRecordRef>!) -> UnsafeRawPointer!](txtrecordgetbytesptr(_:).md)
  Allows you to retrieve a pointer to the raw bytes within a TXTRecordRef.
- [func TXTRecordGetLength(UnsafePointer<TXTRecordRef>!) -> UInt16](txtrecordgetlength(_:).md)
  Allows you to determine the length of the raw bytes within a TXTRecordRef.
- [func TXTRecordRemoveValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](txtrecordremovevalue(_:_:).md)
  Removes a key from a TXTRecordRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/txtrecordsetvalue(_:_:_:_:))*