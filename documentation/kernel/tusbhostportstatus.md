# tUSBHostPortStatus

**Framework**: Kernel  
**Kind**: tag

Constants for the USB host port status.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum tUSBHostPortStatus : unsigned int {
    ...
};
```

## Topics

### Constants
- [kUSBHostPortStatusConnectedSpeedFull](tusbhostportstatus/kusbhostportstatusconnectedspeedfull.md)
  The full connected speed.
- [kUSBHostPortStatusConnectedSpeedHigh](tusbhostportstatus/kusbhostportstatusconnectedspeedhigh.md)
  The high connected speed.
- [kUSBHostPortStatusConnectedSpeedLow](tusbhostportstatus/kusbhostportstatusconnectedspeedlow.md)
  The low connected speed.
- [kUSBHostPortStatusConnectedSpeedMask](tusbhostportstatus/kusbhostportstatusconnectedspeedmask.md)
  The connected speed mask.
- [kUSBHostPortStatusConnectedSpeedNone](tusbhostportstatus/kusbhostportstatusconnectedspeednone.md)
  No connected speed.
- [kUSBHostPortStatusConnectedSpeedPhase](tusbhostportstatus/kusbhostportstatusconnectedspeedphase.md)
  The connected speed phase.
- [kUSBHostPortStatusConnectedSpeedSuper](tusbhostportstatus/kusbhostportstatusconnectedspeedsuper.md)
  The SuperSpeed connected speed.
- [kUSBHostPortStatusEnabled](tusbhostportstatus/kusbhostportstatusenabled.md)
  The port status enabled value.
- [kUSBHostPortStatusOvercurrent](tusbhostportstatus/kusbhostportstatusovercurrent.md)
  The port status overcurrent.
- [kUSBHostPortStatusPortTypeAccessory](tusbhostportstatus/kusbhostportstatusporttypeaccessory.md)
  The accessory port type.
- [kUSBHostPortStatusPortTypeCaptive](tusbhostportstatus/kusbhostportstatusporttypecaptive.md)
  The captive port type.
- [kUSBHostPortStatusPortTypeInternal](tusbhostportstatus/kusbhostportstatusporttypeinternal.md)
  The internal port type.
- [kUSBHostPortStatusPortTypeMask](tusbhostportstatus/kusbhostportstatusporttypemask.md)
  The port type mask.
- [kUSBHostPortStatusPortTypePhase](tusbhostportstatus/kusbhostportstatusporttypephase.md)
  The port type phase.
- [kUSBHostPortStatusPortTypeReserved](tusbhostportstatus/kusbhostportstatusporttypereserved.md)
  The reserved port type.
- [kUSBHostPortStatusPortTypeStandard](tusbhostportstatus/kusbhostportstatusporttypestandard.md)
  The standard port type.
- [kUSBHostPortStatusResetting](tusbhostportstatus/kusbhostportstatusresetting.md)
  The resetting port status.
- [kUSBHostPortStatusSuspended](tusbhostportstatus/kusbhostportstatussuspended.md)
  The suspended port status.
- [kUSBHostPortStatusTestMode](tusbhostportstatus/kusbhostportstatustestmode.md)
  The test mode port status.
- [kUSBHostPortStatusConnectedSpeedSuperPlus](tusbhostportstatus/kusbhostportstatusconnectedspeedsuperplus.md)
  The SuperSpeedPlus connected speed.
- [kUSBHostPortStatusConnectedSpeedSuperPlusBy2](tusbhostportstatus/kusbhostportstatusconnectedspeedsuperplusby2.md)
  The SuperSpeedPlus By 2 connected speed.

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
- [IOUSBLowLatencyIsocStruct](iousblowlatencyisocstruct.md)
  An internal structure to pass parameters between IOUSBLib and UserClient.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/tusbhostportstatus)*