# bInterval

**Framework**: USBDriverKit  
**Kind**: property

The interval to use when polling the endpoint for data transfers, specified in frames or microframes depending on the device’s speed.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t bInterval;
```

## See Also

- [bLength](iousbendpointdescriptor/blength.md)
  The length of the descriptor in bytes.
- [bDescriptorType](iousbendpointdescriptor/bdescriptortype.md)
  The type of the descriptor.
- [bEndpointAddress](iousbendpointdescriptor/bendpointaddress.md)
  The address of the endpoint.
- [bmAttributes](iousbendpointdescriptor/bmattributes.md)
  The attributes of the endpoint.
- [wMaxPacketSize](iousbendpointdescriptor/wmaxpacketsize.md)
  The maximum packet size that the endpoint supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbendpointdescriptor/binterval)*