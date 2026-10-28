# VZUSBKeyboardConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A device that defines the configuration for a USB keyboard.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZUSBKeyboardConfiguration
```

```objc
@interface VZUSBKeyboardConfiguration : VZKeyboardConfiguration
```

## Overview

A [`VZVirtualMachineView`](./vzvirtualmachineview.md) can use this device to send key events to the VM.

## Topics

### Creating a USB keyboard
- [init()](./vzusbkeyboardconfiguration/init%28%29.md)
  Creates a USB keyboard configuration.

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
- [class VZMacKeyboardConfiguration](./vzmackeyboardconfiguration.md)
  A device that defines the configuration for a Mac keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbkeyboardconfiguration)*