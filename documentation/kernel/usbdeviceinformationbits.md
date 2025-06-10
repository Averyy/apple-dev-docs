# USBDeviceInformationBits

**Framework**: Kernel  
**Kind**: tdef

The state of a USB device.

**Availability**:
- macOS 10.6+

## Declaration

```swift
typedef enum USBDeviceInformationBits USBDeviceInformationBits;
```

#### Discussion

[`GetUSBDeviceInformation`](https://developer.apple.com/documentation/iokit/iousbdeviceinterface942/2977165-getusbdeviceinformation) returns a `unit32_t` value with bits set indicating that a particular state is present in the USB device.

## Topics

### Constants
- [kUSBInformationDeviceIsCaptiveBit](usbdeviceinformationbits/kusbinformationdeviceiscaptivebit.md)
  The USB device has directly attached to its hub and isn’t removable.
- [kUSBInformationDeviceIsAttachedToRootHubBit](usbdeviceinformationbits/kusbinformationdeviceisattachedtoroothubbit.md)
  The USB device has directly attached to the root hub.
- [kUSBInformationDeviceIsInternalBit](usbdeviceinformationbits/kusbinformationdeviceisinternalbit.md)
  The USB device is internal to the enclosure.
- [kUSBInformationDeviceIsConnectedBit](usbdeviceinformationbits/kusbinformationdeviceisconnectedbit.md)
  The system has connected the USB device to its hub.
- [kUSBInformationDeviceIsEnabledBit](usbdeviceinformationbits/kusbinformationdeviceisenabledbit.md)
  The system has enabled the hub port that the USB device attaches to.
- [kUSBInformationDeviceIsSuspendedBit](usbdeviceinformationbits/kusbinformationdeviceissuspendedbit.md)
  The system has suspended the hub port that the USB device attaches to.
- [kUSBInformationDeviceIsInResetBit](usbdeviceinformationbits/kusbinformationdeviceisinresetbit.md)
  The system is resetting the hub port that the USB attaches to.
- [kUSBInformationDeviceOvercurrentBit](usbdeviceinformationbits/kusbinformationdeviceovercurrentbit.md)
  The USB device generated an overcurrent.
- [kUSBInformationDevicePortIsInTestModeBit](usbdeviceinformationbits/kusbinformationdeviceportisintestmodebit.md)
  The hub port that the USB device attaches to is in test mode.
- [kUSBInformationDeviceIsRootHub](usbdeviceinformationbits/kusbinformationdeviceisroothub.md)
  The device is the root hub simulation.
- [kUSBInformationRootHubisBuiltIn](usbdeviceinformationbits/kusbinformationroothubisbuiltin.md)
  The USB root hub is built-in.
- [kUSBInformationDeviceIsRemote](usbdeviceinformationbits/kusbinformationdeviceisremote.md)
  This device attaches to the controller through a remote connection.
- [kUSBInformationDeviceIsAttachedToEnclosure](usbdeviceinformationbits/kusbinformationdeviceisattachedtoenclosure.md)
  The hub port that the USB device connects to has a USB connector on the enclosure.
- [kUSBInformationDeviceIsOnThunderbolt](../iokit/usbdeviceinformationbits/kusbinformationdeviceisonthunderbolt.md)
  The USB device is downstream of a controller that attaches through a Thunderbolt port.
- [kUSBInformationDeviceIsAttachedToEnclosureMask](usbdeviceinformationbits/kusbinformationdeviceisattachedtoenclosuremask.md)
  The mask indicating that the USB device has attached to an enclosure.
- [kUSBInformationDeviceIsAttachedToRootHubMask](usbdeviceinformationbits/kusbinformationdeviceisattachedtoroothubmask.md)
  The mask indicating that the USB device has attached to a root hub.
- [kUSBInformationDeviceIsCaptiveMask](usbdeviceinformationbits/kusbinformationdeviceiscaptivemask.md)
  The mask indicating that the USB device is captive.
- [kUSBInformationDeviceIsConnectedMask](usbdeviceinformationbits/kusbinformationdeviceisconnectedmask.md)
  The mask indicating that the USB device has connected.
- [kUSBInformationDeviceIsEnabledMask](usbdeviceinformationbits/kusbinformationdeviceisenabledmask.md)
  The mask indicating that the USB device is in an enabled state.
- [kUSBInformationDeviceIsInResetMask](usbdeviceinformationbits/kusbinformationdeviceisinresetmask.md)
  The mask indicating that the USB device is in a reset state.
- [kUSBInformationDeviceIsInternalMask](usbdeviceinformationbits/kusbinformationdeviceisinternalmask.md)
  The mask indicating that the USB device is internal.
- [kUSBInformationDeviceIsOnThunderboltBit](usbdeviceinformationbits/kusbinformationdeviceisonthunderboltbit.md)
  The bit indicating that the USB device is on a Thunderbolt port.
- [kUSBInformationDeviceIsOnThunderboltMask](usbdeviceinformationbits/kusbinformationdeviceisonthunderboltmask.md)
  The mask indicating that the USB device is on a Thunderbolt port.
- [kUSBInformationDeviceIsRemoteMask](usbdeviceinformationbits/kusbinformationdeviceisremotemask.md)
  The mask indicating that the USB device is remote.
- [kUSBInformationDeviceIsRootHubMask](usbdeviceinformationbits/kusbinformationdeviceisroothubmask.md)
  The mask indicating that the USB device is a root hub.
- [kUSBInformationDeviceIsSuspendedMask](usbdeviceinformationbits/kusbinformationdeviceissuspendedmask.md)
  The mask indicating that the USB device is in a suspended state.
- [kUSBInformationDeviceOvercurrentMask](usbdeviceinformationbits/kusbinformationdeviceovercurrentmask.md)
  The mask indicating that the USB device is in overcurrent.
- [kUSBInformationDevicePortIsInTestModeMask](usbdeviceinformationbits/kusbinformationdeviceportisintestmodemask.md)
  The mask indicating that the USB device is in test mode.
- [kUSBInformationRootHubIsBuiltInBit](usbdeviceinformationbits/kusbinformationroothubisbuiltinbit.md)
  The bit indicating that the root hub is built-in.
- [kUSBInformationRootHubIsBuiltInMask](usbdeviceinformationbits/kusbinformationroothubisbuiltinmask.md)
  The mask indicating that the root hub is built-in.
- [kUSBInformationRootHubisBuiltInMask](usbdeviceinformationbits/kusbinformationroothubisbuiltinmask-68p.md)
  The mask indicating that the root hub is built-in.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits)*