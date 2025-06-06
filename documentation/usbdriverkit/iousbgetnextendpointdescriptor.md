# IOUSBGetNextEndpointDescriptor

**Framework**: USBDriverKit  
**Kind**: func

Finds the next endpoint descriptor associated with an interface descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBEndpointDescriptor * IOUSBGetNextEndpointDescriptor(const IOUSBConfigurationDescriptor * configurationDescriptor, const IOUSBInterfaceDescriptor * interfaceDescriptor, const IOUSBDescriptorHeader * currentDescriptor);
```

#### Return Value

An endpoint descriptor pointer, or `NULL` if no matching descriptor can be found.

#### Discussion

This method uses `getNextAssociatedDescriptorWithType` to fetch the next endpoint descriptor associated with a specific interface descriptor.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `interfaceDescriptor`: An interface descriptor within the bounds of the configuration descriptor.
- `currentDescriptor`: A descriptor pointer within the bounds of the configuration descriptor, or  .

## See Also

- [IOUSBGetEndpointAddress](iousbgetendpointaddress.md)
  Extracts the direction and number of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointBurstSize](iousbgetendpointburstsize.md)
  Extracts the burst size from endpoint descriptors.
- [IOUSBGetEndpointDirection](iousbgetendpointdirection.md)
  Extracts the direction of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointIntervalEncodedMicroframes](iousbgetendpointintervalencodedmicroframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointIntervalFrames](iousbgetendpointintervalframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointIntervalMicroframes](iousbgetendpointintervalmicroframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointMaxPacketSize](iousbgetendpointmaxpacketsize.md)
  Extracts the maximum packet size from an endpoint descriptor.
- [IOUSBGetEndpointMaxStreams](iousbgetendpointmaxstreams.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointMaxStreamsEncoded](iousbgetendpointmaxstreamsencoded.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointMult](iousbgetendpointmult.md)
  Extracts the mult count from endpoint descriptors.
- [IOUSBGetEndpointNumber](iousbgetendpointnumber.md)
  Extracts the number of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointType](iousbgetendpointtype.md)
  Extracts the type of an endpoint from an endpoint descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetnextendpointdescriptor)*