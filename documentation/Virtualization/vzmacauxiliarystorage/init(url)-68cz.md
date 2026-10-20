# init(url:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initializes an auxiliary storage object with data from the location at the URL you provide.

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

- `URL`: The URL of the auxiliary storage on the local file system.

## See Also

### Creating the auxiliary storage
- [init(contentsOfURL: URL)](./init%28contentsofurl%29.md)
  Initializes an auxiliary storage object with data from the location at the URL you provide.
- [init(creatingStorageAt: URL, hardwareModel: VZMacHardwareModel, options: VZMacAuxiliaryStorage.InitializationOptions) throws](./init%28creatingstorageat,hardwaremodel,options%29.md)
  Creates an initialized Mac auxiliary storage instance that describes a specific hardware model at a URL you specify.
- [VZMacAuxiliaryStorage.InitializationOptions](./initializationoptions.md)
  Options you can set when creating new auxiliary storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacauxiliarystorage/init(url:)-68cz)*