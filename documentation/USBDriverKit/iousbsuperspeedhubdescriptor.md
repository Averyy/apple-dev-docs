# IOUSBSuperSpeedHubDescriptor

**Framework**: USBDriverKit  
**Kind**: struct  
**Role**: Structure

A structure that defines the descriptor for a Super Speed USB hub.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
struct IOUSBSuperSpeedHubDescriptor;
```

## Overview

For more information about this descriptor type, see section 10.13.2.1 of the USB 3.0 specification at [http://www.usb.org](http://www.usb.org).

## Topics

### Accessing the Descriptor Properties
- [bLength](./iousbsuperspeedhubdescriptor/blength.md)
- [bDescriptorType](./iousbsuperspeedhubdescriptor/bdescriptortype.md)
- [bNumberPorts](./iousbsuperspeedhubdescriptor/bnumberports.md)
- [wHubCharacteristics](./iousbsuperspeedhubdescriptor/whubcharacteristics.md)
- [bPowerOnToPowerGood](./iousbsuperspeedhubdescriptor/bpowerontopowergood.md)
- [bHubControllerCurrent](./iousbsuperspeedhubdescriptor/bhubcontrollercurrent.md)
- [bHubDecodeLatency](./iousbsuperspeedhubdescriptor/bhubdecodelatency.md)
- [wHubDelay](./iousbsuperspeedhubdescriptor/whubdelay.md)
- [deviceRemovable](./iousbsuperspeedhubdescriptor/deviceremovable.md)

## See Also

### USB Descriptors
- [IOUSB20HubDescriptor](./iousb20hubdescriptor.md)
  A structure that defines the descriptor for a USB hub.
- [SuperSpeed Hub Characteristics](./superspeed_hub_characteristics-enum.md)
  Constants for specifying super-speed hub characteristics.
- [UASPipeDescriptor](./uaspipedescriptor.md)
  A structure that defines the Mass Storage Specific UAS pipe usage descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbsuperspeedhubdescriptor)*