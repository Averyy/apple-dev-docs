# VZMacOSConfigurationRequirements

**Framework**: Virtualization  
**Kind**: class

An object that describes the parameter constraints required by a specific configuration of macOS.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZMacOSConfigurationRequirements
```

## Topics

### Configuration Requirements
- [var hardwareModel: VZMacHardwareModel](vzmacosconfigurationrequirements/hardwaremodel.md)
  The hardware model for this configuration.
- [var minimumSupportedCPUCount: Int](vzmacosconfigurationrequirements/minimumsupportedcpucount.md)
  The minimum supported number of CPUs for this configuration.
- [var minimumSupportedMemorySize: UInt64](vzmacosconfigurationrequirements/minimumsupportedmemorysize.md)
  The minimum supported memory size for this configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZMacHardwareModel](vzmachardwaremodel.md)
  A specification for the hardware elements and configurations present in a particular Mac hardware model.
- [class VZMacOSInstaller](vzmacosinstaller.md)
  An object you use to install macOS on the specified virtual machine.
- [class VZMacOSRestoreImage](vzmacosrestoreimage.md)
  An object that describes a version of macOS to install on to a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosconfigurationrequirements)*