# bMult

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The mult value for isochronous endpoints.

**Availability**:
- macOS 10.8+

## Declaration

```c
UInt8 bMult;
```

#### Discussion

For SuperSpeed isochronous endpoints, this is the mult value from the SuperSpeed endpoint companion descriptor. For high-speed isochronous and interrupt endpoints, this is bits 11 and 12 of the standard endpoint descriptor.

## See Also

### Getting the Properties
- [bVersion](./api-1546121-bversion.md)
  The version of the structure.
- [bAlternateSetting](./api-1546104-balternatesetting.md)
  The alternative setting for obtaining endpoint and pipe properties.
- [bDirection](./api-1546544-bdirection.md)
  The direction of the endpoint.
- [bEndpointNumber](./api-1546577-bendpointnumber.md)
  The number of the endpoint.
- [bTransferType](./api-1546085-btransfertype.md)
  The transfer type of the endpoint.
- [bUsageType](./api-1545903-busagetype.md)
  The usage type of the endpoint.
- [bSyncType](./api-1546228-bsynctype.md)
  The type for isochronous endpoints.
- [bInterval](./api-1546398-binterval.md)
  The interval field from the standard endpoint descriptor.
- [wMaxPacketSize](./api-1546100-wmaxpacketsize.md)
  The maximum packet size.
- [bMaxBurst](./api-1546213-bmaxburst.md)
  The maximum number of packets the endpoint can send or receive for SuperSpeed endpoints.
- [bMaxStreams](./api-1546220-bmaxstreams.md)
  The maximum number of streams this endpoint supports for SuperSpeed bulk endpoints.
- [wBytesPerInterval](./api-1546060-wbytesperinterval.md)
  The number of bytes per interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbendpointproperties/1546456-bmult)*