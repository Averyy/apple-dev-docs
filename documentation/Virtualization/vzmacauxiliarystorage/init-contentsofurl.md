# init(contentsOfURL:)

**Framework**: Virtualization  
**Kind**: init

Initializes an auxiliary storage object with data from the location at the URL you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(contentsOf URL: URL)
```

#### Discussion

Use this initializer to load the data from an auxiliary storage object stored on the file system. To create a new auxiliary storage object, use [`init(creatingStorageAt:hardwareModel:options:)`](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md).

## Parameters

- `URL`: The URL of the auxiliary storage on the local file system.

## See Also

- [init(url: URL)](vzmacauxiliarystorage/init(url:).md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(creatingStorageAt: URL, hardwareModel: VZMacHardwareModel, options: VZMacAuxiliaryStorage.InitializationOptions) throws](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md)
  Creates an initialized Mac auxiliary storage instance that describes a specific hardware model at a URL you specify.
- [VZMacAuxiliaryStorage.InitializationOptions](vzmacauxiliarystorage/initializationoptions.md)
  Options you can set when creating new auxiliary storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/init(contentsofurl:))*