# customVirtioDeviceWillResume(_:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when a device resumes.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDeviceWillResume(_ device: VZCustomVirtioDevice)
```

#### Discussion

A device is in a resumed state when its corresponding [`VZVirtualMachine`](vzvirtualmachine.md) resumes from the paused state. This happens when you call [`resume()`](vzvirtualmachine/resume().md).

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillresume(_:))*