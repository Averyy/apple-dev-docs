# timeout

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The timeout value in seconds for the connection between the client and server.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var timeout: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval timeout;
```

#### Discussion

When the timeout expires, the client attempts to reconnect with the server. If after several retries, the client can’t reestablish a connection to the server, the framework invokes the [`attachment(_:didEncounterError:)`](../vznetworkblockdevicestoragedeviceattachmentdelegate/attachment%28_,didencountererror%29.md) delegate method.

## See Also

### Getting information about the attachment point
- [var isForcedReadOnly: Bool](./isforcedreadonly.md)
  Returns a Boolean value that indicates whether the underlying disk attachment network is in a read-only state.
- [var synchronizationMode: VZDiskSynchronizationMode](./synchronizationmode.md)
  The mode in which the NBD client synchronizes data with the NBD server.
- [var url: URL](./url.md)
  The URL that refers to the NBD server to which the NBD client will connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/timeout)*