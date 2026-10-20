# VZMacOSConfigurationRequirements

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that describes the parameter constraints required by a specific configuration of macOS.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacOSConfigurationRequirements
```

```objc
@interface VZMacOSConfigurationRequirements : NSObject
```

## Topics

### Configuration Requirements
- [var hardwareModel: VZMacHardwareModel](./vzmacosconfigurationrequirements/hardwaremodel.md)
  The hardware model for this configuration.
- [var minimumSupportedCPUCount: Int](./vzmacosconfigurationrequirements/minimumsupportedcpucount.md)
  The minimum supported number of CPUs for this configuration.
- [var minimumSupportedMemorySize: UInt64](./vzmacosconfigurationrequirements/minimumsupportedmemorysize.md)
  The minimum supported memory size for this configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZMacHardwareModel](./vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
### Installers
- [class VZMacOSInstaller](./vzmacosinstaller.md)
  An object you use to install macOS on the specified virtual machine.
- [class VZMacOSRestoreImage](./vzmacosrestoreimage.md)
  An object that describes a version of macOS to install on to a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosconfigurationrequirements)*