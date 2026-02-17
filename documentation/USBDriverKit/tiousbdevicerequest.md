# tIOUSBDeviceRequest

**Framework**: USBDriverKit  
**Kind**: enum

Constants for configuring a device request.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum tIOUSBDeviceRequest : unsigned int;
```

## Topics

### Getting the Device Request Settings
- [kIOUSBDeviceRequestSize](tiousbdevicerequest/kiousbdevicerequestsize.md)
- [kIOUSBDeviceRequestDirectionMask](tiousbdevicerequest/kiousbdevicerequestdirectionmask.md)
- [kIOUSBDeviceRequestDirectionPhase](tiousbdevicerequest/kiousbdevicerequestdirectionphase.md)
- [kIOUSBDeviceRequestDirectionOut](tiousbdevicerequest/kiousbdevicerequestdirectionout.md)
- [kIOUSBDeviceRequestDirectionIn](tiousbdevicerequest/kiousbdevicerequestdirectionin.md)
- [kIOUSBDeviceRequestTypeMask](tiousbdevicerequest/kiousbdevicerequesttypemask.md)
- [kIOUSBDeviceRequestTypePhase](tiousbdevicerequest/kiousbdevicerequesttypephase.md)
- [kIOUSBDeviceRequestTypeStandard](tiousbdevicerequest/kiousbdevicerequesttypestandard.md)
- [kIOUSBDeviceRequestTypeClass](tiousbdevicerequest/kiousbdevicerequesttypeclass.md)
- [kIOUSBDeviceRequestTypeVendor](tiousbdevicerequest/kiousbdevicerequesttypevendor.md)
- [kIOUSBDeviceRequestRecipientMask](tiousbdevicerequest/kiousbdevicerequestrecipientmask.md)
- [kIOUSBDeviceRequestRecipientPhase](tiousbdevicerequest/kiousbdevicerequestrecipientphase.md)
- [kIOUSBDeviceRequestRecipientDevice](tiousbdevicerequest/kiousbdevicerequestrecipientdevice.md)
- [kIOUSBDeviceRequestRecipientInterface](tiousbdevicerequest/kiousbdevicerequestrecipientinterface.md)
- [kIOUSBDeviceRequestRecipientEndpoint](tiousbdevicerequest/kiousbdevicerequestrecipientendpoint.md)
- [kIOUSBDeviceRequestRecipientOther](tiousbdevicerequest/kiousbdevicerequestrecipientother.md)

## See Also

- [Standard Device Requests](standard_device_requests-enum.md)
  Constants for the standard requests you can make to a USB device.
- [IOUSBDeviceRequest](iousbdevicerequest.md)
  A structure that defines a standard device request.
- [IOUSBDeviceRequestSetSELData](iousbdevicerequestsetseldata.md)
  The structure for receiving system exit latency values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/tiousbdevicerequest)*