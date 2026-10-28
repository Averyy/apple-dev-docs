# IOUSBInterface

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An object that represents an interface of a device on the USB bus.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`IOUSBHostInterface`](./iousbhostinterface.md) instead.

## Declaration

```cpp
class IOUSBInterface : IOService
```

## Overview

Use this class to find an interface’s pipes and read its associated descriptors.

## Topics

### Miscellaneous
- [DeviceRequest(IOUSBDevRequest *, IOUSBCompletion *)](./iousbinterface/api-1809501-devicerequest.md)
  Sends a control request to the default control pipe in the device (pipe zero)
- [DeviceRequest(IOUSBDevRequestDesc *, IOUSBCompletion *)](./iousbinterface/api-1809505-devicerequest.md)
  Sends a control request to the default control pipe in the device (pipe zero)
- [EnableRemoteWake](./iousbinterface/api-1809508-enableremotewake.md)
  Will enable or disable the USB 3.0 remote wake function for the interface
- [FindNextAltInterface](./iousbinterface/api-1809512-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterface/api-1809516-findnextassociateddescriptor.md)
- [FindNextPipe(IOUSBPipe *, IOUSBFindEndpointRequest *)](./iousbinterface/api-1809521-findnextpipe.md)
- [FindNextPipe(IOUSBPipe *, IOUSBFindEndpointRequest *, bool)](./iousbinterface/api-1809527-findnextpipe.md)
- [GetAlternateSetting](./iousbinterface/api-1809532-getalternatesetting.md)
- [GetConfigValue](./iousbinterface/api-1809537-getconfigvalue.md)
- [GetDevice](./iousbinterface/api-1809542-getdevice.md)
- [GetEndpointProperties](./iousbinterface/api-1809546-getendpointproperties.md)
  Returns the properties of an endpoint, possibly in an alternate interface.
- [GetEndpointPropertiesV3](./iousbinterface/api-1809552-getendpointpropertiesv3.md)
  Returns the properties of an endpoint, possibly in an alternate interface, including any information from the SuperSpeed Companion Descriptor
- [GetInterfaceClass](./iousbinterface/api-1809556-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterface/api-1809561-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterface/api-1809564-getinterfaceprotocol.md)
- [GetInterfaceStatus](./iousbinterface/api-1809569-getinterfacestatus.md)
  Returns the result of issuing a GET_STATUS request on the device for this interface.
- [GetInterfaceStringIndex](./iousbinterface/api-1809572-getinterfacestringindex.md)
- [GetInterfaceSubClass](./iousbinterface/api-1809576-getinterfacesubclass.md)
- [GetNumEndpoints](./iousbinterface/api-1809584-getnumendpoints.md)
- [GetPipeObj](./iousbinterface/api-1809591-getpipeobj.md)
- [RecreateStreams](./iousbinterface/api-1809596-recreatestreams.md)
- [RememberStreams](./iousbinterface/api-1809603-rememberstreams.md)
- [RememberStreams.](./iousbinterface/api-1809609-rememberstreams.md)
- [SetAlternateInterface](./iousbinterface/api-1809615-setalternateinterface.md)
- [SetFunctionSuspendFeature](./iousbinterface/api-1809621-setfunctionsuspendfeature.md)
  Issues a SET_FEATURE(FUNCTION_SUSPEND) to the interface.
### Instance Methods
- [- getMetaClass](./iousbinterface/api-3609096-getmetaclass.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### IOKit
- [IOUSBDevice](./iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOOFPathMatching](./api-1575304-ioofpathmatching.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
- [IOUSBHostDevice](./iousbhostdevice.md)
- [IOUSBHostPipe](./iousbhostpipe.md)
- [IOUSBHostIOSource](./iousbhostiosource.md)
- [IOUSBHostStream](./iousbhoststream.md)
- [IOHIDEventDriver](./iohideventdriver.md)
- [IOHIDEventService](./iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](./iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](./iohidsystem.md)
- [IOHIKeyboardMapper](./iohikeyboardmapper.md)
- [IOHIKeyboard](./iohikeyboard.md)
- [IOHIPointing](./iohipointing.md)
- [IOHIDevice](./iohidevice.md)
- [IOHIDElement](./iohidelement.md)
- [IOHIDWorkLoop](./iohidworkloop.md)
- [IOEthernetInterface](./ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](./ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbinterface)*