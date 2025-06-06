# IOATAPIProtocolTransport

**Framework**: Kernel  
**Kind**: cl

SCSI Protocol Driver Family for ATAPI Devices.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class IOATAPIProtocolTransport : IOSCSIProtocolServices
```

#### Overview

IOATAPIProtocolTransport contains all the bus specific support for ATAPI compliant devices. To add vendor specific features or workarounds you will sub-class the appropriate methods of this family.

## Topics

### Instance Methods
- [- AbortSCSICommand](ioatapiprotocoltransport/1550943-abortscsicommand.md)
- [- AllocateATACommandObjects](ioatapiprotocoltransport/1550934-allocateatacommandobjects.md)
- [- CheckWakeupResetOccurred](ioatapiprotocoltransport/1550928-checkwakeupresetoccurred.md)
- [- CompleteSCSITask](ioatapiprotocoltransport/1550979-completescsitask.md)
- [- ConfigureATAPIDevice](ioatapiprotocoltransport/1550930-configureatapidevice.md)
- [- DeallocateATACommandObjects](ioatapiprotocoltransport/1550961-deallocateatacommandobjects.md)
- [- DisablePollingOfStatusRegister](ioatapiprotocoltransport/1550958-disablepollingofstatusregister.md)
- [- EnablePollingOfStatusRegister](ioatapiprotocoltransport/1550929-enablepollingofstatusregister.md)
- [- GatedWaitForRequest](ioatapiprotocoltransport/1550966-gatedwaitforrequest.md)
- [- GetATACommandObject](ioatapiprotocoltransport/1550951-getatacommandobject.md)
- [- HandlePowerOff](ioatapiprotocoltransport/1550944-handlepoweroff.md)
- [- HandlePowerOn](ioatapiprotocoltransport/1550960-handlepoweron.md)
- [- HandleProtocolServiceFeature](ioatapiprotocoltransport/1550976-handleprotocolservicefeature.md)
- [- IdentifyATAPIDevice](ioatapiprotocoltransport/1550978-identifyatapidevice.md)
- [- IdentifyAndConfigureATAPIDevice](ioatapiprotocoltransport/1550965-identifyandconfigureatapidevice.md)
- [- InspectDevice](ioatapiprotocoltransport/1550942-inspectdevice.md)
- [- IsProtocolServiceSupported](ioatapiprotocoltransport/1550953-isprotocolservicesupported.md)
- [- PollStatusRegister](ioatapiprotocoltransport/1550949-pollstatusregister.md)
- [- PollStatusRegisterCallback](ioatapiprotocoltransport/1550971-pollstatusregistercallback.md)
- [- ReconfigureATAPIDevice](ioatapiprotocoltransport/1550952-reconfigureatapidevice.md)
- [- ReportATAPIDeviceType](ioatapiprotocoltransport/1550941-reportatapidevicetype.md)
- [- ResetATAPIDevice](ioatapiprotocoltransport/1550956-resetatapidevice.md)
- [- ReturnATACommandObject](ioatapiprotocoltransport/1550950-returnatacommandobject.md)
- [- SCSITaskCallbackFunction](ioatapiprotocoltransport/1550927-scsitaskcallbackfunction.md)
- [- SendATASleepCommand](ioatapiprotocoltransport/1550968-sendatasleepcommand.md)
- [- SendCommand](ioatapiprotocoltransport/1550963-sendcommand.md)
- [- SendSCSICommand](ioatapiprotocoltransport/1550937-sendscsicommand.md)
- [- SetDMATransferMode](ioatapiprotocoltransport/1550947-setdmatransfermode.md)
- [- SetPIOTransferMode](ioatapiprotocoltransport/1550959-setpiotransfermode.md)
- [- SetWakeupResetOccurred](ioatapiprotocoltransport/1550931-setwakeupresetoccurred.md)
- [- TurnDrivePowerOff](ioatapiprotocoltransport/1550975-turndrivepoweroff.md)
- [- free](ioatapiprotocoltransport/1550954-free.md)
- [- getMetaClass](ioatapiprotocoltransport/1550939-getmetaclass.md)
- [- init](ioatapiprotocoltransport/1550970-init.md)
- [- message](ioatapiprotocoltransport/1550969-message.md)
- [- start](ioatapiprotocoltransport/1550933-start.md)
- [- stop](ioatapiprotocoltransport/1550938-stop.md)
### Type Methods
- [+ sATACallbackSync](ioatapiprotocoltransport/1550955-satacallbacksync.md)
- [+ sATAPIConfigStateMachine](ioatapiprotocoltransport/1550972-satapiconfigstatemachine.md)
- [+ sATAPIResetCallback](ioatapiprotocoltransport/1550967-satapiresetcallback.md)
- [+ sATAPIVoidCallback](ioatapiprotocoltransport/1550946-satapivoidcallback.md)
- [+ sCheckWakeupResetOccurred](ioatapiprotocoltransport/1550974-scheckwakeupresetoccurred.md)
- [+ sConvertHighestBitToNumber](ioatapiprotocoltransport/1550973-sconverthighestbittonumber.md)
- [+ sPollStatusRegister](ioatapiprotocoltransport/1550964-spollstatusregister.md)
- [+ sPollStatusRegisterCallback](ioatapiprotocoltransport/1550936-spollstatusregistercallback.md)
- [+ sSCSITaskCallbackProc](ioatapiprotocoltransport/1550948-sscsitaskcallbackproc.md)
- [+ sSetWakeupResetOccurred](ioatapiprotocoltransport/1550977-ssetwakeupresetoccurred.md)
- [+ sSwapBytes16](ioatapiprotocoltransport/1550945-sswapbytes16.md)

## Relationships

### Inherits From
- [IOSCSIProtocolServices](ioscsiprotocolservices.md)

## See Also

- [ATAPIClientData](atapiclientdata.md)
- [ATAPICmdPacket](atapicmdpacket.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatapiprotocoltransport)*