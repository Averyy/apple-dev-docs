# isForcedReadOnly

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the underlying disk attachment network is in a read-only state.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var isForcedReadOnly: Bool { get }
```

```objc
@property (readonly, getter=isForcedReadOnly) BOOL forcedReadOnly;
```

#### Discussion

The `forcedReadOnly` parameter affects how the Virtualization framework exposes the network block device (NBD) client to the guest operating system by the storage controller.

As part of the NBD protocol, during the handshake phase, the server advertises whether or not the disk the server exposes is read-only. Setting `forcedReadOnly` to [`true`](../../Swift/true.md) forces the NBD client to show up as read-only to the guest regardless of whether or not the NBD server advertises itself as read-only.

## See Also

### Getting information about the attachment point
- [var synchronizationMode: VZDiskSynchronizationMode](./synchronizationmode.md)
  The mode in which the NBD client synchronizes data with the NBD server.
- [var timeout: TimeInterval](./timeout.md)
  The timeout value in seconds for the connection between the client and server.
- [var url: URL](./url.md)
  The URL that refers to the NBD server to which the NBD client will connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/isforcedreadonly)*