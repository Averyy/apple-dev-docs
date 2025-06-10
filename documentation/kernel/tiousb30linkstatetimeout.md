# tIOUSB30LinkStateTimeout

**Framework**: Kernel  
**Kind**: tag

Constants for the link state timeout values on USB 3.0 devices.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum tIOUSB30LinkStateTimeout : unsigned int {
    ...
};
```

#### Discussion

For information about these constants, see USB 3.2, 7.5, 7.5.4, 7.5.9, and 7.5.10.

## Topics

### Constants
- [kIOUSB30LinKStateU2RxDetectDelay](tiousb30linkstatetimeout/kiousb30linkstateu2rxdetectdelay.md)
  The USB 2.0 receive detect delay.
- [kIOUSB30LinkStateHotResetActiveTimeout](tiousb30linkstatetimeout/kiousb30linkstatehotresetactivetimeout.md)
  The hot reset active timeout.
- [kIOUSB30LinkStateLoopbackExitTimeout](tiousb30linkstatetimeout/kiousb30linkstateloopbackexittimeout.md)
  The loopback exit timeout.
- [kIOUSB30LinkStatePollingActiveTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollingactivetimeout.md)
  The polling active timeout.
- [kIOUSB30LinkStatePollingConfigurationTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollingconfigurationtimeout.md)
  The polling configuration timeout.
- [kIOUSB30LinkStatePollingDeadline](tiousb30linkstatetimeout/kiousb30linkstatepollingdeadline.md)
  The polling deadline.
- [kIOUSB30LinkStatePollingIdleTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollingidletimeout.md)
  The polling idle timeout.
- [kIOUSB30LinkStatePollingLFPSTimeout](tiousb30linkstatetimeout/kiousb30linkstatepollinglfpstimeout.md)
  The polling LFPS timeout.
- [kIOUSB30LinkStateRecoveryActiveTimeout](tiousb30linkstatetimeout/kiousb30linkstaterecoveryactivetimeout.md)
  The recovery active timeout.
- [kIOUSB30LinkStateRecoveryConfigurationTimeout](tiousb30linkstatetimeout/kiousb30linkstaterecoveryconfigurationtimeout.md)
  The recovery configuration timeout.
- [kIOUSB30LinkStateRecoveryIdleTimeout](tiousb30linkstatetimeout/kiousb30linkstaterecoveryidletimeout.md)
  The recovery idle timeout.
- [kIOUSB30LinkStateRxDetectQuietTimeout](tiousb30linkstatetimeout/kiousb30linkstaterxdetectquiettimeout.md)
  The receive detect quiet timeout.
- [kIOUSB30LinkStateSSInactiveQuietTimeout](tiousb30linkstatetimeout/kiousb30linkstatessinactivequiettimeout.md)
  The SuperSpeed inactive quiet timeout.
- [kIOUSB30LinkStateSSResumeDeadline](tiousb30linkstatetimeout/kiousb30linkstatessresumedeadline.md)
  The SuperSpeed resume deadline.
- [kIOUSB30LinkStateU0LTimeout](tiousb30linkstatetimeout/kiousb30linkstateu0ltimeout.md)
  The U0L timeout.
- [kIOUSB30LinkStateU0RecoveryTimeout](tiousb30linkstatetimeout/kiousb30linkstateu0recoverytimeout.md)
  The U0 recovery timeout.
- [kIOUSB30LinkStateU1NoLFPSResponseTimeout](tiousb30linkstatetimeout/kiousb30linkstateu1nolfpsresponsetimeout.md)
  The U1 no LFPS response timeout.
- [kIOUSB30LinkStateU1PingTimeout](tiousb30linkstatetimeout/kiousb30linkstateu1pingtimeout.md)
  The U1 ping timeout.
- [kIOUSB30LinkStateU2NoLFPSResponseTimeout](tiousb30linkstatetimeout/kiousb30linkstateu2nolfpsresponsetimeout.md)
  The U2 no LFPS response timeout.
- [kIOUSB30LinkStateU3NoLFPSResponseTimeout](tiousb30linkstatetimeout/kiousb30linkstateu3nolfpsresponsetimeout.md)
  The U3 no LFPS response timeout.
- [kIOUSB30LinkStateU3RxDetectDelay](tiousb30linkstatetimeout/kiousb30linkstateu3rxdetectdelay.md)
  The U3 receive detect delay.
- [kIOUSB30LinkStateU3WakeupRetryDelay](tiousb30linkstatetimeout/kiousb30linkstateu3wakeupretrydelay.md)
  The U3 wakeup retry delay.
- [kIOUSB30LinkStateHotResetDeadline](tiousb30linkstatetimeout/kiousb30linkstatehotresetdeadline.md)
- [kIOUSB30LinkStateHotResetExitTimeout](tiousb30linkstatetimeout/kiousb30linkstatehotresetexittimeout.md)
- [kIOUSB30LinkStateRecoveryDeadline](tiousb30linkstatetimeout/kiousb30linkstaterecoverydeadline.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/tiousb30linkstatetimeout)*