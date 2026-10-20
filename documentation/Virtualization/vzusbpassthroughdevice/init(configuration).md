# init(configuration:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(configuration: VZUSBPassthroughDeviceConfiguration) throws
```

```objc
- (instancetype) initWithConfiguration:(VZUSBPassthroughDeviceConfiguration *) configuration error:(NSError **) error;
```

#### Return Value

An initialized VZUSBPassthroughDevice on success, or nil on failure.

#### Discussion

Initialize the USB passthrough device.

## Parameters

- `configuration`: The configuration of the USB passthrough device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbpassthroughdevice/init(configuration:))*