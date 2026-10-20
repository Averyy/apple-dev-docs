# VZMacKeyboardConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A device that defines the configuration for a Mac keyboard.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class VZMacKeyboardConfiguration
```

```objc
@interface VZMacKeyboardConfiguration : VZKeyboardConfiguration
```

#### Overview

Use this configuration to attach a Mac keyboard configuration to a VM. A [`VZVirtualMachineView`](./vzvirtualmachineview.md) can use this device to send key events to the VM, including the Mac-specific key events, such as the Globe key.

## Topics

### Creating a new Mac keyboard configuration
- [init()](./vzmackeyboardconfiguration/init%28%29.md)
  Creates a new Mac keyboard configuration.

## Relationships

### Inherits From
- [VZKeyboardConfiguration](./vzkeyboardconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Keyboards
- [class VZKeyboardConfiguration](./vzkeyboardconfiguration.md)
  The base class for a configuring a keyboard.
- [class VZUSBKeyboardConfiguration](./vzusbkeyboardconfiguration.md)
  A device that defines the configuration for a USB keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmackeyboardconfiguration)*