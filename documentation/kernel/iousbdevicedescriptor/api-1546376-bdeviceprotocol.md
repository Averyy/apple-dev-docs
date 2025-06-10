# bDeviceProtocol

**Framework**: Kernel  
**Kind**: structp

The protocol that the device supports.

**Availability**:
- macOS 10.0+

## Declaration

```swift
uint8_t bDeviceProtocol;
```

## See Also

- [bLength](iousbdevicedescriptor/1546302-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbdevicedescriptor/1545902-bdescriptortype.md)
  The type of the descriptor.
- [bcdUSB](iousbdevicedescriptor/1546010-bcdusb.md)
  The USB specification version number that the device is compliant with.
- [bDeviceClass](iousbdevicedescriptor/1546557-bdeviceclass.md)
  The class code indicating the behavior of this device.
- [bDeviceSubClass](iousbdevicedescriptor/1546530-bdevicesubclass.md)
  The subclass code that further defines the behavior of this device.
- [bMaxPacketSize0](iousbdevicedescriptor/1546126-bmaxpacketsize0.md)
  An exponent value that specifies the maximum packet size for endpoint `0`.
- [idVendor](iousbdevicedescriptor/1546331-idvendor.md)
  The ID of the device’s manufacturer.
- [idProduct](iousbdevicedescriptor/1546261-idproduct.md)
  The product ID that the manufacturer assigns.
- [bcdDevice](iousbdevicedescriptor/1546251-bcddevice.md)
  The device release number as a binary-coded decimal.
- [iManufacturer](iousbdevicedescriptor/1546249-imanufacturer.md)
  The index of the string descriptor that describes the manufacturer.
- [iProduct](iousbdevicedescriptor/1546566-iproduct.md)
  The index of the string descriptor that describes the product.
- [iSerialNumber](iousbdevicedescriptor/1545940-iserialnumber.md)
  The index of the string descriptor that describes the device’s serial number.
- [bNumConfigurations](iousbdevicedescriptor/1546184-bnumconfigurations.md)
  The number of configurations that the device supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevicedescriptor/1546376-bdeviceprotocol)*