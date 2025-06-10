# GetInterfaceClass

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual UInt8 GetInterfaceClass();
```

#### Return_value

the interface class

#### Overview

returns the class code for this interface (assigned by the USB) a value of zero is reserved if the value is FFh, the interface class is vendor-specific all other values are reserved for assignment by the USB

## See Also

- [DeviceRequest(IOUSBDevRequest *, IOUSBCompletion *)](iousbinterface/1809501-devicerequest.md)
  Sends a control request to the default control pipe in the device (pipe zero)
- [DeviceRequest(IOUSBDevRequestDesc *, IOUSBCompletion *)](iousbinterface/1809505-devicerequest.md)
  Sends a control request to the default control pipe in the device (pipe zero)
- [EnableRemoteWake](iousbinterface/1809508-enableremotewake.md)
  Will enable or disable the USB 3.0 remote wake function for the interface
- [FindNextAltInterface](iousbinterface/1809512-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](iousbinterface/1809516-findnextassociateddescriptor.md)
- [FindNextPipe(IOUSBPipe *, IOUSBFindEndpointRequest *)](iousbinterface/1809521-findnextpipe.md)
- [FindNextPipe(IOUSBPipe *, IOUSBFindEndpointRequest *, bool)](iousbinterface/1809527-findnextpipe.md)
- [GetAlternateSetting](iousbinterface/1809532-getalternatesetting.md)
- [GetConfigValue](iousbinterface/1809537-getconfigvalue.md)
- [GetDevice](iousbinterface/1809542-getdevice.md)
- [GetEndpointProperties](iousbinterface/1809546-getendpointproperties.md)
  Returns the properties of an endpoint, possibly in an alternate interface.
- [GetEndpointPropertiesV3](iousbinterface/1809552-getendpointpropertiesv3.md)
  Returns the properties of an endpoint, possibly in an alternate interface, including any information from the SuperSpeed Companion Descriptor
- [GetInterfaceNumber](iousbinterface/1809561-getinterfacenumber.md)
- [GetInterfaceProtocol](iousbinterface/1809564-getinterfaceprotocol.md)
- [GetInterfaceStatus](iousbinterface/1809569-getinterfacestatus.md)
  Returns the result of issuing a GET_STATUS request on the device for this interface.
- [GetInterfaceStringIndex](iousbinterface/1809572-getinterfacestringindex.md)
- [GetInterfaceSubClass](iousbinterface/1809576-getinterfacesubclass.md)
- [GetNumEndpoints](iousbinterface/1809584-getnumendpoints.md)
- [GetPipeObj](iousbinterface/1809591-getpipeobj.md)
- [RecreateStreams](iousbinterface/1809596-recreatestreams.md)
- [RememberStreams](iousbinterface/1809603-rememberstreams.md)
- [RememberStreams.](iousbinterface/1809609-rememberstreams.md)
- [SetAlternateInterface](iousbinterface/1809615-setalternateinterface.md)
- [SetFunctionSuspendFeature](iousbinterface/1809621-setfunctionsuspendfeature.md)
  Issues a SET_FEATURE(FUNCTION_SUSPEND) to the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbinterface/1809556-getinterfaceclass)*