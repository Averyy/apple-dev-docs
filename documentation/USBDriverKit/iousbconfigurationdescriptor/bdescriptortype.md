# bDescriptorType

**Framework**: USBDriverKit  
**Kind**: property

The type of the descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t bDescriptorType;
```

#### Discussion

The value in this field is always [`kIOUSBDescriptorTypeConfiguration`](tiousbdescriptortype/kiousbdescriptortypeconfiguration.md).

## See Also

- [bLength](iousbconfigurationdescriptor/blength.md)
  The size of the descriptor in bytes.
- [wTotalLength](iousbconfigurationdescriptor/wtotallength.md)
  The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbconfigurationdescriptor/bdescriptortype)*