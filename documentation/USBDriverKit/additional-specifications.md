# Additional Specifications

**Framework**: USBDriverKit

Request information from a device and get hardware and timing information.

## Topics

### Device Requests
- [Standard Device Requests](standard_device_requests-enum.md)
  Constants for the standard requests you can make to a USB device.
- [IOUSBDeviceRequest](iousbdevicerequest.md)
  A structure that defines a standard device request.
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
### Hub Port Status Requests
- [IOUSB30HubPortStatusExt](iousb30hubportstatusext.md)
  The structure for getting the port status of a USB 3 hub.
- [tIOUSBDeviceRequestDirectionValue](tiousbdevicerequestdirectionvalue.md)
  Enumerated device request direction values.
- [tIOUSB30HubExtStatus](tiousb30hubextstatus.md)
  Bit masks for getting port status values.
- [tIOUSB30HubPortStatusCode](tiousb30hubportstatuscode.md)
  Constants for the port status type codes.
- [Hub Parameters](hub_parameters-enum.md)
  Constants for hub parameters.
### Device Notifications
- [tIOUSB30DeviceNotificationType](tiousb30devicenotificationtype.md)
  Constants indicating the type of a device notification.
### Electrical Characteristics
- [tIOUSB20BusCurrent](tiousb20buscurrent.md)
  Constants for the available current levels for USB 2.0 devices.
- [tIOUSB30BusCurrent](tiousb30buscurrent.md)
  Constants for the available power levels of USB 3.0 devices.
- [tIOUSBBusVoltage](tiousbbusvoltage.md)
  A constant for the USB bus voltage.
### Timing Parameters
- [tIOUSB30LinkStateTimeout](tiousb30linkstatetimeout.md)
  Constants for the link state timeout values on USB 3.0 devices.
- [tIOUSB30ResetTimeout](tiousb30resettimeout.md)
  Constants for the reset timeout values on USB 3.0 devices.
- [tIOUSB30TimingParameters](tiousb30timingparameters.md)
  Constants for USB 3.0 timing parameters.
- [Timing Parameters](timing_parameters-enum.md)
  Constants for ping response times.

## See Also

- [USB Device Descriptors](usb-device-descriptors.md)
  Determine the capabilities and configuration of a device using descriptors from the USB specification.
- [Registry Property Names](registry-property-names.md)
  Search for specific keys in the device registry.
- [Utilities](utilities.md)
  Manipulate bit structures and convert integers between device- and platform-native formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/additional-specifications)*