# init(url:)

**Framework**: Virtualization  
**Kind**: init

Initialize the variable store from the URL of an existing file.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(url URL: URL)
```

## Parameters

- `URL`: The URL of the location on disk that contains the stored EFI information.

## See Also

- [init(creatingVariableStoreAt: URL, options: VZEFIVariableStore.InitializationOptions) throws](vzefivariablestore/init(creatingvariablestoreat:options:).md)
  Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.
- [VZEFIVariableStore.InitializationOptions](vzefivariablestore/initializationoptions.md)
  Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/init(url:))*