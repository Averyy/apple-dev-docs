# init(deviceQueue:delegate:)

**Framework**: Virtualization  
**Kind**: init

Creates a custom Virtio device delegate provider.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init(deviceQueue: dispatch_queue_t, delegate: any VZCustomVirtioDeviceConfigurationDelegate)
```

## Parameters

- `deviceQueue`: The dispatch queue on which the framework synchronizes all device operations.
- `delegate`: The delegate object that implements the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegateprovider/init(devicequeue:delegate:))*