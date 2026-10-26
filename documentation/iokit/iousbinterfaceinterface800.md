# IOUSBInterfaceInterface800

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.12+

## Declaration

```c
typedef struct IOUSBInterfaceStruct800 {
    ...
} IOUSBInterfaceInterface800;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface800/api-1639585-abortpipe.md)
- [AbortStreamsPipe](./iousbinterfaceinterface800/api-1639562-abortstreamspipe.md)
- [AcknowledgeNotification](./iousbinterfaceinterface800/api-1639560-acknowledgenotification.md)
- [AddRef](./iousbinterfaceinterface800/api-1639581-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface800/api-1639563-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface800/api-1639550-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface800/api-1639607-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface800/api-1639577-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface800/api-1639619-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface800/api-1639568-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface800/api-1639611-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface800/api-1639569-createinterfaceasyncport.md)
- [CreateStreams](./iousbinterfaceinterface800/api-1639548-createstreams.md)
- [FindNextAltInterface](./iousbinterfaceinterface800/api-1639547-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface800/api-1639544-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface800/api-1639593-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface800/api-1639596-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface800/api-1639600-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface800/api-1639549-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface800/api-1639602-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface800/api-1639601-getconfigurationvalue.md)
- [GetConfiguredStreams](./iousbinterfaceinterface800/api-1639617-getconfiguredstreams.md)
- [GetDevice](./iousbinterfaceinterface800/api-1639616-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface800/api-1639578-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface800/api-1639546-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface800/api-1639594-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface800/api-1639570-getendpointproperties.md)
- [GetEndpointPropertiesV3](./iousbinterfaceinterface800/api-1639614-getendpointpropertiesv3.md)
- [GetFrameListTime](./iousbinterfaceinterface800/api-1639615-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface800/api-1639559-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface800/api-1639583-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface800/api-1639584-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface800/api-1639537-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface800/api-1639554-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface800/api-1639595-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface800/api-1639610-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface800/api-1639608-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface800/api-1639561-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface800/api-1639557-getpipeproperties.md)
- [GetPipePropertiesV2](./iousbinterfaceinterface800/api-1639543-getpipepropertiesv2.md)
- [GetPipePropertiesV3](./iousbinterfaceinterface800/api-1639575-getpipepropertiesv3.md)
- [GetPipeStatus](./iousbinterfaceinterface800/api-1639576-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface800/api-1639597-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface800/api-1639586-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface800/api-1639588-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface800/api-1639556-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface800/api-1639580-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface800/api-1639603-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface800/api-1639558-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface800/api-1639545-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface800/api-1639599-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface800/api-1639566-readpipeto.md)
- [ReadStreamsPipeAsyncTO](./iousbinterfaceinterface800/api-1639574-readstreamspipeasyncto.md)
- [ReadStreamsPipeTO](./iousbinterfaceinterface800/api-1639582-readstreamspipeto.md)
- [RegisterDriver](./iousbinterfaceinterface800/api-1639592-registerdriver.md)
- [RegisterForNotification](./iousbinterfaceinterface800/api-1639540-registerfornotification.md)
- [Release](./iousbinterfaceinterface800/api-1639551-release.md)
- [ResetPipe](./iousbinterfaceinterface800/api-1639604-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface800/api-1639555-setalternateinterface.md)
- [SetDeviceIdlePolicy](./iousbinterfaceinterface800/api-1639606-setdeviceidlepolicy.md)
- [SetPipeIdlePolicy](./iousbinterfaceinterface800/api-1639538-setpipeidlepolicy.md)
- [SetPipePolicy](./iousbinterfaceinterface800/api-1639618-setpipepolicy.md)
- [SupportsStreams](./iousbinterfaceinterface800/api-1639605-supportsstreams.md)
- [USBInterfaceClose](./iousbinterfaceinterface800/api-1639541-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface800/api-1639567-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface800/api-1639579-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface800/api-1639553-usbinterfaceopenseize.md)
- [UnregisterNotification](./iousbinterfaceinterface800/api-1639565-unregisternotification.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface800/api-1639542-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface800/api-1639612-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface800/api-1639539-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface800/api-1639572-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface800/api-1639564-writepipeto.md)
- [WriteStreamsPipeAsyncTO](./iousbinterfaceinterface800/api-1639587-writestreamspipeasyncto.md)
- [WriteStreamsPipeTO](./iousbinterfaceinterface800/api-1639552-writestreamspipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface800)*