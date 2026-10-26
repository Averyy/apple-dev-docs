# IOUSBInterfaceInterface245

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.4+

## Declaration

```c
typedef struct IOUSBInterfaceStruct245 {
    ...
} IOUSBInterfaceInterface245;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface245/api-1559055-abortpipe.md)
- [AddRef](./iousbinterfaceinterface245/api-1559408-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface245/api-1559723-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface245/api-1558771-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface245/api-1559253-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface245/api-1559510-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface245/api-1559776-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface245/api-1559005-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface245/api-1559348-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface245/api-1558821-createinterfaceasyncport.md)
- [FindNextAltInterface](./iousbinterfaceinterface245/api-1559098-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface245/api-1558726-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface245/api-1558808-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface245/api-1559137-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface245/api-1558790-getbusframenumber.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface245/api-1559230-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface245/api-1559002-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface245/api-1558713-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface245/api-1559584-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface245/api-1558865-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface245/api-1559309-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface245/api-1559183-getendpointproperties.md)
- [GetFrameListTime](./iousbinterfaceinterface245/api-1559244-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface245/api-1559383-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface245/api-1559142-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface245/api-1559350-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface245/api-1558844-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface245/api-1559210-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface245/api-1559516-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface245/api-1559220-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface245/api-1558815-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface245/api-1559690-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface245/api-1558832-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface245/api-1559453-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface245/api-1559779-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface245/api-1559512-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface245/api-1558733-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface245/api-1559149-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface245/api-1559763-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface245/api-1559221-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface245/api-1558818-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface245/api-1558805-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface245/api-1559519-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface245/api-1558928-readpipeto.md)
- [Release](./iousbinterfaceinterface245/api-1559267-release.md)
- [ResetPipe](./iousbinterfaceinterface245/api-1559233-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface245/api-1559454-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface245/api-1559101-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface245/api-1559449-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface245/api-1559660-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface245/api-1558981-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface245/api-1559655-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface245/api-1559049-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface245/api-1559093-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface245/api-1559460-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface245/api-1559158-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface245/api-1559464-writepipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface245)*