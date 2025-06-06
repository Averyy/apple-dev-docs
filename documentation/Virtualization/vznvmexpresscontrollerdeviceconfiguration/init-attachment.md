# init(attachment:)

**Framework**: Virtualization  
**Kind**: init

Creates a new NVM Express controller configuration with the storage device attachment you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(attachment: VZStorageDeviceAttachment)
```

## Parameters

- `attachment`: The storage device attachment. This defines how the virtualized device operates on the host side.

## See Also

- [class VZDiskImageStorageDeviceAttachment](vzdiskimagestoragedeviceattachment.md)
  A device that stores content in a disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznvmexpresscontrollerdeviceconfiguration/init(attachment:))*