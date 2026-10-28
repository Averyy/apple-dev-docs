# MaxPower

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The maximum power consumption of the USB device expressed in 2 milliamp units.

**Availability**:
- macOS 10.0+

## Declaration

```c
uint8_t MaxPower;
```

## Discussion

A value of 50 indicates that the device consumes a maximum of 100 milliamps of current.

## See Also

### Getting the Properties
- [bLength](./api-1546137-blength.md)
  The size of the descriptor.
- [bDescriptorType](./api-1546155-bdescriptortype.md)
  The type of the descriptor.
- [wTotalLength](./api-1546253-wtotallength.md)
  The total length of the descriptor, including the length of all related interface, endpoint, and vendor-specific descriptors.
- [bNumInterfaces](./api-1546162-bnuminterfaces.md)
  The number of interfaces this configuration supports.
- [bConfigurationValue](./api-1546567-bconfigurationvalue.md)
  The value to use when selecting this configuration.
- [iConfiguration](./api-1546218-iconfiguration.md)
  The index of the string descriptor that describes this configuration.
- [bmAttributes](./api-1546539-bmattributes.md)
  A bit mask indicating the configuration’s characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbconfigurationdescriptor/1545938-maxpower)*