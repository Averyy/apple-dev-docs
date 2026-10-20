# IOUSBGetEndpointUsageType

**Framework**: USBDriverKit  
**Kind**: func  
**Role**: Function

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t IOUSBGetEndpointUsageType(const IOUSBEndpointDescriptor *descriptor);
```

#### Return Value

tEndpointUsageType indicating the type found.

#### Discussion

Extract the usage type of an endpoint from an endpoint descriptor

This method parses an endpoint descriptor to determine its usage type. Only periodic endpoints have usage types

## Parameters

- `descriptor`: The descriptor to parse

## See Also

### Functions
- [IOUSBGetEndpointSynchronizationType](./iousbgetendpointsynchronizationtype.md)
- [IOUSBGetPlatformCapabilityDescriptorWithUUID](./iousbgetplatformcapabilitydescriptorwithuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointusagetype)*