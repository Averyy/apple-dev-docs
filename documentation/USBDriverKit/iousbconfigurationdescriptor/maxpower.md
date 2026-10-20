# MaxPower

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The maximum power consumption of the USB device expressed in 2mA units.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t MaxPower;
```

#### Discussion

A value of 50 indicates that the device consumes a maximum of 100mA of current.

## See Also

### Getting the Descriptor Properties
- [bLength](./blength.md)
  The size of the descriptor in bytes.
- [bDescriptorType](./bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](./wtotallength.md)
  The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.
- [bNumInterfaces](./bnuminterfaces.md)
  The number of interfaces this configuration supports.
- [bConfigurationValue](./bconfigurationvalue.md)
  The value to use when selecting this configuration.
- [iConfiguration](./iconfiguration.md)
  The index of the string descriptor that describes this configuration.
- [bmAttributes](./bmattributes.md)
  A bitmask indicating the configuration’s characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbconfigurationdescriptor/maxpower)*