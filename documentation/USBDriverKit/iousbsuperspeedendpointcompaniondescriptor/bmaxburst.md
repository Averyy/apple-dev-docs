# bMaxBurst

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of packets the endpoint can send or receive in one burst.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bMaxBurst;
```

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The length of this descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bmAttributes](./bmattributes.md)
  The attributes associated with the endpoint.
- [wBytesPerInterval](./wbytesperinterval.md)
  The total number of bytes this endpoint transfers during each service interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbsuperspeedendpointcompaniondescriptor/bmaxburst)*