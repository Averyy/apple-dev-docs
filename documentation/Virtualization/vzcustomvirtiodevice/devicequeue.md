# deviceQueue

**Framework**: Virtualization  
**Kind**: property

The dispatch queue this device uses.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var deviceQueue: dispatch_queue_t { get }
```

#### Discussion

The framework performs all operations on `VZCustomVirtioDevice` and [`VZCustomVirtioDeviceDelegate`](vzcustomvirtiodevicedelegate.md) on this serial queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/devicequeue)*