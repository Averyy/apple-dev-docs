# bInterval

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The interval to use when polling the endpoint for data transfers.

**Availability**:
- macOS 10.0+

## Declaration

```c
uint8_t bInterval;
```

## Discussion

Specify the value in frames or microframes, depending on the device’s speed.

## See Also

### Getting the Properties
- [bLength](./api-1546156-blength.md)
  The size of the descriptor.
- [bDescriptorType](./api-1545995-bdescriptortype.md)
  The type of the descriptor.
- [bEndpointAddress](./api-1546243-bendpointaddress.md)
  The address of the endpoint.
- [bmAttributes](./api-1546048-bmattributes.md)
  The attributes of the endpoint.
- [wMaxPacketSize](./api-1546305-wmaxpacketsize.md)
  The maximum packet size that the endpoint supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbendpointdescriptor/1546209-binterval)*