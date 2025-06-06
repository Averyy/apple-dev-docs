# wTotalLength

**Framework**: USBDriverKit  
**Kind**: property

The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint16_t wTotalLength;
```

## See Also

- [bLength](iousbconfigurationdescriptor/blength.md)
  The size of the descriptor in bytes.
- [bDescriptorType](iousbconfigurationdescriptor/bdescriptortype.md)
  The type of the descriptor.
- [bNumInterfaces](iousbconfigurationdescriptor/bnuminterfaces.md)
  The number of interfaces this configuration supports.
- [bConfigurationValue](iousbconfigurationdescriptor/bconfigurationvalue.md)
  The value to use when selecting this configuration.
- [iConfiguration](iousbconfigurationdescriptor/iconfiguration.md)
  The index of the string descriptor that describes this configuration.
- [bmAttributes](iousbconfigurationdescriptor/bmattributes.md)
  A bitmask indicating the configuration’s characteristics.
- [MaxPower](iousbconfigurationdescriptor/maxpower.md)
  The maximum power consumption of the USB device expressed in 2mA units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbconfigurationdescriptor/wtotallength)*