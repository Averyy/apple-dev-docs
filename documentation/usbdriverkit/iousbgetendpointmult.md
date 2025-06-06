# IOUSBGetEndpointMult

**Framework**: USBDriverKit  
**Kind**: func

Extracts the mult count from endpoint descriptors.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t IOUSBGetEndpointMult(uint32_t usbDeviceSpeed, const IOUSBEndpointDescriptor * descriptor, const IOUSBSuperSpeedEndpointCompanionDescriptor * companionDescriptor, const IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor * sspCompanionDescriptor);
```

#### Return Value

The mult count.

#### Discussion

This method parses endpoint descriptors to determine mult.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The endpoint descriptor to parse.
- `companionDescriptor`: The companion descriptor to parse, or  .
- `sspCompanionDescriptor`: The SSP companion descriptor to parse, or  .

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
- [IOUSBGetEndpointMaxStreams](iousbgetendpointmaxstreams.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointMaxStreamsEncoded](iousbgetendpointmaxstreamsencoded.md)
  Extracts the number of streams an endpoint supports.
- [IOUSBGetEndpointNumber](iousbgetendpointnumber.md)
  Extracts the number of an endpoint from an endpoint descriptor.
- [IOUSBGetEndpointType](iousbgetendpointtype.md)
  Extracts the type of an endpoint from an endpoint descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointmult)*