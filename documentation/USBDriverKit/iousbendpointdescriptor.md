# IOUSBEndpointDescriptor

**Framework**: USBDriverKit  
**Kind**: struct

The structure for storing an endpoint descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBEndpointDescriptor;
```

#### Overview

For more information about this descriptor type, see section 9.6.6 of the USB 2.0 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Accessing the Descriptor Properties
- [bLength](iousbendpointdescriptor/blength.md)
  The length of the descriptor in bytes.
- [bDescriptorType](iousbendpointdescriptor/bdescriptortype.md)
  The type of the descriptor.
- [bEndpointAddress](iousbendpointdescriptor/bendpointaddress.md)
  The address of the endpoint.
- [bmAttributes](iousbendpointdescriptor/bmattributes.md)
  The attributes of the endpoint.
- [wMaxPacketSize](iousbendpointdescriptor/wmaxpacketsize.md)
  The maximum packet size that the endpoint supports.
- [bInterval](iousbendpointdescriptor/binterval.md)
  The interval to use when polling the endpoint for data transfers, specified in frames or microframes depending on the device’s speed.

## See Also

- [IOUSBSuperSpeedEndpointCompanionDescriptor](iousbsuperspeedendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeed USB Endpoint Companion.
- [IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbsuperspeedplusisochronousendpointcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus Isochronous USB Endpoint Companion.
- [tIOUSBEndpointType](tiousbendpointtype.md)
  Constants describing the types of endpoints.
- [Endpoint Attributes](endpoint_attributes-enum.md)
  Constants for endpoint attributes.
- [SuperSpeed USB Endpoint Descriptor Options](superspeed_usb_endpoint_descript-enum.md)
  Constants for super-speed endpoint attributes.
- [tIOUSBEndpointDirection](tiousbendpointdirection.md)
  The direction of data transfers on an endpoint.
- [tIOUSBEndpointSynchronizationType](tiousbendpointsynchronizationtype.md)
  Constants for the endpoint synchronization types.
- [tIOUSBEndpointUsageType](tiousbendpointusagetype.md)
  Constants for the endpoint usage types.
- [tIOUSBLanguageID](tiousblanguageid.md)
  Constants for the USB language identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbendpointdescriptor)*