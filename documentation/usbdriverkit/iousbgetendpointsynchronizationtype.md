# IOUSBGetEndpointSynchronizationType

**Framework**: USBDriverKit  
**Kind**: func

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t IOUSBGetEndpointSynchronizationType(const IOUSBEndpointDescriptor * descriptor);
```

#### Return Value

tEndpointSynchronizationType indicating the type found.

#### Discussion

This method parses an endpoint descriptor to determine its synchronization type. Only Isochronous endpoints have non-zero synchronization types

## Parameters

- `descriptor`: The descriptor to parse

## See Also

- [IOUSBGetEndpointUsageType](iousbgetendpointusagetype.md)
- [IOUSBGetPlatformCapabilityDescriptorWithUUID](iousbgetplatformcapabilitydescriptorwithuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointsynchronizationtype)*