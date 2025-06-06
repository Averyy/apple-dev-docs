# VZLinuxRosettaAvailability

**Framework**: Virtualization  
**Kind**: enum

Constants that describe the availability and installation status of Rosetta.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum VZLinuxRosettaAvailability
```

## Mentions

- [Running Intel Binaries in Linux VMs with Rosetta](running-intel-binaries-in-linux-vms-with-rosetta.md)

## Topics

### Rosetta availability states
- [VZLinuxRosettaAvailability.notSupported](vzlinuxrosettaavailability/notsupported.md)
  The current hardware or software configuration doesn’t support Rosetta.
- [VZLinuxRosettaAvailability.notInstalled](vzlinuxrosettaavailability/notinstalled.md)
  Rosetta isn’t installed.
- [VZLinuxRosettaAvailability.installed](vzlinuxrosettaavailability/installed.md)
  Rosetta is available on the host system.
### Initializers
- [init?(rawValue: Int)](vzlinuxrosettaavailability/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class var availability: VZLinuxRosettaAvailability](vzlinuxrosettadirectoryshare/availability.md)
  A value that indicates the current state of Rosetta’s availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaavailability)*