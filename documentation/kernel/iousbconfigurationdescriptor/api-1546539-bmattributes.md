# bmAttributes

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

A bit mask indicating the configuration’s characteristics.

**Availability**:
- macOS 10.0+

## Declaration

```c
uint8_t bmAttributes;
```

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
- [MaxPower](./api-1545938-maxpower.md)
  The maximum power consumption of the USB device expressed in 2 milliamp units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbconfigurationdescriptor/1546539-bmattributes)*