# IOUSBDeviceRequest

**Framework**: USBDriverKit  
**Kind**: struct

A structure that defines a standard device request.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBDeviceRequest;
```

#### Overview

For information about device requests, see section 9.3 of the USB 2.0 specification at [`http://www.usb.org`](https://developer.apple.comhttp://www.usb.org).

## Topics

### Getting the Request Data
- [bmRequestType](iousbdevicerequest/bmrequesttype.md)
- [bRequest](iousbdevicerequest/brequest.md)
- [wValue](iousbdevicerequest/wvalue.md)
- [wIndex](iousbdevicerequest/windex.md)
- [wLength](iousbdevicerequest/wlength.md)

## See Also

- [Standard Device Requests](standard_device_requests-enum.md)
  Constants for the standard requests you can make to a USB device.
- [IOUSBDeviceRequestSetSELData](iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.
- [tIOUSBDeviceRequest](tiousbdevicerequest.md)
  Constants for configuring a device request.
- [tIOUSBDeviceRequestTypeValue](tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [tIOUSBDeviceRequestRecipientValue](tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.
- [Get Status Options](get_status_options-enum.md)
  Constants for use with get status requests.
- [Suspend Feature Options](suspend_feature_options-enum.md)
  Constants to use when enabling the suspend feature of a device.
- [Link Power Management Capabilities](link_power_management_capabiliti-enum.md)
  Constants for link power management capabilities.
- [Standard Feature Selectors](standard_feature_selectors-enum.md)
  Constants for the standard feature selectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbdevicerequest)*