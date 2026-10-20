# bmAttributes

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The attributes associated with the endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bmAttributes;
```

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The length of this descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [bMaxBurst](./bmaxburst.md)
  The maximum number of packets the endpoint can send or receive in one burst.
- [wBytesPerInterval](./wbytesperinterval.md)
  The total number of bytes this endpoint transfers during each service interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbsuperspeedendpointcompaniondescriptor/bmattributes)*