# IOUSBGetEndpointIntervalMicroframes

**Framework**: USBDriverKit  
**Kind**: func

Extracts the interval of an endpoint descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint32_t IOUSBGetEndpointIntervalMicroframes(uint32_t usbDeviceSpeed, const IOUSBEndpointDescriptor * descriptor);
```

#### Return Value

The endpoint interval in microframes.

#### Discussion

This method parses an endpoint descriptor and returns the service interval in microframes.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The endpoint descriptor to parse.

## See Also

- [IOUSBGetNextEndpointDescriptor](iousbgetnextendpointdescriptor.md)
  Finds the next endpoint descriptor associated with an interface descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointintervalmicroframes)*