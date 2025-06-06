# uuid

**Framework**: Virtualization  
**Kind**: property  
**Required**: Yes

The device’s unique identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var uuid: UUID { get set }
```

#### Discussion

The framework autogenerates the device UUID.

Before restoring the VM, you need to set the device’s UUID to the UUID of the device with the attachment at the time of saving the VM’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbdeviceconfiguration/uuid)*