# VZNetworkBlockDeviceStorageDeviceAttachmentDelegate

**Framework**: Virtualization  
**Kind**: protocol

Methods you implement to respond to changes to a network block device attachment.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol VZNetworkBlockDeviceStorageDeviceAttachmentDelegate : NSObjectProtocol
```

## Topics

### Responding to connectivity changes
- [func attachment(VZNetworkBlockDeviceStorageDeviceAttachment, didEncounterError: any Error)](vznetworkblockdevicestoragedeviceattachmentdelegate/attachment(_:didencountererror:).md)
  The method the attachment object calls when the NBD client encounters a nonrecoverable error.
- [func attachmentWasConnected(VZNetworkBlockDeviceStorageDeviceAttachment)](vznetworkblockdevicestoragedeviceattachmentdelegate/attachmentwasconnected(_:).md)
  The method the attachment object calls when the NBD client successfully connects or reconnects with the server.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any VZNetworkBlockDeviceStorageDeviceAttachmentDelegate)?](vznetworkblockdevicestoragedeviceattachment/delegate.md)
  The object that receives messages about changes to the network block device attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachmentdelegate)*