# init(url:timeout:isForcedReadOnly:synchronizationMode:)

**Framework**: Virtualization  
**Kind**: init

Creates a new network block device storage attachment from an NBD Uniform Resource Indicator (URI) represented as a URL, timeout value, and read-only and synchronization modes that you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(url URL: URL, timeout: TimeInterval, isForcedReadOnly forcedReadOnly: Bool, synchronizationMode: VZDiskSynchronizationMode) throws
```

#### Discussion

The `forcedReadOnly` parameter affects how framework exposes the NBD client to the guest operating system by the storage controller. As part of the NBD protocol, the NBD server advertises whether or not the disk exposed by the NBD client is read-only during the handshake phase of the protocol. Setting `forcedReadOnly` to [`true`](https://developer.apple.com/documentation/swift/true) forces the NBD client to show up as read-only to the guest regardless of whether or not the NBD server advertises itself as read-only.

## Parameters

- `URL`: The NBD’s URI represented as a URL.
- `timeout`: The timeout value in seconds for the connection between the client and server. When the timeout expires, an attempt to reconnect with the server takes place.
- `forcedReadOnly`: If  , the framework forces the disk attachment to be read-only, regardless of whether or not the NBD server supports write requests.
- `synchronizationMode`: The mode in which the disk attachment synchronizes data with the underlying storage device.

## See Also

- [convenience init(url: URL) throws](vznetworkblockdevicestoragedeviceattachment/init(url:).md)
  Creates a new network block device (NBD) storage attachment from an NDB Uniform Resource Indicator (URI) represented as a URL that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/init(url:timeout:isforcedreadonly:synchronizationmode:))*