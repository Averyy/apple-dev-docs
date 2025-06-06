# init(attachment:)

**Framework**: Virtualization  
**Kind**: init

Creates a block device configuration object that uses the specified storage medium.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(attachment: VZStorageDeviceAttachment)
```

#### Return Value

A block storage device configuration object to include in your virtual machine’s configuration.

## Parameters

- `attachment`: The attachment object that provides the storage for the device. For example, specify a   object to implement the storage using a local disk image on the host computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioblockdeviceconfiguration/init(attachment:))*