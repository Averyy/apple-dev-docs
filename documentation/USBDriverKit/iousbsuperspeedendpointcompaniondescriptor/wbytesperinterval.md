# wBytesPerInterval

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The total number of bytes this endpoint transfers during each service interval.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint16_t wBytesPerInterval;
```

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The length of this descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bMaxBurst](./bmaxburst.md)
  The maximum number of packets the endpoint can send or receive in one burst.
- [bmAttributes](./bmattributes.md)
  The attributes associated with the endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbsuperspeedendpointcompaniondescriptor/wbytesperinterval)*