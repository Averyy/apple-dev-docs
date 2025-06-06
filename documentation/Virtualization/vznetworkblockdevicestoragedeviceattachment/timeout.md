# timeout

**Framework**: Virtualization  
**Kind**: property

The timeout value in seconds for the connection between the client and server.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var timeout: TimeInterval { get }
```

#### Discussion

When the timeout expires, the client attempts to reconnect with the server. If after several retries, the client can’t reestablish a connection to the server, the framework invokes the [`attachment(_:didEncounterError:)`](vznetworkblockdevicestoragedeviceattachmentdelegate/attachment(_:didencountererror:).md) delegate method.

## See Also

- [var isForcedReadOnly: Bool](vznetworkblockdevicestoragedeviceattachment/isforcedreadonly.md)
  Returns a Boolean value that indicates whether the underlying disk attachment network is in a read-only state.
- [var synchronizationMode: VZDiskSynchronizationMode](vznetworkblockdevicestoragedeviceattachment/synchronizationmode.md)
  The mode in which the NBD client synchronizes data with the NBD server.
- [var url: URL](vznetworkblockdevicestoragedeviceattachment/url.md)
  The URL that refers to the NBD server to which the NBD client will connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/timeout)*