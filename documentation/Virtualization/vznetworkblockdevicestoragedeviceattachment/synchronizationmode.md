# synchronizationMode

**Framework**: Virtualization  
**Kind**: property

The mode in which the NBD client synchronizes data with the NBD server.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var synchronizationMode: VZDiskSynchronizationMode { get }
```

#### Discussion

See [`VZDiskSynchronizationMode`](vzdisksynchronizationmode.md) for details on how the specific mode affects data synchronization between the NBD client and server.

## See Also

- [var isForcedReadOnly: Bool](vznetworkblockdevicestoragedeviceattachment/isforcedreadonly.md)
  Returns a Boolean value that indicates whether the underlying disk attachment network is in a read-only state.
- [var timeout: TimeInterval](vznetworkblockdevicestoragedeviceattachment/timeout.md)
  The timeout value in seconds for the connection between the client and server.
- [var url: URL](vznetworkblockdevicestoragedeviceattachment/url.md)
  The URL that refers to the NBD server to which the NBD client will connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/synchronizationmode)*