# VZEFIVariableStore.InitializationOptions

**Framework**: Virtualization  
**Kind**: struct  
**Role**: Structure

Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct InitializationOptions
```

```c
enum VZEFIVariableStoreInitializationOptions : NSUInteger;
```

## Topics

### Creating an EFI initialization store
- [init(rawValue: UInt)](./initializationoptions/init%28rawvalue%29.md)
  Creates a new EFI variable store with the specified value.
### Constants that control overwriting
- [static var allowOverwrite: VZEFIVariableStore.InitializationOptions](./initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the framework can overwrite the EFI variable store.
- [static var allowOverwrite: VZEFIVariableStore.InitializationOptions](./initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the framework can overwrite the EFI variable store.

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

## See Also

### Creating the variable store
- [init(creatingVariableStoreAt: URL, options: VZEFIVariableStore.InitializationOptions) throws](./init%28creatingvariablestoreat,options%29.md)
  Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.
- [init(url: URL)](./init%28url%29-83pcn.md)
  Initialize the variable store from the URL of an existing file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/initializationoptions)*