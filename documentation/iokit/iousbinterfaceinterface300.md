# IOUSBInterfaceInterface300

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
typedef struct IOUSBInterfaceStruct300 {
    ...
} IOUSBInterfaceInterface300;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface300/api-1558784-abortpipe.md)
- [AddRef](./iousbinterfaceinterface300/api-1559487-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface300/api-1559800-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface300/api-1559720-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface300/api-1559671-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface300/api-1558919-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface300/api-1558853-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface300/api-1558838-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface300/api-1559193-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface300/api-1558908-createinterfaceasyncport.md)
- [FindNextAltInterface](./iousbinterfaceinterface300/api-1558980-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface300/api-1559048-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface300/api-1558829-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface300/api-1559476-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface300/api-1559353-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface300/api-1559481-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface300/api-1559033-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface300/api-1559030-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface300/api-1559736-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface300/api-1559319-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface300/api-1559222-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface300/api-1559492-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface300/api-1559385-getendpointproperties.md)
- [GetFrameListTime](./iousbinterfaceinterface300/api-1559287-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface300/api-1559677-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface300/api-1559258-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface300/api-1559188-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface300/api-1559626-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface300/api-1559018-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface300/api-1559643-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface300/api-1558942-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface300/api-1559443-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface300/api-1558807-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface300/api-1559198-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface300/api-1559684-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface300/api-1559139-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface300/api-1559077-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface300/api-1558705-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface300/api-1559371-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface300/api-1558974-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface300/api-1558792-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface300/api-1559698-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface300/api-1558743-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface300/api-1559216-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface300/api-1559737-readpipeto.md)
- [Release](./iousbinterfaceinterface300/api-1559682-release.md)
- [ResetPipe](./iousbinterfaceinterface300/api-1559357-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface300/api-1559102-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface300/api-1559673-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface300/api-1559486-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface300/api-1559004-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface300/api-1559367-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface300/api-1559335-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface300/api-1559238-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface300/api-1559086-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface300/api-1559146-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface300/api-1559205-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface300/api-1559208-writepipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface300)*