# IOUSB20HubDescriptor

**Framework**: USBDriverKit  
**Kind**: struct

A structure that defines the descriptor for a USB hub.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSB20HubDescriptor;
```

#### Overview

For more information about this descriptor type, see section 11.23.2.1 of the USB 2.0 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Accessing the Descriptor Properties
- [bLength](iousb20hubdescriptor/blength.md)
- [bDescriptorType](iousb20hubdescriptor/bdescriptortype.md)
- [bNumberPorts](iousb20hubdescriptor/bnumberports.md)
- [wHubCharacteristics](iousb20hubdescriptor/whubcharacteristics.md)
- [bPowerOnToPowerGood](iousb20hubdescriptor/bpowerontopowergood.md)
- [bHubControllerCurrent](iousb20hubdescriptor/bhubcontrollercurrent.md)
- [deviceRemovable](iousb20hubdescriptor/deviceremovable.md)
- [reserved](iousb20hubdescriptor/reserved.md)

## See Also

- [IOUSBSuperSpeedHubDescriptor](iousbsuperspeedhubdescriptor.md)
  A structure that defines the descriptor for a Super Speed USB hub.
- [SuperSpeed Hub Characteristics](superspeed_hub_characteristics-enum.md)
  Constants for specifying super-speed hub characteristics.
- [UASPipeDescriptor](uaspipedescriptor.md)
  A structure that defines the Mass Storage Specific UAS pipe usage descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousb20hubdescriptor)*