# VZKeyboardConfiguration

**Framework**: Virtualization  
**Kind**: class

The base class for a configuring a keyboard.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZKeyboardConfiguration
```

#### Overview

`VZKeyboardConfiguration` defines the abstract interface that defines a virtual keyboard that you connect to a guest operating system. Don’t instantiate `VZKeyboardConfiguration` directly, use one of its subclasses such as [`VZUSBKeyboardConfiguration`](vzusbkeyboardconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZMacKeyboardConfiguration](vzmackeyboardconfiguration.md)
- [VZUSBKeyboardConfiguration](vzusbkeyboardconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacKeyboardConfiguration](vzmackeyboardconfiguration.md)
  A device that defines the configuration for a Mac keyboard.
- [class VZUSBKeyboardConfiguration](vzusbkeyboardconfiguration.md)
  A device that defines the configuration for a USB keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzkeyboardconfiguration)*