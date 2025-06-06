# IOUSBGetEndpointMaxStreams

**Framework**: USBDriverKit  
**Kind**: func

Extracts the number of streams an endpoint supports.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint32_t IOUSBGetEndpointMaxStreams(uint32_t usbDeviceSpeed, const IOUSBEndpointDescriptor * descriptor, const IOUSBSuperSpeedEndpointCompanionDescriptor * companionDescriptor);
```

#### Return Value

The number of streams.

#### Discussion

This method parses endpoint descriptors and returns the number of streams supported.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The endpoint descriptor to parse.
- `companionDescriptor`: The companion descriptor to parse.

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
- [IOUSBGetEndpointIntervalMicroframes](iousbgetendpointintervalmicroframes.md)
  Extracts the interval of an endpoint descriptor.
- [IOUSBGetEndpointMaxPacketSize](iousbgetendpointmaxpacketsize.md)
  Extracts the maximum packet size from an endpoint descriptor.
- [IOUSBGetEndpointMaxStreamsEncoded](iousbgetendpointmaxstreamsencoded.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointMult](iousbgetendpointmult.md)
  Extracts the mult count from endpoint descriptors.
- [IOUSBGetEndpointNumber](iousbgetendpointnumber.md)
  Extracts the number of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointType](iousbgetendpointtype.md)
  Extracts the type of an endpoint from an endpoint descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointmaxstreams)*