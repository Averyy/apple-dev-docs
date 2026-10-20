# init(url:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initialize the variable store from the URL of an existing file.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(url URL: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL;
```

## Parameters

- `URL`: The URL of the location on disk that contains the stored EFI information.

## See Also

### Creating the variable store
- [init(creatingVariableStoreAt: URL, options: VZEFIVariableStore.InitializationOptions) throws](./init%28creatingvariablestoreat,options%29.md)
  Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.
- [VZEFIVariableStore.InitializationOptions](./initializationoptions.md)
  Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/init(url:)-83pcn)*