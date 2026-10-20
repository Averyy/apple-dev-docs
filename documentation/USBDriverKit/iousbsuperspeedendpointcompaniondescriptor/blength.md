# bLength

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The length of this descriptor in bytes.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bLength;
```

## See Also

### Accessing the Descriptor Properties
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bMaxBurst](./bmaxburst.md)
  The maximum number of packets the endpoint can send or receive in one burst.
- [bmAttributes](./bmattributes.md)
  The attributes associated with the endpoint.
- [wBytesPerInterval](./wbytesperinterval.md)
  The total number of bytes this endpoint transfers during each service interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbsuperspeedendpointcompaniondescriptor/blength)*