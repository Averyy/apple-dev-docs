# wMaxPacketSize

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The maximum packet size that the endpoint supports.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint16_t wMaxPacketSize;
```

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The length of the descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bEndpointAddress](./bendpointaddress.md)
  The address of the endpoint.
- [bmAttributes](./bmattributes.md)
  The attributes of the endpoint.
- [bInterval](./binterval.md)
  The interval to use when polling the endpoint for data transfers, specified in frames or microframes depending on the device’s speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbendpointdescriptor/wmaxpacketsize)*