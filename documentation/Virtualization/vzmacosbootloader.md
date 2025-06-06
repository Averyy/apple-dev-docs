# VZMacOSBootLoader

**Framework**: Virtualization  
**Kind**: class

An object that loads and configures a boot loader for running macOS on Apple silicon as a guest system of your VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacOSBootLoader
```

## Mentions

- [Installing macOS on a Virtual Machine](installing-macos-on-a-virtual-machine.md)

#### Overview

You must use a [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) in conjunction with the macOS boot loader. It’s invalid to use it with any other platform configuration.

## Topics

### Creating a macOS boot loader
- [init()](vzmacosbootloader/init.md)
  Creates a macOS boot loader.

## Relationships

### Inherits From
- [VZBootLoader](vzbootloader.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [var platform: VZPlatformConfiguration](vzvirtualmachineconfiguration/platform.md)
  The hardware platform to use.
- [class VZBootLoader](vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosbootloader)*