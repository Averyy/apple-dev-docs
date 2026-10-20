# GetInterfaceStringIndex

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual UInt8 GetInterfaceStringIndex();
```

#### Return Value

the string index

#### Overview

returns the index of the string descriptor describing the interface

## See Also

### Miscellaneous
- [DeviceRequest(IOUSBDevRequest *, IOUSBCompletion *)](./api-1809501-devicerequest.md)
  Sends a control request to the default control pipe in the device (pipe zero)
- [DeviceRequest(IOUSBDevRequestDesc *, IOUSBCompletion *)](./api-1809505-devicerequest.md)
  Sends a control request to the default control pipe in the device (pipe zero)
- [EnableRemoteWake](./api-1809508-enableremotewake.md)
  Will enable or disable the USB 3.0 remote wake function for the interface
- [FindNextAltInterface](./api-1809512-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./api-1809516-findnextassociateddescriptor.md)
- [FindNextPipe(IOUSBPipe *, IOUSBFindEndpointRequest *)](./api-1809521-findnextpipe.md)
- [FindNextPipe(IOUSBPipe *, IOUSBFindEndpointRequest *, bool)](./api-1809527-findnextpipe.md)
- [GetAlternateSetting](./api-1809532-getalternatesetting.md)
- [GetConfigValue](./api-1809537-getconfigvalue.md)
- [GetDevice](./api-1809542-getdevice.md)
- [GetEndpointProperties](./api-1809546-getendpointproperties.md)
  Returns the properties of an endpoint, possibly in an alternate interface.
- [GetEndpointPropertiesV3](./api-1809552-getendpointpropertiesv3.md)
  Returns the properties of an endpoint, possibly in an alternate interface, including any information from the SuperSpeed Companion Descriptor
- [GetInterfaceClass](./api-1809556-getinterfaceclass.md)
- [GetInterfaceNumber](./api-1809561-getinterfacenumber.md)
- [GetInterfaceProtocol](./api-1809564-getinterfaceprotocol.md)
- [GetInterfaceStatus](./api-1809569-getinterfacestatus.md)
  Returns the result of issuing a GET_STATUS request on the device for this interface.
- [GetInterfaceSubClass](./api-1809576-getinterfacesubclass.md)
- [GetNumEndpoints](./api-1809584-getnumendpoints.md)
- [GetPipeObj](./api-1809591-getpipeobj.md)
- [RecreateStreams](./api-1809596-recreatestreams.md)
- [RememberStreams](./api-1809603-rememberstreams.md)
- [RememberStreams.](./api-1809609-rememberstreams.md)
- [SetAlternateInterface](./api-1809615-setalternateinterface.md)
- [SetFunctionSuspendFeature](./api-1809621-setfunctionsuspendfeature.md)
  Issues a SET_FEATURE(FUNCTION_SUSPEND) to the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbinterface/1809572-getinterfacestringindex)*