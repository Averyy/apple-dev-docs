# VZMacKeyboardConfiguration

**Framework**: Virtualization  
**Kind**: class

A device that defines the configuration for a Mac keyboard.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZMacKeyboardConfiguration
```

#### Overview

Use this configuration to attach a Mac keyboard configuration to a VM. A [`VZVirtualMachineView`](vzvirtualmachineview.md) can use this device to send key events to the VM, including the Mac-specific key events, such as the Globe key.

## Topics

### Creating a new Mac keyboard configuration
- [init()](vzmackeyboardconfiguration/init.md)
  Creates a new Mac keyboard configuration.

## Relationships

### Inherits From
- [VZKeyboardConfiguration](vzkeyboardconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZKeyboardConfiguration](vzkeyboardconfiguration.md)
  The base class for a configuring a keyboard.
- [class VZUSBKeyboardConfiguration](vzusbkeyboardconfiguration.md)
  A device that defines the configuration for a USB keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmackeyboardconfiguration)*