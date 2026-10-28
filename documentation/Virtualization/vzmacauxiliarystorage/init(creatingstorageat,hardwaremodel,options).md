# init(creatingStorageAt:hardwareModel:options:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates an initialized Mac auxiliary storage instance that describes a specific hardware model at a URL you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(creatingStorageAt URL: URL, hardwareModel: VZMacHardwareModel, options: VZMacAuxiliaryStorage.InitializationOptions = []) throws
```

```objc
- (instancetype) initCreatingStorageAtURL:(NSURL *) URL hardwareModel:(VZMacHardwareModel *) hardwareModel options:(VZMacAuxiliaryStorageInitializationOptions) options error:(NSError **) error;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

## Return Value

Returns a newly initialized `VZMacAuxiliaryStorage` object on success or `nil` if there was an error. On failure,  `error` contains the `NSError` that describes reason for the failure.

## Discussion

Use this method to create a new auxiliary storage object that describes a specific hardware model. To restore data from a previously saved existing auxiliary storage object, use [`init(contentsOfURL:)`](./init%28contentsofurl%29.md).

## Parameters

- `URL`: The `URL` to write the auxiliary storage to on the local file system.
- `hardwareModel`: The [`VZMacHardwareModel`](../vzmachardwaremodel.md) model to use. The auxiliary storage can have different layouts for different hardware models.
- `options`: Initialization options from the available [`VZMacAuxiliaryStorage.InitializationOptions`](./initializationoptions.md).

## See Also

### Creating the auxiliary storage
- [init(contentsOfURL: URL)](./init%28contentsofurl%29.md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(url: URL)](./init%28url%29-68cz.md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [VZMacAuxiliaryStorage.InitializationOptions](./initializationoptions.md)
  Options you can set when creating new auxiliary storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:))*