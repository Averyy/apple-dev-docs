# bmAttributes

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The attributes of the endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bmAttributes;
```

#### Discussion

This field contains the transfer type, synchronization type, and usage type attributes for the endpoint. For a list of possible values, see [Endpoint Attributes](../endpoint_attributes-enum.md).

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The length of the descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bEndpointAddress](./bendpointaddress.md)
  The address of the endpoint.
- [wMaxPacketSize](./wmaxpacketsize.md)
  The maximum packet size that the endpoint supports.
- [bInterval](./binterval.md)
  The interval to use when polling the endpoint for data transfers, specified in frames or microframes depending on the device’s speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbendpointdescriptor/bmattributes)*