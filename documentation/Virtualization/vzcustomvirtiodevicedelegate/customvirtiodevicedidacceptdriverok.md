# customVirtioDeviceDidAcceptDriverOk(_:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when the device and driver successfully complete Virtio negotiation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDeviceDidAcceptDriverOk(_ device: VZCustomVirtioDevice)
```

#### Discussion

The guest driver sets the status to the value `DRIVER_OK`.

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicedidacceptdriverok(_:))*