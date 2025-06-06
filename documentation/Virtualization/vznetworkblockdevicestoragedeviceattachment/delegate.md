# delegate

**Framework**: Virtualization  
**Kind**: property

The object that receives messages about changes to the network block device attachment.

**Availability**:
- macOS 14.0+

## Declaration

```swift
weak var delegate: (any VZNetworkBlockDeviceStorageDeviceAttachmentDelegate)? { get set }
```

## See Also

- [protocol VZNetworkBlockDeviceStorageDeviceAttachmentDelegate](vznetworkblockdevicestoragedeviceattachmentdelegate.md)
  Methods you implement to respond to changes to a network block device attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachment/delegate)*