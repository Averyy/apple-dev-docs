# wMaxPacketSize

**Framework**: Kernel  
**Kind**: structp

The maximum packet size.

**Availability**:
- macOS 10.8+

## Declaration

```swift
UInt16 wMaxPacketSize;
```

#### Discussion

The meaning of this value depends on whether [`GetPipePropertiesV3`](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface942/2977226-getpipepropertiesv3) or [`GetEndpointPropertiesV3`](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface942/2977212-getendpointpropertiesv3) uses it.

## See Also

- [bVersion](iousbendpointproperties/1546121-bversion.md)
  The version of the structure.
- [bAlternateSetting](iousbendpointproperties/1546104-balternatesetting.md)
  The alternative setting for obtaining endpoint and pipe properties.
- [bDirection](iousbendpointproperties/1546544-bdirection.md)
  The direction of the endpoint.
- [bEndpointNumber](iousbendpointproperties/1546577-bendpointnumber.md)
  The number of the endpoint.
- [bTransferType](iousbendpointproperties/1546085-btransfertype.md)
  The transfer type of the endpoint.
- [bUsageType](iousbendpointproperties/1545903-busagetype.md)
  The usage type of the endpoint.
- [bSyncType](iousbendpointproperties/1546228-bsynctype.md)
  The type for isochronous endpoints.
- [bInterval](iousbendpointproperties/1546398-binterval.md)
  The interval field from the standard endpoint descriptor.
- [bMaxBurst](iousbendpointproperties/1546213-bmaxburst.md)
  The maximum number of packets the endpoint can send or receive for SuperSpeed endpoints.
- [bMaxStreams](iousbendpointproperties/1546220-bmaxstreams.md)
  The maximum number of streams this endpoint supports for SuperSpeed bulk endpoints.
- [bMult](iousbendpointproperties/1546456-bmult.md)
  The mult value for isochronous endpoints.
- [wBytesPerInterval](iousbendpointproperties/1546060-wbytesperinterval.md)
  The number of bytes per interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbendpointproperties/1546100-wmaxpacketsize)*