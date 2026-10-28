# IOATAPIProtocolTransport

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

SCSI Protocol Driver Family for ATAPI Devices.

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class IOATAPIProtocolTransport : IOSCSIProtocolServices
```

## Overview

IOATAPIProtocolTransport contains all the bus specific support for ATAPI compliant devices. To add vendor specific features or workarounds you will sub-class the appropriate methods of this family.

## Topics

### Instance Methods
- [- AbortSCSICommand](./ioatapiprotocoltransport/api-1550943-abortscsicommand.md)
- [- AllocateATACommandObjects](./ioatapiprotocoltransport/api-1550934-allocateatacommandobjects.md)
- [- CheckWakeupResetOccurred](./ioatapiprotocoltransport/api-1550928-checkwakeupresetoccurred.md)
- [- CompleteSCSITask](./ioatapiprotocoltransport/api-1550979-completescsitask.md)
- [- ConfigureATAPIDevice](./ioatapiprotocoltransport/api-1550930-configureatapidevice.md)
- [- DeallocateATACommandObjects](./ioatapiprotocoltransport/api-1550961-deallocateatacommandobjects.md)
- [- DisablePollingOfStatusRegister](./ioatapiprotocoltransport/api-1550958-disablepollingofstatusregister.md)
- [- EnablePollingOfStatusRegister](./ioatapiprotocoltransport/api-1550929-enablepollingofstatusregister.md)
- [- GatedWaitForRequest](./ioatapiprotocoltransport/api-1550966-gatedwaitforrequest.md)
- [- GetATACommandObject](./ioatapiprotocoltransport/api-1550951-getatacommandobject.md)
- [- HandlePowerOff](./ioatapiprotocoltransport/api-1550944-handlepoweroff.md)
- [- HandlePowerOn](./ioatapiprotocoltransport/api-1550960-handlepoweron.md)
- [- HandleProtocolServiceFeature](./ioatapiprotocoltransport/api-1550976-handleprotocolservicefeature.md)
- [- IdentifyATAPIDevice](./ioatapiprotocoltransport/api-1550978-identifyatapidevice.md)
- [- IdentifyAndConfigureATAPIDevice](./ioatapiprotocoltransport/api-1550965-identifyandconfigureatapidevice.md)
- [- InspectDevice](./ioatapiprotocoltransport/api-1550942-inspectdevice.md)
- [- IsProtocolServiceSupported](./ioatapiprotocoltransport/api-1550953-isprotocolservicesupported.md)
- [- PollStatusRegister](./ioatapiprotocoltransport/api-1550949-pollstatusregister.md)
- [- PollStatusRegisterCallback](./ioatapiprotocoltransport/api-1550971-pollstatusregistercallback.md)
- [- ReconfigureATAPIDevice](./ioatapiprotocoltransport/api-1550952-reconfigureatapidevice.md)
- [- ReportATAPIDeviceType](./ioatapiprotocoltransport/api-1550941-reportatapidevicetype.md)
- [- ResetATAPIDevice](./ioatapiprotocoltransport/api-1550956-resetatapidevice.md)
- [- ReturnATACommandObject](./ioatapiprotocoltransport/api-1550950-returnatacommandobject.md)
- [- SCSITaskCallbackFunction](./ioatapiprotocoltransport/api-1550927-scsitaskcallbackfunction.md)
- [- SendATASleepCommand](./ioatapiprotocoltransport/api-1550968-sendatasleepcommand.md)
- [- SendCommand](./ioatapiprotocoltransport/api-1550963-sendcommand.md)
- [- SendSCSICommand](./ioatapiprotocoltransport/api-1550937-sendscsicommand.md)
- [- SetDMATransferMode](./ioatapiprotocoltransport/api-1550947-setdmatransfermode.md)
- [- SetPIOTransferMode](./ioatapiprotocoltransport/api-1550959-setpiotransfermode.md)
- [- SetWakeupResetOccurred](./ioatapiprotocoltransport/api-1550931-setwakeupresetoccurred.md)
- [- TurnDrivePowerOff](./ioatapiprotocoltransport/api-1550975-turndrivepoweroff.md)
- [- free](./ioatapiprotocoltransport/api-1550954-free.md)
- [- getMetaClass](./ioatapiprotocoltransport/api-1550939-getmetaclass.md)
- [- init](./ioatapiprotocoltransport/api-1550970-init.md)
- [- message](./ioatapiprotocoltransport/api-1550969-message.md)
- [- start](./ioatapiprotocoltransport/api-1550933-start.md)
- [- stop](./ioatapiprotocoltransport/api-1550938-stop.md)
### Type Methods
- [+ sATACallbackSync](./ioatapiprotocoltransport/api-1550955-satacallbacksync.md)
- [+ sATAPIConfigStateMachine](./ioatapiprotocoltransport/api-1550972-satapiconfigstatemachine.md)
- [+ sATAPIResetCallback](./ioatapiprotocoltransport/api-1550967-satapiresetcallback.md)
- [+ sATAPIVoidCallback](./ioatapiprotocoltransport/api-1550946-satapivoidcallback.md)
- [+ sCheckWakeupResetOccurred](./ioatapiprotocoltransport/api-1550974-scheckwakeupresetoccurred.md)
- [+ sConvertHighestBitToNumber](./ioatapiprotocoltransport/api-1550973-sconverthighestbittonumber.md)
- [+ sPollStatusRegister](./ioatapiprotocoltransport/api-1550964-spollstatusregister.md)
- [+ sPollStatusRegisterCallback](./ioatapiprotocoltransport/api-1550936-spollstatusregistercallback.md)
- [+ sSCSITaskCallbackProc](./ioatapiprotocoltransport/api-1550948-sscsitaskcallbackproc.md)
- [+ sSetWakeupResetOccurred](./ioatapiprotocoltransport/api-1550977-ssetwakeupresetoccurred.md)
- [+ sSwapBytes16](./ioatapiprotocoltransport/api-1550945-sswapbytes16.md)

## Relationships

### Inherits From
- [IOSCSIProtocolServices](./ioscsiprotocolservices.md)

## See Also

### ATAPI
- [ATAPIClientData](./atapiclientdata.md)
- [ATAPICmdPacket](./atapicmdpacket.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatapiprotocoltransport)*