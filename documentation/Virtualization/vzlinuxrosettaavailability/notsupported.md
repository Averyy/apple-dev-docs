# VZLinuxRosettaAvailability.notSupported

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

The current hardware or software configuration doesn’t support Rosetta.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case notSupported
```

```c
VZLinuxRosettaAvailabilityNotSupported
```

## Discussion

This error can occur if the host’s version of macOS doesn’t support Rosetta, such as macOS 12 or earlier, or if the underlying Mac computer doesn’t support Rosetta, such as an Intel-based Mac computer.

## See Also

### Rosetta availability states
- [VZLinuxRosettaAvailability.notInstalled](./notinstalled.md)
  Rosetta isn’t installed.
- [VZLinuxRosettaAvailability.installed](./installed.md)
  Rosetta is available on the host system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettaavailability/notsupported)*