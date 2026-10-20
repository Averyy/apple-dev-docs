# VZMacAuxiliaryStorage.InitializationOptions

**Framework**: Virtualization  
**Kind**: struct  
**Role**: Structure

Options you can set when creating new auxiliary storage.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct InitializationOptions
```

```c
enum VZMacAuxiliaryStorageInitializationOptions : NSUInteger;
```

## Topics

### Mac auxiliary storage structure
- [init(rawValue: UInt)](./initializationoptions/init%28rawvalue%29.md)
  Creates a new initialization options structure with the value you supply.
### Controlling overwrites
- [static var allowOverwrite: VZMacAuxiliaryStorage.InitializationOptions](./initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the VM can overwrite an existing auxiliary storage file.
- [static var allowOverwrite: VZMacAuxiliaryStorage.InitializationOptions](./initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the VM can overwrite an existing auxiliary storage file.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/initializationoptions)*