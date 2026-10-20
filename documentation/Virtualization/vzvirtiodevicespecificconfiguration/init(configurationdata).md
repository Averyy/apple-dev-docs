# init(configurationData:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initializes a Virtio device specific configuration object with the configuration data you provide

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(configurationData: Data)
```

```objc
- (instancetype) initWithConfigurationData:(NSData *) configurationData;
```

## Parameters

- `configurationData`: The device-specific configuration that you provide serialized into an [`NSData`](../../Foundation/nsdata.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiodevicespecificconfiguration/init(configurationdata:))*