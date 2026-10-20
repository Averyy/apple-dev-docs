# IOUSBEndpointProperties

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that holds USB endpoint properties.

**Availability**:
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBEndpointProperties IOUSBEndpointProperties;
```

#### Discussion

Use this structure with the IOUSBLib [`GetEndpointPropertiesV3`](../iokit/iousbinterfaceinterface942/api-2977212-getendpointpropertiesv3.md) and [`GetPipePropertiesV3`](../iokit/iousbinterfaceinterface942/api-2977226-getpipepropertiesv3.md) API. Most of the fields come directly from the corresponding standard endpoint descriptor and SuperSpeed endpoint companion descriptor.

The API synthesizes `wBytesPerInterval` for high-speed high-bandwidth isochronous endpoints.

## Topics

### Getting the Properties
- [bVersion](./iousbendpointproperties/api-1546121-bversion.md)
  The version of the structure.
- [bAlternateSetting](./iousbendpointproperties/api-1546104-balternatesetting.md)
  The alternative setting for obtaining endpoint and pipe properties.
- [bDirection](./iousbendpointproperties/api-1546544-bdirection.md)
  The direction of the endpoint.
- [bEndpointNumber](./iousbendpointproperties/api-1546577-bendpointnumber.md)
  The number of the endpoint.
- [bTransferType](./iousbendpointproperties/api-1546085-btransfertype.md)
  The transfer type of the endpoint.
- [bUsageType](./iousbendpointproperties/api-1545903-busagetype.md)
  The usage type of the endpoint.
- [bSyncType](./iousbendpointproperties/api-1546228-bsynctype.md)
  The type for isochronous endpoints.
- [bInterval](./iousbendpointproperties/api-1546398-binterval.md)
  The interval field from the standard endpoint descriptor.
- [wMaxPacketSize](./iousbendpointproperties/api-1546100-wmaxpacketsize.md)
  The maximum packet size.
- [bMaxBurst](./iousbendpointproperties/api-1546213-bmaxburst.md)
  The maximum number of packets the endpoint can send or receive for SuperSpeed endpoints.
- [bMaxStreams](./iousbendpointproperties/api-1546220-bmaxstreams.md)
  The maximum number of streams this endpoint supports for SuperSpeed bulk endpoints.
- [bMult](./iousbendpointproperties/api-1546456-bmult.md)
  The mult value for isochronous endpoints.
- [wBytesPerInterval](./iousbendpointproperties/api-1546060-wbytesperinterval.md)
  The number of bytes per interval.

## See Also

### Endpoint Descriptors
- [IOUSBEndpointDescriptor](./iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.
- [IOUSBStandardEndpointDescriptors](./iousbstandardendpointdescriptors.md)
  A container for descriptors for a single endpoint.
- [IOUSBEndpointDescriptorPtr](./iousbendpointdescriptorptr.md)
  A pointer to the endpoint descriptor.
- [IOUSBEndpointPropertiesPtr](./iousbendpointpropertiesptr.md)
  A pointer to an endpoint properties object.
- [IOUSBGetEndpointDescriptorOptions](./iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.
### Related Documentation
- [pseudoSymbol-1807324](pseudoSymbol-1807324)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbendpointproperties)*