# customVirtioDeviceWillResume(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when a device resumes.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func customVirtioDeviceWillResume(_ device: VZCustomVirtioDevice)
```

```objc
- (void) customVirtioDeviceWillResume:(VZCustomVirtioDevice *) device;
```

## Discussion

A device is in a resumed state when its corresponding [`VZVirtualMachine`](../vzvirtualmachine.md) resumes from the paused state. This happens when you call [`resume()`](../vzvirtualmachine/resume%28%29.md).

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillresume(_:))*