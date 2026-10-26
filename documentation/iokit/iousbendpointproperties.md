# IOUSBEndpointProperties

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBEndpointProperties {
    ...
} IOUSBEndpointProperties;
```

#### Overview

Structure used with the IOUSBLib GetEndpointPropertiesV3 and GetPipePropertiesV3 API. Most of the fields are taken directly from corresponding Standard Endpoint Descriptor and SuperSpeed Endpoint Companion Descriptor. wBytesPerInterval will be synthesized for High Speed High Bandwidth Isochronous endpoints.

## Topics

### Instance Properties
- [bAlternateSetting](./iousbendpointproperties/api-1425690-balternatesetting.md)
  Used as an input for GetEndpointPropertiesV3. Used as an output for GetPipePropertiesV3
- [bDirection](./iousbendpointproperties/api-1425747-bdirection.md)
  Used as an input for GetEndpointPropertiesV3. Used as an output for GetPipePropertiesV3. One of kUSBIn or kUSBOut.
- [bEndpointNumber](./iousbendpointproperties/api-1426375-bendpointnumber.md)
  Used as an input for GetEndpointPropertiesV3. Used as an output for GetPipePropertiesV3
- [bInterval](./iousbendpointproperties/api-1426099-binterval.md)
  The bInterval field from the Standard Endpoint descriptor.
- [bMaxBurst](./iousbendpointproperties/api-1425566-bmaxburst.md)
  For SuperSpeed endpoints, maximum number of packets the endpoint can send or receive as part of a burst
- [bMaxStreams](./iousbendpointproperties/api-1425739-bmaxstreams.md)
  For SuperSpeed bulk endpoints, maximum number of streams this endpoint supports.
- [bMult](./iousbendpointproperties/api-1426019-bmult.md)
  For SuperSpeed isoc endpoints, this is the mult value from the SuperSpeed Endpoint Companion Descriptor. For High Speed isoc and interrupt endpoints, this is bits 11 and 12 of the Standard Endpoint Descriptor, which represents a similar value.
- [bSyncType](./iousbendpointproperties/api-1425347-bsynctype.md)
  For isoc endpoints only
- [bTransferType](./iousbendpointproperties/api-1426064-btransfertype.md)
  One of kUSBControl, kUSBBulk, kUSBIsoc, or kUSBInterrupt
- [bUsageType](./iousbendpointproperties/api-1425537-busagetype.md)
  For interrupt and isoc endpoints, the usage type. For Bulk endpoints of the UAS Mass Storage Protocol, the pipe ID.
- [bVersion](./iousbendpointproperties/api-1426285-bversion.md)
  Version of the structure. Currently kUSBEndpointPropertiesVersion3. Need to set this when using this structure
- [wBytesPerInterval](./iousbendpointproperties/api-1426234-wbytesperinterval.md)
  For SuperSpeed interrupt and isoc endpoints, this is the wBytesPerInterval from the SuperSpeed Endpoint Companion Descriptor. For High Speed High Bandwidth isoc endpoints, this will be equal to wMaxPacketSize * (bMult+1).
- [wMaxPacketSize](./iousbendpointproperties/api-1426352-wmaxpacketsize.md)
  The meaning of this value depends on whether this is called with GetPipePropertiesV3 or GetEndpointPropertiesV3. See the documentation of those calls for more info.

## See Also

### Related Documentation
- [pseudoSymbol-1807324](pseudoSymbol-1807324)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbendpointproperties)*