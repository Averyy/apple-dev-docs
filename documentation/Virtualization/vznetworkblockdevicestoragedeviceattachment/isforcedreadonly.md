# isForcedReadOnly

**Framework**: Virtualization  
**Kind**: property

Returns a Boolean value that indicates whether the underlying disk attachment network is in a read-only state.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var isForcedReadOnly: Bool { get }
```

#### Discussion

The `forcedReadOnly` parameter affects how the Virtualization framework exposes the network block device (NBD) client to the guest operating system by the storage controller.

As part of the NBD protocol, during the handshake phase, the server advertises whether or not the disk the server exposes is read-only. Setting `forcedReadOnly` to [`true`](https://developer.apple.com/documentation/swift/true) forces the NBD client to show up as read-only to the guest regardless of whether or not the NBD server advertises itself as read-only.

## See Also

- [var synchronizationMode: VZDiskSynchronizationMode](vznetworkblockdevicestoragedeviceattachment/synchronizationmode.md)
  The mode in which the NBD client synchronizes data with the NBD server.
- [var timeout: TimeInterval](vznetworkblockdevicestoragedeviceattachment/timeout.md)
  The timeout value in seconds for the connection between the client and server.
- [var url: URL](vznetworkblockdevicestoragedeviceattachment/url.md)
  The URL that refers to the NBD server to which the NBD client will connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/isforcedreadonly)*