# init(url:)

**Framework**: Virtualization  
**Kind**: init

Creates a new network block device (NBD) storage attachment from an NDB Uniform Resource Indicator (URI) represented as a URL that you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
convenience init(url URL: URL) throws
```

## Parameters

- `URL`: The NBD’s URI represented as a URL.

## See Also

- [init(url: URL, timeout: TimeInterval, isForcedReadOnly: Bool, synchronizationMode: VZDiskSynchronizationMode) throws](vznetworkblockdevicestoragedeviceattachment/init(url:timeout:isforcedreadonly:synchronizationmode:).md)
  Creates a new network block device storage attachment from an NBD Uniform Resource Indicator (URI) represented as a URL, timeout value, and read-only and synchronization modes that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/init(url:))*