# IOUSBGetEndpointUsageType

**Framework**: USBDriverKit  
**Kind**: func

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t IOUSBGetEndpointUsageType(const IOUSBEndpointDescriptor * descriptor);
```

#### Return Value

tEndpointUsageType indicating the type found.

#### Discussion

This method parses an endpoint descriptor to determine its usage type. Only periodic endpoints have usage types

## Parameters

- `descriptor`: The descriptor to parse

## See Also

- [IOUSBGetEndpointSynchronizationType](iousbgetendpointsynchronizationtype.md)
- [IOUSBGetPlatformCapabilityDescriptorWithUUID](iousbgetplatformcapabilitydescriptorwithuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointusagetype)*