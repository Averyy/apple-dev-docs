# VZUSBKeyboardConfiguration

**Framework**: Virtualization  
**Kind**: class

A device that defines the configuration for a USB keyboard.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZUSBKeyboardConfiguration
```

#### Overview

A [`VZVirtualMachineView`](vzvirtualmachineview.md) can use this device to send key events to the VM.

## Topics

### Creating a USB keyboard
- [init()](vzusbkeyboardconfiguration/init.md)
  Creates a USB keyboard configuration.

## Relationships

### Inherits From
- [VZKeyboardConfiguration](vzkeyboardconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZKeyboardConfiguration](vzkeyboardconfiguration.md)
  The base class for a configuring a keyboard.
- [class VZMacKeyboardConfiguration](vzmackeyboardconfiguration.md)
  A device that defines the configuration for a Mac keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbkeyboardconfiguration)*