# IOUSBInterfaceInterface550

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBInterfaceStruct550 {
    ...
} IOUSBInterfaceInterface550;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface550/api-1559748-abortpipe.md)
- [AbortStreamsPipe](./iousbinterfaceinterface550/api-1559034-abortstreamspipe.md)
- [AddRef](./iousbinterfaceinterface550/api-1558791-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface550/api-1559728-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface550/api-1559623-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface550/api-1559402-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface550/api-1559590-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface550/api-1559022-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface550/api-1559588-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface550/api-1559271-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface550/api-1559075-createinterfaceasyncport.md)
- [CreateStreams](./iousbinterfaceinterface550/api-1559160-createstreams.md)
- [FindNextAltInterface](./iousbinterfaceinterface550/api-1559347-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface550/api-1558914-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface550/api-1559100-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface550/api-1559320-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface550/api-1559042-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface550/api-1558964-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface550/api-1559718-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface550/api-1559721-getconfigurationvalue.md)
- [GetConfiguredStreams](./iousbinterfaceinterface550/api-1559788-getconfiguredstreams.md)
- [GetDevice](./iousbinterfaceinterface550/api-1558868-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface550/api-1558887-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface550/api-1559480-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface550/api-1558729-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface550/api-1559069-getendpointproperties.md)
- [GetEndpointPropertiesV3](./iousbinterfaceinterface550/api-1559815-getendpointpropertiesv3.md)
- [GetFrameListTime](./iousbinterfaceinterface550/api-1558723-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface550/api-1559266-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface550/api-1559467-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface550/api-1558793-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface550/api-1559521-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface550/api-1559656-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface550/api-1558787-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface550/api-1559505-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface550/api-1559809-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface550/api-1559300-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface550/api-1559276-getpipeproperties.md)
- [GetPipePropertiesV2](./iousbinterfaceinterface550/api-1559342-getpipepropertiesv2.md)
- [GetPipePropertiesV3](./iousbinterfaceinterface550/api-1559364-getpipepropertiesv3.md)
- [GetPipeStatus](./iousbinterfaceinterface550/api-1559011-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface550/api-1559555-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface550/api-1559642-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface550/api-1558767-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface550/api-1559153-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface550/api-1559150-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface550/api-1559369-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface550/api-1559066-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface550/api-1558938-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface550/api-1559031-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface550/api-1559318-readpipeto.md)
- [ReadStreamsPipeAsyncTO](./iousbinterfaceinterface550/api-1559478-readstreamspipeasyncto.md)
- [ReadStreamsPipeTO](./iousbinterfaceinterface550/api-1559740-readstreamspipeto.md)
- [Release](./iousbinterfaceinterface550/api-1559593-release.md)
- [ResetPipe](./iousbinterfaceinterface550/api-1559312-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface550/api-1559778-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface550/api-1559285-setpipepolicy.md)
- [SupportsStreams](./iousbinterfaceinterface550/api-1559366-supportsstreams.md)
- [USBInterfaceClose](./iousbinterfaceinterface550/api-1559399-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface550/api-1559692-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface550/api-1558905-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface550/api-1559731-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface550/api-1559614-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface550/api-1559475-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface550/api-1559494-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface550/api-1559263-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface550/api-1558950-writepipeto.md)
- [WriteStreamsPipeAsyncTO](./iousbinterfaceinterface550/api-1559025-writestreamspipeasyncto.md)
- [WriteStreamsPipeTO](./iousbinterfaceinterface550/api-1559562-writestreamspipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface550)*