# customVirtioDeviceWillStop(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when a device will be stopped.

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func customVirtioDeviceWillStop(_ device: VZCustomVirtioDevice)
```

```objc
- (void) customVirtioDeviceWillStop:(VZCustomVirtioDevice *) device;
```

## Discussion

A device is in a stopped state when its corresponding [`VZVirtualMachine`](../vzvirtualmachine.md) has stopped. This can happen when the guest performs a shutdown operation itself,  or when you call [`requestStop()`](../vzvirtualmachine/requeststop%28%29.md).

## Parameters

- `device`: The device invoking the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevicewillstop(_:))*