# IOUSBInterfaceInterface220

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.4+

## Declaration

```c
typedef struct IOUSBInterfaceStruct220 {
    ...
} IOUSBInterfaceInterface220;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface220/api-1559028-abortpipe.md)
- [AddRef](./iousbinterfaceinterface220/api-1559537-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface220/api-1559370-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface220/api-1558716-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface220/api-1558939-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface220/api-1559597-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface220/api-1559084-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface220/api-1559291-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface220/api-1559652-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface220/api-1558893-createinterfaceasyncport.md)
- [FindNextAltInterface](./iousbinterfaceinterface220/api-1558973-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface220/api-1559120-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface220/api-1559542-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface220/api-1559568-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface220/api-1559424-getbusframenumber.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface220/api-1559608-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface220/api-1558932-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface220/api-1559785-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface220/api-1559477-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface220/api-1559499-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface220/api-1558759-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface220/api-1558848-getendpointproperties.md)
- [GetFrameListTime](./iousbinterfaceinterface220/api-1559310-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface220/api-1559265-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface220/api-1558840-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface220/api-1559204-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface220/api-1559749-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface220/api-1559818-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface220/api-1559529-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface220/api-1558736-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface220/api-1559080-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface220/api-1559391-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface220/api-1559190-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface220/api-1558930-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface220/api-1559058-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface220/api-1559422-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface220/api-1559640-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface220/api-1559156-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface220/api-1559470-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface220/api-1559704-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface220/api-1558918-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface220/api-1559802-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface220/api-1558862-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface220/api-1559466-readpipeto.md)
- [Release](./iousbinterfaceinterface220/api-1559523-release.md)
- [ResetPipe](./iousbinterfaceinterface220/api-1558796-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface220/api-1559392-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface220/api-1559380-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface220/api-1559587-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface220/api-1559452-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface220/api-1559023-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface220/api-1559381-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface220/api-1558779-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface220/api-1559570-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface220/api-1559672-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface220/api-1559646-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface220/api-1559261-writepipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface220)*