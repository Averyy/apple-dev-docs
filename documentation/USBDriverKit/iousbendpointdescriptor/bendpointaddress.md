# bEndpointAddress

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The address of the endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bEndpointAddress;
```

## Discussion

The address includes information about the direction of the endpoint.

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The length of the descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bmAttributes](./bmattributes.md)
  The attributes of the endpoint.
- [wMaxPacketSize](./wmaxpacketsize.md)
  The maximum packet size that the endpoint supports.
- [bInterval](./binterval.md)
  The interval to use when polling the endpoint for data transfers, specified in frames or microframes depending on the device’s speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbendpointdescriptor/bendpointaddress)*