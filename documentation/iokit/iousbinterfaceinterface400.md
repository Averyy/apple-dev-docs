# IOUSBInterfaceInterface400

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```c
typedef struct IOUSBInterfaceStruct400 {
    ...
} IOUSBInterfaceInterface400;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface400/api-3142792-abortpipe.md)
- [AddRef](./iousbinterfaceinterface400/api-3142793-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface400/api-3142794-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface400/api-3142795-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface400/api-3142796-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface400/api-3142797-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface400/api-3142798-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface400/api-3142799-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface400/api-3142800-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface400/api-3142801-createinterfaceasyncport.md)
- [FindNextAltInterface](./iousbinterfaceinterface400/api-3142802-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface400/api-3142803-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface400/api-3142804-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface400/api-3142805-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface400/api-3142806-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface400/api-3142807-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface400/api-3142808-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface400/api-3142809-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface400/api-3142810-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface400/api-3142811-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface400/api-3142812-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface400/api-3142813-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface400/api-3142814-getendpointproperties.md)
- [GetFrameListTime](./iousbinterfaceinterface400/api-3142815-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface400/api-3142816-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface400/api-3142817-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface400/api-3142818-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface400/api-3142819-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface400/api-3142820-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface400/api-3142821-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface400/api-3142822-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface400/api-3142823-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface400/api-3142824-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface400/api-3142825-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface400/api-3142826-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface400/api-3142827-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface400/api-3142828-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface400/api-3142829-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface400/api-3142830-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface400/api-3142831-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface400/api-3142832-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface400/api-3142833-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface400/api-3142834-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface400/api-3142835-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface400/api-3142836-readpipeto.md)
- [Release](./iousbinterfaceinterface400/api-3142837-release.md)
- [ResetPipe](./iousbinterfaceinterface400/api-3142838-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface400/api-3142839-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface400/api-3142840-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface400/api-3142841-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface400/api-3142842-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface400/api-3142843-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface400/api-3142844-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface400/api-3142845-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface400/api-3142846-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface400/api-3142847-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface400/api-3142848-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface400/api-3142849-writepipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface400)*