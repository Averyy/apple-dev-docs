# VZEFIVariableStore.InitializationOptions

**Framework**: Virtualization  
**Kind**: struct

Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct InitializationOptions
```

## Topics

### Creating an EFI initialization store
- [init(rawValue: UInt)](vzefivariablestore/initializationoptions/init(rawvalue:).md)
  Creates a new EFI variable store with the specified value.
### Constants that control overwriting
- [static var allowOverwrite: VZEFIVariableStore.InitializationOptions](vzefivariablestore/initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the framework can overwrite the EFI variable store.
- [static var allowOverwrite: VZEFIVariableStore.InitializationOptions](vzefivariablestore/initializationoptions/allowoverwrite.md)
  A Boolean value that indicates whether the framework can overwrite the EFI variable store.

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

## See Also

- [init(creatingVariableStoreAt: URL, options: VZEFIVariableStore.InitializationOptions) throws](vzefivariablestore/init(creatingvariablestoreat:options:).md)
  Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.
- [init(url: URL)](vzefivariablestore/init(url:)-83pcn.md)
  Initialize the variable store from the URL of an existing file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/initializationoptions)*