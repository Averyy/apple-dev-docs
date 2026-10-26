# IOUSBInterfaceInterface700

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.10+

## Declaration

```c
typedef struct IOUSBInterfaceStruct700 {
    ...
} IOUSBInterfaceInterface700;
```

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface700/api-1558975-abortpipe.md)
- [AbortStreamsPipe](./iousbinterfaceinterface700/api-1559108-abortstreamspipe.md)
- [AcknowledgeNotification](./iousbinterfaceinterface700/api-1558876-acknowledgenotification.md)
- [AddRef](./iousbinterfaceinterface700/api-1559272-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface700/api-1558857-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface700/api-1559337-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface700/api-1558955-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface700/api-1558739-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface700/api-1558948-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface700/api-1558748-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface700/api-1558744-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface700/api-1559577-createinterfaceasyncport.md)
- [CreateStreams](./iousbinterfaceinterface700/api-1559325-createstreams.md)
- [FindNextAltInterface](./iousbinterfaceinterface700/api-1559333-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./iousbinterfaceinterface700/api-1559645-findnextassociateddescriptor.md)
- [GetAlternateSetting](./iousbinterfaceinterface700/api-1559400-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface700/api-1559358-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface700/api-1559168-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbinterfaceinterface700/api-1559546-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface700/api-1559635-getbusmicroframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface700/api-1559036-getconfigurationvalue.md)
- [GetConfiguredStreams](./iousbinterfaceinterface700/api-1558797-getconfiguredstreams.md)
- [GetDevice](./iousbinterfaceinterface700/api-1559016-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface700/api-1558847-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface700/api-1558953-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface700/api-1558782-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface700/api-1558992-getendpointproperties.md)
- [GetEndpointPropertiesV3](./iousbinterfaceinterface700/api-1558751-getendpointpropertiesv3.md)
- [GetFrameListTime](./iousbinterfaceinterface700/api-1559605-getframelisttime.md)
- [GetIOUSBLibVersion](./iousbinterfaceinterface700/api-1559280-getiousblibversion.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface700/api-1559592-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface700/api-1558710-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface700/api-1559600-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface700/api-1559362-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface700/api-1559330-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface700/api-1559528-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface700/api-1559760-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface700/api-1559724-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface700/api-1559181-getpipeproperties.md)
- [GetPipePropertiesV2](./iousbinterfaceinterface700/api-1559738-getpipepropertiesv2.md)
- [GetPipePropertiesV3](./iousbinterfaceinterface700/api-1559507-getpipepropertiesv3.md)
- [GetPipeStatus](./iousbinterfaceinterface700/api-1559290-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface700/api-1559824-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface700/api-1559206-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface700/api-1559163-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface700/api-1559707-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface700/api-1559313-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface700/api-1559611-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface700/api-1559419-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface700/api-1559771-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface700/api-1559359-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface700/api-1559806-readpipeto.md)
- [ReadStreamsPipeAsyncTO](./iousbinterfaceinterface700/api-1559573-readstreamspipeasyncto.md)
- [ReadStreamsPipeTO](./iousbinterfaceinterface700/api-1558725-readstreamspipeto.md)
- [RegisterDriver](./iousbinterfaceinterface700/api-1559547-registerdriver.md)
- [RegisterForNotification](./iousbinterfaceinterface700/api-1559154-registerfornotification.md)
- [Release](./iousbinterfaceinterface700/api-1559489-release.md)
- [ResetPipe](./iousbinterfaceinterface700/api-1558884-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface700/api-1559437-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface700/api-1559522-setpipepolicy.md)
- [SupportsStreams](./iousbinterfaceinterface700/api-1558724-supportsstreams.md)
- [USBInterfaceClose](./iousbinterfaceinterface700/api-1559669-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface700/api-1559072-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface700/api-1558954-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface700/api-1559147-usbinterfaceopenseize.md)
- [UnregisterNotification](./iousbinterfaceinterface700/api-1558970-unregisternotification.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface700/api-1559743-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface700/api-1559009-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface700/api-1559122-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface700/api-1558737-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface700/api-1559495-writepipeto.md)
- [WriteStreamsPipeAsyncTO](./iousbinterfaceinterface700/api-1559617-writestreamspipeasyncto.md)
- [WriteStreamsPipeTO](./iousbinterfaceinterface700/api-1559236-writestreamspipeto.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface700)*