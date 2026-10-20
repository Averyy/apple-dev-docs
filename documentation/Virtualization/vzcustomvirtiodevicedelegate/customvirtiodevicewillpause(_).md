# customVirtioDeviceWillPause(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when a device pauses.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func customVirtioDeviceWillPause(_ device: VZCustomVirtioDevice)
```

```objc
- (void) customVirtioDeviceWillPause:(VZCustomVirtioDevice *) device;
```

#### Discussion

A device is in a paused state when its corresponding [`VZVirtualMachine`](../vzvirtualmachine.md) is in a paused state. This happens when you call [`pause()`](../vzvirtualmachine/pause%28%29.md).

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillpause(_:))*