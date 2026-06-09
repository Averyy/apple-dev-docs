# customVirtioDeviceWillStop(_:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when a device will be stopped.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDeviceWillStop(_ device: VZCustomVirtioDevice)
```

#### Discussion

A device is in a stopped state when its corresponding [`VZVirtualMachine`](vzvirtualmachine.md) has stopped. This can happen when the guest performs a shutdown operation itself,  or when you call [`requestStop()`](vzvirtualmachine/requeststop().md).

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillstop(_:))*