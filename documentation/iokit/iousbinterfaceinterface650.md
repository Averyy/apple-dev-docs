# IOUSBInterfaceInterface650

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.9+

## Declaration

```c
typedef struct IOUSBInterfaceStruct650 {
    ...
} IOUSBInterfaceInterface650;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface650/api-1559196-abortpipe.md)
- [AbortStreamsPipe](./iousbinterfaceinterface650/api-1558820-abortstreamspipe.md)
- [AcknowledgeNotification](./iousbinterfaceinterface650/api-1559274-acknowledgenotification.md)
- [AddRef](./iousbinterfaceinterface650/api-1558951-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface650/api-1559786-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface650/api-1558927-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface650/api-1558742-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface650/api-1558846-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface650/api-1559742-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface650/api-1559401-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface650/api-1558885-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface650/api-1558763-createinterfaceasyncport.md)
- [CreateStreams](./iousbinterfaceinterface650/api-1559695-createstreams.md)
- [FindNextAltInterface](./iousbinterfaceinterface650/api-1559092-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface650/api-1559041-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface650/api-1558814-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface650/api-1559351-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface650/api-1559170-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface650/api-1559563-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface650/api-1559071-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface650/api-1559349-getconfigurationvalue.md)
- [GetConfiguredStreams](./iousbinterfaceinterface650/api-1559813-getconfiguredstreams.md)
- [GetDevice](./iousbinterfaceinterface650/api-1558929-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface650/api-1559329-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface650/api-1559114-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface650/api-1559774-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface650/api-1559112-getendpointproperties.md)
- [GetEndpointPropertiesV3](./iousbinterfaceinterface650/api-1558842-getendpointpropertiesv3.md)
- [GetFrameListTime](./iousbinterfaceinterface650/api-1559711-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface650/api-1559451-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface650/api-1558941-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface650/api-1558961-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface650/api-1559254-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface650/api-1558944-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface650/api-1559583-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface650/api-1558732-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface650/api-1559447-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface650/api-1559426-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface650/api-1558827-getpipeproperties.md)
- [GetPipePropertiesV2](./iousbinterfaceinterface650/api-1559044-getpipepropertiesv2.md)
- [GetPipePropertiesV3](./iousbinterfaceinterface650/api-1558898-getpipepropertiesv3.md)
- [GetPipeStatus](./iousbinterfaceinterface650/api-1558731-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface650/api-1559607-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface650/api-1559143-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface650/api-1559213-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface650/api-1558760-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface650/api-1559714-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface650/api-1559612-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface650/api-1559159-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface650/api-1558813-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface650/api-1559798-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface650/api-1559184-readpipeto.md)
- [ReadStreamsPipeAsyncTO](./iousbinterfaceinterface650/api-1559762-readstreamspipeasyncto.md)
- [ReadStreamsPipeTO](./iousbinterfaceinterface650/api-1558940-readstreamspipeto.md)
- [RegisterForNotification](./iousbinterfaceinterface650/api-1559434-registerfornotification.md)
- [Release](./iousbinterfaceinterface650/api-1558976-release.md)
- [ResetPipe](./iousbinterfaceinterface650/api-1559225-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface650/api-1558937-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface650/api-1559228-setpipepolicy.md)
- [SupportsStreams](./iousbinterfaceinterface650/api-1559356-supportsstreams.md)
- [USBInterfaceClose](./iousbinterfaceinterface650/api-1559772-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface650/api-1559306-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface650/api-1559115-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface650/api-1559578-usbinterfaceopenseize.md)
- [UnregisterNotification](./iousbinterfaceinterface650/api-1559455-unregisternotification.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface650/api-1558994-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface650/api-1558824-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface650/api-1559595-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface650/api-1559007-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface650/api-1559735-writepipeto.md)
- [WriteStreamsPipeAsyncTO](./iousbinterfaceinterface650/api-1559502-writestreamspipeasyncto.md)
- [WriteStreamsPipeTO](./iousbinterfaceinterface650/api-1559797-writestreamspipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface650)*