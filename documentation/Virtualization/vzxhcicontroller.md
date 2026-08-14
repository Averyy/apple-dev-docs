# VZXHCIController

**Framework**: Virtualization  
**Kind**: class

A class that represents a USB Extensible Host Controller Interface (XHCI) controller in a VM.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZXHCIController
```

#### Overview

Don’t create `VZXHCIController` objects directly. Instead, you create a `VZXHCIController` object at runtime though the [`usbControllers`](vzvirtualmachineconfiguration/usbcontrollers.md) property of the [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object by populating it with [`VZXHCIControllerConfiguration`](vzxhcicontrollerconfiguration.md) objects.

## Relationships

### Inherits From
- [VZUSBController](vzusbcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZUSBController](vzusbcontroller.md)
  A class that represents a USB controller in a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzxhcicontroller)*