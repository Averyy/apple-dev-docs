# init(creatingVariableStoreAt:options:)

**Framework**: Virtualization  
**Kind**: init

Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(creatingVariableStoreAt URL: URL, options: VZEFIVariableStore.InitializationOptions = []) throws
```

## Parameters

- `URL`: A URL that specifies the location on disk at which to store the EFI information.
- `options`: An array of possible  .

## See Also

- [init(url: URL)](vzefivariablestore/init(url:).md)
  Initialize the variable store from the URL of an existing file.
- [VZEFIVariableStore.InitializationOptions](vzefivariablestore/initializationoptions.md)
  Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/init(creatingvariablestoreat:options:))*