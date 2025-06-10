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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/initializationoptions)*