# IOUSBLowLatencyIsocStruct

**Framework**: Kernel  
**Kind**: tdef

An internal structure to pass parameters between IOUSBLib and UserClient.

**Availability**:
- macOS 10.2+

## Declaration

```swift
typedef struct IOUSBLowLatencyIsocStruct IOUSBLowLatencyIsocStruct;
```

## Topics

### Getting the Properties
- [fBufSize](iousblowlatencyisocstruct/1546373-fbufsize.md)
  The buffer size.
- [fDataBufferCookie](iousblowlatencyisocstruct/1546223-fdatabuffercookie.md)
  The data buffer cookie.
- [fDataBufferOffset](iousblowlatencyisocstruct/1546407-fdatabufferoffset.md)
  The data buffer offset.
- [fFrameListBufferCookie](iousblowlatencyisocstruct/1546295-fframelistbuffercookie.md)
  The frame list buffer cookie.
- [fFrameListBufferOffset](iousblowlatencyisocstruct/1546475-fframelistbufferoffset.md)
  The frame list buffer offset.
- [fNumFrames](iousblowlatencyisocstruct/1545919-fnumframes.md)
  The number of frames.
- [fPipe](iousblowlatencyisocstruct/1546483-fpipe.md)
  The pipe value.
- [fStartFrame](iousblowlatencyisocstruct/1546421-fstartframe.md)
  The start frame.
- [fUpdateFrequency](iousblowlatencyisocstruct/1546046-fupdatefrequency.md)
  The update frequency.

## See Also

- [tIOUSB20BusCurrent](tiousb20buscurrent.md)
  Constants for the available current levels for USB 2.0 devices.
- [tIOUSB30BusCurrent](tiousb30buscurrent.md)
  Constants for the available power levels of USB 3.0 devices.
- [tIOUSB30DeviceNotificationType](tiousb30devicenotificationtype.md)
  Constants indicating the type of a device notification.
- [tIOUSB30HubExtStatus](tiousb30hubextstatus.md)
  Bit masks for getting port status values.
- [tIOUSB30HubPortStatusCode](tiousb30hubportstatuscode.md)
  Constants for the port status type codes.
- [tIOUSB30LinkStateTimeout](tiousb30linkstatetimeout.md)
  Constants for the link state timeout values on USB 3.0 devices.
- [tIOUSB30ResetTimeout](tiousb30resettimeout.md)
  Constants for the reset timeout values on USB 3.0 devices.
- [tIOUSB30TimingParameters](tiousb30timingparameters.md)
  Constants for USB 3.0 timing parameters.
- [tIOUSBBusVoltage](tiousbbusvoltage.md)
  A constant for the USB bus voltage.
- [tIOUSBDeviceCapabilityType](tiousbdevicecapabilitytype.md)
  Constants for the device capability types.
- [tIOUSBDeviceRequest](tiousbdevicerequest.md)
  Constants for configuring a device request.
- [tIOUSBDeviceRequestDirectionValue](tiousbdevicerequestdirectionvalue.md)
  Enumerated device request direction values.
- [tIOUSBDeviceRequestRecipientValue](tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.
- [tIOUSBDeviceRequestTypeValue](tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [tIOUSBEndpointDirection](tiousbendpointdirection.md)
  The direction of data transfers on an endpoint.
- [tIOUSBEndpointSynchronizationType](tiousbendpointsynchronizationtype.md)
  Constants for the endpoint synchronization types.
- [tIOUSBEndpointType](tiousbendpointtype.md)
  Constants describing the types of endpoints.
- [tIOUSBEndpointUsageType](tiousbendpointusagetype.md)
  Constants for the endpoint usage types.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](tiousbhostporttype.md)
  Constants indicating a port’s type.
- [tIOUSBLanguageID](tiousblanguageid.md)
  Constants for the USB language identifiers.
- [tInternalUSBHostConnectionSpeed](tinternalusbhostconnectionspeed.md)
  Constants for the internal USB host connection speed.
- [tUSBHostConnectionSpeed](tusbhostconnectionspeed.md)
  Constants for the USB host connection speed.
- [tUSBHostDeviceAddress](tusbhostdeviceaddress.md)
  The USB host device address.
- [tUSBHostPortStatus](tusbhostportstatus.md)
  Constants for the USB host port status.
- [tUSBHostPortType](tusbhostporttype.md)
  Constants for the USB host port type.
- [IOUSBGetFrameStruct](iousbgetframestruct.md)
  A structure that contains frame information.
- [IOUSBHostIOSourceClientRecord](iousbhostiosourceclientrecord.md)
  The USB host input/output source client record.
- [IOUSBIsocFrame](iousbisocframe.md)
  A structure for encoding information about a single frame in an isochronous transfer.
- [IOUSBIsocStruct](iousbisocstruct.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
- [IOUSBLowLatencyIsocFrame](iousblowlatencyisocframe.md)
  A structure for encoding information about each low-latency isochronous frame.
- [IOUSBKeyboardData](iousbkeyboarddata.md)
  A structure containing USB keyboard data.
- [IOUSBKeyboardDataPtr](iousbkeyboarddataptr.md)
  A pointer to a structure containing USB keyboard data.
- [IOUSBMouseData](iousbmousedata.md)
  A structure containing USB mouse data.
- [IOUSBMouseDataPtr](iousbmousedataptr.md)
  A pointer to a structure containing USB mouse data.
- [IOUSBMatch](iousbmatch.md)
  A structure for matching USB devices.
- [USBClassSpecificDesc](usbclassspecificdesc.md)
  A class-specific descriptor.
- [USBDeviceAddress](usbdeviceaddress.md)
  A USB device address.
- [USBDeviceInformationBits](usbdeviceinformationbits.md)
  The state of a USB device.
- [USBHubClassRequest](usbhubclassrequest.md)
  A structure that provides USB hub requests.
- [USBLowLatencyBufferType](usblowlatencybuffertype.md)
  Specifies which kind of low-latency buffer to create.
- [USBNotificationTypes](usbnotificationtypes.md)
  Defines types of USB notifications.
- [USBPhysicalAddress32](usbphysicaladdress32.md)
  A 32-bit USB physical address.
- [USBPowerRequestTypes](usbpowerrequesttypes.md)
  Specifies the kind of power to reserve.
- [USBReEnumerateOptions](usbreenumerateoptions.md)
  Options for reenumerating a device.
- [USBStatus](usbstatus.md)
  The value of the USB device status.
- [USBStatusPtr](usbstatusptr.md)
  A pointer to a USB status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousblowlatencyisocstruct)*