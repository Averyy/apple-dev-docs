# init(creatingVariableStoreAt:options:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a new EFI variable store at specified the URL on the filesystem, initialization options, and error-return variable.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(creatingVariableStoreAt URL: URL, options: VZEFIVariableStore.InitializationOptions = []) throws
```

```objc
- (instancetype) initCreatingVariableStoreAtURL:(NSURL *) URL options:(VZEFIVariableStoreInitializationOptions) options error:(NSError **) error;
```

## Parameters

- `URL`: A URL that specifies the location on disk at which to store the EFI information.
- `options`: An array of possible [`VZEFIVariableStore.InitializationOptions`](./initializationoptions.md).

## See Also

### Creating the variable store
- [init(url: URL)](./init%28url%29-83pcn.md)
  Initialize the variable store from the URL of an existing file.
- [VZEFIVariableStore.InitializationOptions](./initializationoptions.md)
  Constants that describe the options available when creating a new Extensible Firmware Interface (EFI) variable store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/init(creatingvariablestoreat:options:))*