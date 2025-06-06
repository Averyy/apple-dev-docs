# VZLinuxRosettaAvailability.notSupported

**Framework**: Virtualization  
**Kind**: case

The current hardware or software configuration doesn’t support Rosetta.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case notSupported
```

#### Discussion

This error can occur if the host’s version of macOS doesn’t support Rosetta, such as macOS 12 or earlier, or if the underlying Mac computer doesn’t support Rosetta, such as an Intel-based Mac computer.

## See Also

- [VZLinuxRosettaAvailability.notInstalled](vzlinuxrosettaavailability/notinstalled.md)
  Rosetta isn’t installed.
- [VZLinuxRosettaAvailability.installed](vzlinuxrosettaavailability/installed.md)
  Rosetta is available on the host system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaavailability/notsupported)*