# iProduct

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The index of the string descriptor that describes the product.

**Availability**:
- macOS 10.0+

## Declaration

```c
uint8_t iProduct;
```

## See Also

### Getting the Device Properties
- [bLength](./api-1546302-blength.md)
  The size of the descriptor.
- [bDescriptorType](./api-1545902-bdescriptortype.md)
  The type of the descriptor.
- [bcdUSB](./api-1546010-bcdusb.md)
  The USB specification version number that the device is compliant with.
- [bDeviceClass](./api-1546557-bdeviceclass.md)
  The class code indicating the behavior of this device.
- [bDeviceSubClass](./api-1546530-bdevicesubclass.md)
  The subclass code that further defines the behavior of this device.
- [bDeviceProtocol](./api-1546376-bdeviceprotocol.md)
  The protocol that the device supports.
- [bMaxPacketSize0](./api-1546126-bmaxpacketsize0.md)
  An exponent value that specifies the maximum packet size for endpoint `0`.
- [idVendor](./api-1546331-idvendor.md)
  The ID of the device’s manufacturer.
- [idProduct](./api-1546261-idproduct.md)
  The product ID that the manufacturer assigns.
- [bcdDevice](./api-1546251-bcddevice.md)
  The device release number as a binary-coded decimal.
- [iManufacturer](./api-1546249-imanufacturer.md)
  The index of the string descriptor that describes the manufacturer.
- [iSerialNumber](./api-1545940-iserialnumber.md)
  The index of the string descriptor that describes the device’s serial number.
- [bNumConfigurations](./api-1546184-bnumconfigurations.md)
  The number of configurations that the device supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicedescriptor/1546566-iproduct)*