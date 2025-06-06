# init(url:)

**Framework**: Virtualization  
**Kind**: init

Initializes an auxiliary storage object with data from the location at the URL you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(url URL: URL)
```

## Parameters

- `URL`: The URL of the auxiliary storage on the local file system.

## See Also

- [init(contentsOfURL: URL)](vzmacauxiliarystorage/init(contentsofurl:).md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(creatingStorageAt: URL, hardwareModel: VZMacHardwareModel, options: VZMacAuxiliaryStorage.InitializationOptions) throws](vzmacauxiliarystorage/init(creatingstorageat:hardwaremodel:options:).md)
  Creates an initialized Mac auxiliary storage instance that describes a specific hardware model at a URL you specify.
- [VZMacAuxiliaryStorage.InitializationOptions](vzmacauxiliarystorage/initializationoptions.md)
  Options you can set when creating new auxiliary storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/init(url:))*