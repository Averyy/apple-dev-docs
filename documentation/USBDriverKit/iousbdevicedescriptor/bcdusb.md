# bcdUSB

**Framework**: USBDriverKit  
**Kind**: property

The USB specification release number with which the device complies.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint16_t bcdUSB;
```

#### Discussion

The value in this field is formatted as a binary-coded decimal number.

## See Also

- [bLength](iousbdevicedescriptor/blength.md)
  The length of the descriptor in bytes.
- [bDescriptorType](iousbdevicedescriptor/bdescriptortype.md)
  The type of the descriptor.
- [bDeviceClass](iousbdevicedescriptor/bdeviceclass.md)
  The class code indicating the behavior of this device.
- [bDeviceSubClass](iousbdevicedescriptor/bdevicesubclass.md)
  The subclass code that further defines the behavior of this device.
- [bDeviceProtocol](iousbdevicedescriptor/bdeviceprotocol.md)
  The protocol that the device supports.
- [bMaxPacketSize0](iousbdevicedescriptor/bmaxpacketsize0.md)
  The maximum packet size for endpoint `0`, specified as an exponent value.
- [idVendor](iousbdevicedescriptor/idvendor.md)
  The ID of the device’s manufacturer.
- [idProduct](iousbdevicedescriptor/idproduct.md)
  The product ID assigned by the manufacturer.
- [bcdDevice](iousbdevicedescriptor/bcddevice.md)
  The release number of the device, specified as a binary-coded decimal number.
- [iManufacturer](iousbdevicedescriptor/imanufacturer.md)
  The index of the string descriptor that describes the manufacturer.
- [iProduct](iousbdevicedescriptor/iproduct.md)
  The index of the string descriptor that describes the product.
- [iSerialNumber](iousbdevicedescriptor/iserialnumber.md)
  The index of the string descriptor that describes the device’s serial number.
- [bNumConfigurations](iousbdevicedescriptor/bnumconfigurations.md)
  The number of configurations that the device supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbdevicedescriptor/bcdusb)*