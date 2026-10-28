# IOUSBGetEndpointSynchronizationType

**Framework**: USBDriverKit  
**Kind**: func  
**Role**: Function

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t IOUSBGetEndpointSynchronizationType(const IOUSBEndpointDescriptor *descriptor);
```

## Return Value

tEndpointSynchronizationType indicating the type found.

## Discussion

Extract the synchronization type of an  endpoint from an endpoint descriptor

This method parses an endpoint descriptor to determine its synchronization type. Only Isochronous endpoints have non-zero synchronization types

## Parameters

- `descriptor`: The descriptor to parse

## See Also

### Functions
- [IOUSBGetEndpointUsageType](./iousbgetendpointusagetype.md)
- [IOUSBGetPlatformCapabilityDescriptorWithUUID](./iousbgetplatformcapabilitydescriptorwithuuid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointsynchronizationtype)*