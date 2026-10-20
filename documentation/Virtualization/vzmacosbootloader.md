# VZMacOSBootLoader

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that loads and configures a boot loader for running macOS on Apple silicon as a guest system of your VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacOSBootLoader
```

```objc
@interface VZMacOSBootLoader : VZBootLoader
```

## Mentions

- [Installing macOS on a Virtual Machine](./installing-macos-on-a-virtual-machine.md)

#### Overview

You must use a [`VZMacPlatformConfiguration`](./vzmacplatformconfiguration.md) in conjunction with the macOS boot loader. It’s invalid to use it with any other platform configuration.

## Topics

### Creating a macOS boot loader
- [init()](./vzmacosbootloader/init%28%29.md)
  Creates a macOS boot loader.

## Relationships

### Inherits From
- [VZBootLoader](./vzbootloader.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZMacPlatformConfiguration](./vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [var platform: VZPlatformConfiguration](./vzvirtualmachineconfiguration/platform.md)
  The hardware platform to use.
### Boot images
- [class VZBootLoader](./vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosbootloader)*