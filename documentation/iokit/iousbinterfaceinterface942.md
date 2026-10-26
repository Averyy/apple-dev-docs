# IOUSBInterfaceInterface942

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.14+

## Declaration

```c
typedef struct IOUSBInterfaceStruct942 {
    ...
} IOUSBInterfaceInterface942;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface942/api-2977185-abortpipe.md)
- [AbortStreamsPipe](./iousbinterfaceinterface942/api-2977186-abortstreamspipe.md)
- [AcknowledgeNotification](./iousbinterfaceinterface942/api-2977187-acknowledgenotification.md)
- [AddRef](./iousbinterfaceinterface942/api-2977188-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface942/api-2977189-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface942/api-2977190-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface942/api-2977191-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface942/api-2977192-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface942/api-2977193-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface942/api-2977194-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface942/api-2977195-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface942/api-2977196-createinterfaceasyncport.md)
- [CreateStreams](./iousbinterfaceinterface942/api-2977197-createstreams.md)
- [FindNextAltInterface](./iousbinterfaceinterface942/api-2977198-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface942/api-2977199-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface942/api-2977200-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface942/api-2977201-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface942/api-2977202-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface942/api-2977203-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface942/api-2977204-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface942/api-2977205-getconfigurationvalue.md)
- [GetConfiguredStreams](./iousbinterfaceinterface942/api-2977206-getconfiguredstreams.md)
- [GetDevice](./iousbinterfaceinterface942/api-2977207-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface942/api-2977208-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface942/api-2977209-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface942/api-2977210-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface942/api-2977211-getendpointproperties.md)
- [GetEndpointPropertiesV3](./iousbinterfaceinterface942/api-2977212-getendpointpropertiesv3.md)
- [GetFrameListTime](./iousbinterfaceinterface942/api-2977213-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface942/api-2977214-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface942/api-2977215-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncNotificationPort](./iousbinterfaceinterface942/api-2977216-getinterfaceasyncnotificationpor.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface942/api-2977217-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface942/api-2977218-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface942/api-2977219-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface942/api-2977220-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface942/api-2977221-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface942/api-2977222-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface942/api-2977223-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface942/api-2977224-getpipeproperties.md)
- [GetPipePropertiesV2](./iousbinterfaceinterface942/api-2977225-getpipepropertiesv2.md)
- [GetPipePropertiesV3](./iousbinterfaceinterface942/api-2977226-getpipepropertiesv3.md)
- [GetPipeStatus](./iousbinterfaceinterface942/api-2977227-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface942/api-2977228-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface942/api-2977229-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface942/api-2977230-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface942/api-2977231-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface942/api-2977232-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface942/api-2977233-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface942/api-2977234-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface942/api-2977235-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface942/api-2977236-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface942/api-2977237-readpipeto.md)
- [ReadStreamsPipeAsyncTO](./iousbinterfaceinterface942/api-2977238-readstreamspipeasyncto.md)
- [ReadStreamsPipeTO](./iousbinterfaceinterface942/api-2977239-readstreamspipeto.md)
- [RegisterDriver](./iousbinterfaceinterface942/api-2977240-registerdriver.md)
- [RegisterForNotification](./iousbinterfaceinterface942/api-2977241-registerfornotification.md)
- [Release](./iousbinterfaceinterface942/api-2977242-release.md)
- [ResetPipe](./iousbinterfaceinterface942/api-2977243-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface942/api-2977244-setalternateinterface.md)
- [SetDeviceIdlePolicy](./iousbinterfaceinterface942/api-2977245-setdeviceidlepolicy.md)
- [SetPipeIdlePolicy](./iousbinterfaceinterface942/api-2977246-setpipeidlepolicy.md)
- [SetPipePolicy](./iousbinterfaceinterface942/api-2977247-setpipepolicy.md)
- [SupportsStreams](./iousbinterfaceinterface942/api-2977248-supportsstreams.md)
- [USBInterfaceClose](./iousbinterfaceinterface942/api-2977249-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface942/api-2977250-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface942/api-2977251-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface942/api-2977252-usbinterfaceopenseize.md)
- [UnregisterNotification](./iousbinterfaceinterface942/api-2977253-unregisternotification.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface942/api-2977254-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface942/api-2977255-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface942/api-2977256-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface942/api-2977257-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface942/api-2977258-writepipeto.md)
- [WriteStreamsPipeAsyncTO](./iousbinterfaceinterface942/api-2977259-writestreamspipeasyncto.md)
- [WriteStreamsPipeTO](./iousbinterfaceinterface942/api-2977260-writestreamspipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface942)*