# customVirtioDeviceWillPause(_:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when a device pauses.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDeviceWillPause(_ device: VZCustomVirtioDevice)
```

#### Discussion

A device is in a paused state when its corresponding [`VZVirtualMachine`](vzvirtualmachine.md) is in a paused state. This happens when you call [`pause()`](vzvirtualmachine/pause().md).

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillpause(_:))*