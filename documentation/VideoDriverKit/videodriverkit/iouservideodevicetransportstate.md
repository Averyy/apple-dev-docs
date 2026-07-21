# IOUserVideoDeviceTransportState

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoDeviceTransportState : uint64_t;
```

#### Overview

The current transport state of the device.

Device transport state is stopped.  The hardware necessary for IO should be disabled.

Device transport state is prewarmed.  The minimal hardware for IO should be enabled to minimize transition to normal IO operation.

Device transport state is running.  The hardware should be enabled to fully run IO.

## Topics

### Transport states
- [Stopped](videodriverkit/iouservideodevicetransportstate/stopped.md)
- [Prewarmed](videodriverkit/iouservideodevicetransportstate/prewarmed.md)
- [Running](videodriverkit/iouservideodevicetransportstate/running.md)

## See Also

- [GetDeviceTransportState](iouservideoclockdevice/getdevicetransportstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideodevicetransportstate)*