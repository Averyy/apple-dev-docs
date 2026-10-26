# IOUSBInterfaceInterface500

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
typedef struct IOUSBInterfaceStruct500 {
    ...
} IOUSBInterfaceInterface500;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface500/api-1559124-abortpipe.md)
- [AddRef](./iousbinterfaceinterface500/api-1558854-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface500/api-1559565-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface500/api-1558754-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface500/api-1559442-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface500/api-1559231-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface500/api-1559536-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface500/api-1558978-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface500/api-1558798-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface500/api-1559126-createinterfaceasyncport.md)
- [FindNextAltInterface](./iousbinterfaceinterface500/api-1559670-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface500/api-1559332-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface500/api-1559441-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface500/api-1559766-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface500/api-1559667-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface500/api-1558878-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface500/api-1559094-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface500/api-1559167-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface500/api-1559428-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface500/api-1559560-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface500/api-1558958-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface500/api-1559613-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface500/api-1559127-getendpointproperties.md)
- [GetFrameListTime](./iousbinterfaceinterface500/api-1559688-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface500/api-1558866-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface500/api-1559829-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface500/api-1559382-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface500/api-1559725-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface500/api-1559485-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface500/api-1559317-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface500/api-1559017-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface500/api-1559176-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface500/api-1559068-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface500/api-1559793-getpipeproperties.md)
- [GetPipePropertiesV2](./iousbinterfaceinterface500/api-1559558-getpipepropertiesv2.md)
- [GetPipeStatus](./iousbinterfaceinterface500/api-1559081-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface500/api-1558777-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface500/api-1559649-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface500/api-1559765-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface500/api-1559293-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface500/api-1559079-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface500/api-1559730-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface500/api-1559324-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface500/api-1559681-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface500/api-1559761-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface500/api-1559497-readpipeto.md)
- [Release](./iousbinterfaceinterface500/api-1559019-release.md)
- [ResetPipe](./iousbinterfaceinterface500/api-1559596-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface500/api-1558841-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface500/api-1559463-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface500/api-1559543-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface500/api-1559819-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface500/api-1559001-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface500/api-1559691-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface500/api-1559599-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface500/api-1559803-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface500/api-1559105-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface500/api-1559409-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface500/api-1559039-writepipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface500)*