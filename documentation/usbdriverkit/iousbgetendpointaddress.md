# IOUSBGetEndpointAddress

**Framework**: USBDriverKit  
**Kind**: func

Extracts the direction and number of an endpoint from an endpoint descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t IOUSBGetEndpointAddress(const IOUSBEndpointDescriptor * descriptor);
```

#### Return Value

An unsigned int representing the direction and endpoint number.

#### Discussion

This method parses an endpoint descriptor to determine its address.

## Parameters

- `descriptor`: The descriptor to parse.

## See Also

- [IOUSBGetNextEndpointDescriptor](iousbgetnextendpointdescriptor.md)
  Finds the next endpoint descriptor associated with an interface descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointaddress)*