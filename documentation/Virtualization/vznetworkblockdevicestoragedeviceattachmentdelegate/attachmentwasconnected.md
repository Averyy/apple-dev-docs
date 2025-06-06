# attachmentWasConnected(_:)

**Framework**: Virtualization  
**Kind**: method

The method the attachment object calls when the NBD client successfully connects or reconnects with the server.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func attachmentWasConnected(_ attachment: VZNetworkBlockDeviceStorageDeviceAttachment)
```

#### Discussion

Connection with the server takes place when the VM is first started, and reconnection attempts take place when the connection times out or when the NBD client has encountered a recoverable error, such as an I/O error from the server. The Virtualization framework may call this method multiple times during a VM’s life cycle. Reconnections are transparent to the guest.

## Parameters

- `attachment`: The attachment object calling the delegate method.

## See Also

- [func attachment(VZNetworkBlockDeviceStorageDeviceAttachment, didEncounterError: any Error)](vznetworkblockdevicestoragedeviceattachmentdelegate/attachment(_:didencountererror:).md)
  The method the attachment object calls when the NBD client encounters a nonrecoverable error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachmentdelegate/attachmentwasconnected(_:))*