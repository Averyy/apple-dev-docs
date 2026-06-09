# customVirtioDeviceWillReset(_:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when a device resets.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDeviceWillReset(_ device: VZCustomVirtioDevice)
```

#### Discussion

You can initiate a reset by calling the [`requestReset()`](vzcustomvirtiodevice/requestreset().md) method, and the guest driver can also initiate the reset by itself. The framework calls this method when the reset completes for either scenario.

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillreset(_:))*