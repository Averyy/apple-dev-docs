# VZKeyboardConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a configuring a keyboard.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZKeyboardConfiguration
```

```objc
@interface VZKeyboardConfiguration : NSObject
```

#### Overview

`VZKeyboardConfiguration` defines the abstract interface that defines a virtual keyboard that you connect to a guest operating system. Don’t instantiate `VZKeyboardConfiguration` directly, use one of its subclasses such as [`VZUSBKeyboardConfiguration`](./vzusbkeyboardconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZMacKeyboardConfiguration](./vzmackeyboardconfiguration.md)
- [VZUSBKeyboardConfiguration](./vzusbkeyboardconfiguration.md)
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
- [class VZMacKeyboardConfiguration](./vzmackeyboardconfiguration.md)
  A device that defines the configuration for a Mac keyboard.
- [class VZUSBKeyboardConfiguration](./vzusbkeyboardconfiguration.md)
  A device that defines the configuration for a USB keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzkeyboardconfiguration)*