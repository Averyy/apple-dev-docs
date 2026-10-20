# VZLinuxRosettaAvailability

**Framework**: Virtualization  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the availability and installation status of Rosetta.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum VZLinuxRosettaAvailability
```

```c
enum VZLinuxRosettaAvailability : NSInteger;
```

## Mentions

- [Running Intel Binaries in Linux VMs](./running-intel-binaries-in-linux-vms.md)

## Topics

### Rosetta availability states
- [VZLinuxRosettaAvailability.notSupported](./vzlinuxrosettaavailability/notsupported.md)
  The current hardware or software configuration doesn’t support Rosetta.
- [VZLinuxRosettaAvailability.notInstalled](./vzlinuxrosettaavailability/notinstalled.md)
  Rosetta isn’t installed.
- [VZLinuxRosettaAvailability.installed](./vzlinuxrosettaavailability/installed.md)
  Rosetta is available on the host system.
### Initializers
- [init?(rawValue: Int)](./vzlinuxrosettaavailability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking Rosetta availability
- [class var availability: VZLinuxRosettaAvailability](./vzlinuxrosettadirectoryshare/availability.md)
  A value that indicates the current state of Rosetta’s availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaavailability)*