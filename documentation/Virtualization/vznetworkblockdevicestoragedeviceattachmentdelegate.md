# VZNetworkBlockDeviceStorageDeviceAttachmentDelegate

**Framework**: Virtualization  
**Kind**: protocol  
**Role**: Protocol

Methods you implement to respond to changes to a network block device attachment.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol VZNetworkBlockDeviceStorageDeviceAttachmentDelegate : NSObjectProtocol
```

```objc
@protocol VZNetworkBlockDeviceStorageDeviceAttachmentDelegate <NSObject>
```

## Topics

### Responding to connectivity changes
- [func attachment(VZNetworkBlockDeviceStorageDeviceAttachment, didEncounterError: any Error)](./vznetworkblockdevicestoragedeviceattachmentdelegate/attachment%28_,didencountererror%29.md)
  The method the attachment object calls when the NBD client encounters a nonrecoverable error.
- [func attachmentWasConnected(VZNetworkBlockDeviceStorageDeviceAttachment)](./vznetworkblockdevicestoragedeviceattachmentdelegate/attachmentwasconnected%28_%29.md)
  The method the attachment object calls when the NBD client successfully connects or reconnects with the server.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing changes to the network block device
- [var delegate: (any VZNetworkBlockDeviceStorageDeviceAttachmentDelegate)?](./vznetworkblockdevicestoragedeviceattachment/delegate.md)
  The object that receives messages about changes to the network block device attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachmentdelegate)*