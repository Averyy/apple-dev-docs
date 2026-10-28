# attachment(_:didEncounterError:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the attachment object calls when the NBD client encounters a nonrecoverable error.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func attachment(_ attachment: VZNetworkBlockDeviceStorageDeviceAttachment, didEncounterError error: any Error)
```

```objc
- (void) attachment:(VZNetworkBlockDeviceStorageDeviceAttachment *) attachment didEncounterError:(NSError *) error;
```

## Discussion

After the attachment object calls this method, the NBD client is in a nonfunctional state.

## Parameters

- `attachment`: The attachment object calling the delegate method.
- `error`: An [`NSError`](../../Foundation/nserror.md) that describes the nonrecoverable error.

## See Also

### Responding to connectivity changes
- [func attachmentWasConnected(VZNetworkBlockDeviceStorageDeviceAttachment)](./attachmentwasconnected%28_%29.md)
  The method the attachment object calls when the NBD client successfully connects or reconnects with the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkblockdevicestoragedeviceattachmentdelegate/attachment(_:didencountererror:))*