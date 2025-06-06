# IOUSBSuperSpeedEndpointCompanionDescriptor

**Framework**: USBDriverKit  
**Kind**: struct

The descriptor for a SuperSpeed USB Endpoint Companion.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBSuperSpeedEndpointCompanionDescriptor;
```

#### Overview

For more information about this descriptor type, see section 9.6.7 of the USB 3.1 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Accessing the Descriptor Properties
- [bLength](iousbsuperspeedendpointcompaniondescriptor/blength.md)
  The length of this descriptor in bytes.
- [bDescriptorType](iousbsuperspeedendpointcompaniondescriptor/bdescriptortype.md)
  The type of the descriptor.
- [bMaxBurst](iousbsuperspeedendpointcompaniondescriptor/bmaxburst.md)
  The maximum number of packets the endpoint can send or receive in one burst.
- [bmAttributes](iousbsuperspeedendpointcompaniondescriptor/bmattributes.md)
  The attributes associated with the endpoint.
- [wBytesPerInterval](iousbsuperspeedendpointcompaniondescriptor/wbytesperinterval.md)
  The total number of bytes this endpoint transfers during each service interval.

## See Also

- [IOUSBEndpointDescriptor](iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbsuperspeedendpointcompaniondescriptor)*