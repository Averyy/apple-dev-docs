# init(contentsOfURL:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initializes an auxiliary storage object with data from the location at the URL you provide.

**Availability**:
- macOS 12.0+ - Deprecated in 27.2

## Declaration

```swift
init(contentsOfURL URL: URL)
```

## Discussion

Use this initializer to load the data from an auxiliary storage object stored on the file system. To create a new auxiliary storage object, use [`init(creatingStorageAt:hardwareModel:options:)`](./init%28creatingstorageat,hardwaremodel,options%29.md).

## Parameters

- `URL`: The URL of the auxiliary storage on the local file system.

## See Also

### Creating the auxiliary storage
- [init(url: URL)](./init%28url%29-68cz.md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(creatingStorageAt: URL, hardwareModel: VZMacHardwareModel, options: VZMacAuxiliaryStorage.InitializationOptions) throws](./init%28creatingstorageat,hardwaremodel,options%29.md)
  Creates an initialized Mac auxiliary storage instance that describes a specific hardware model at a URL you specify.
- [VZMacAuxiliaryStorage.InitializationOptions](./initializationoptions.md)
  Options you can set when creating new auxiliary storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/init(contentsofurl:))*