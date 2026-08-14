# VZMacAuxiliaryStorage.InitializationOptions

**Framework**: Virtualization  
**Kind**: struct

Options you can set when creating new auxiliary storage.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct InitializationOptions
```

## Topics

### Mac auxiliary storage structure
- [init(rawValue: UInt)](vzmacauxiliarystorage/initializationoptions/init(rawvalue:).md)
  Creates a new initialization options structure with the value you supply.
### Controlling overwrites
- [static var allowOverwrite: VZMacAuxiliaryStorage.InitializationOptions](vzmacauxiliarystorage/initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the VM can overwrite an existing auxiliary storage file.
- [static var allowOverwrite: VZMacAuxiliaryStorage.InitializationOptions](vzmacauxiliarystorage/initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the VM can overwrite an existing auxiliary storage file.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/initializationoptions)*