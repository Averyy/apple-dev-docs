# requestReset()

**Framework**: Virtualization  
**Kind**: method

A request to reset the device.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func requestReset()
```

#### Discussion

This method initiates a reset from the host by setting `DEVICE_NEEDS_RESET`, and the guest may or may not take action. The guest could also initiate a reset by itself. In both scenarios, the framework calls[`customVirtioDeviceWillReset(_:)`](vzcustomvirtiodevicedelegate/customvirtiodevicewillreset(_:).md) when the device should reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/requestreset())*