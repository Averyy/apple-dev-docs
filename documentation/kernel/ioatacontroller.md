# IOATAController

**Framework**: Kernel  
**Kind**: cl

The base class for ata controller family. Provides the interface common to all ata bus controllers.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class IOATAController : IOService
```

#### Overview

The header doc for this class is incomplete. The source however is heavily commented and should be consulted until such time as complete header doc is available.

## Topics

### Miscellaneous
- [busCanDispatch](ioatacontroller/1811873-buscandispatch.md)
  answers whether the bus is in state such that the next command can be dispatched.
- [dispatchNext](ioatacontroller/1811887-dispatchnext.md)
  Causes the command at the front of the queue to dequeue, made the current command and begin execution.
- [handleCommand](ioatacontroller/1811902-handlecommand.md)
  Called by executeCommand() to handle the client command from the workloop context.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](ioatacontroller/reserved.md)
### Instance Methods
- [- ATAPISecondaryExists](ioatacontroller/3917635-atapisecondaryexists.md)
- [- ATAPISlaveExists](ioatacontroller/1490687-atapislaveexists.md)
- [- allocateDoubleBuffer](ioatacontroller/1490619-allocatedoublebuffer.md)
- [- asyncCommand](ioatacontroller/1490682-asynccommand.md)
- [- asyncData](ioatacontroller/1490697-asyncdata.md)
- [- asyncIO](ioatacontroller/1490621-asyncio.md)
- [- asyncStatus](ioatacontroller/1490643-asyncstatus.md)
- [- bitSigToNumeric](ioatacontroller/1490639-bitsigtonumeric.md)
- [- busCanDispatch](ioatacontroller/1490660-buscandispatch.md)
- [- checkTimeout](ioatacontroller/1490701-checktimeout.md)
- [- completeIO](ioatacontroller/1490684-completeio.md)
- [- configureTFPointers](ioatacontroller/1490690-configuretfpointers.md)
- [- dequeueFirstCommand](ioatacontroller/1490618-dequeuefirstcommand.md)
- [- determineATAPIState](ioatacontroller/1490702-determineatapistate.md)
- [- dispatchNext](ioatacontroller/1490645-dispatchnext.md)
- [- enqueueCommand](ioatacontroller/1490655-enqueuecommand.md)
- [- executeCommand](ioatacontroller/1490670-executecommand.md)
- [- executeEventCallouts](ioatacontroller/1490623-executeeventcallouts.md)
- [- free](ioatacontroller/1490669-free.md)
- [- getConfig](ioatacontroller/1490665-getconfig.md)
- [- getMetaClass](ioatacontroller/1490694-getmetaclass.md)
- [- handleBusReset](ioatacontroller/1490710-handlebusreset.md)
- [- handleCommand](ioatacontroller/1490650-handlecommand.md)
- [- handleDeviceInterrupt](ioatacontroller/1490654-handledeviceinterrupt.md)
- [- handleExecIO](ioatacontroller/1490663-handleexecio.md)
- [- handleOverrun](ioatacontroller/1490706-handleoverrun.md)
- [- handleQueueFlush](ioatacontroller/1490678-handlequeueflush.md)
- [- handleRegAccess](ioatacontroller/1490708-handleregaccess.md)
- [- handleTimeout](ioatacontroller/1490647-handletimeout.md)
- [- init](ioatacontroller/1490629-init.md)
- [- issueCommand](ioatacontroller/1490672-issuecommand.md)
- [- probe](ioatacontroller/1490674-probe.md)
- [- provideBusInfo](ioatacontroller/1490695-providebusinfo.md)
- [- readATAPIByteCount](ioatacontroller/1490668-readatapibytecount.md)
- [- readExtRegister](ioatacontroller/1490692-readextregister.md)
- [- readExtRegister](ioatacontroller/3676014-readextregister.md)
- [- registerAccess](ioatacontroller/1490637-registeraccess.md)
- [- scanForDrives](ioatacontroller/1490649-scanfordrives.md)
- [- selectConfig](ioatacontroller/1490626-selectconfig.md)
- [- selectDevice](ioatacontroller/1490680-selectdevice.md)
- [- selectIOTiming](ioatacontroller/1490666-selectiotiming.md)
- [- softResetBus](ioatacontroller/1490635-softresetbus.md)
- [- start](ioatacontroller/1490714-start.md)
- [- startDMA](ioatacontroller/1490712-startdma.md)
- [- startTimer](ioatacontroller/1490651-starttimer.md)
- [- stopDMA](ioatacontroller/1490705-stopdma.md)
- [- stopTimer](ioatacontroller/1490631-stoptimer.md)
- [- swapBytes16](ioatacontroller/1490625-swapbytes16.md)
- [- synchronousIO](ioatacontroller/1490703-synchronousio.md)
- [- txDataIn](ioatacontroller/1490686-txdatain.md)
- [- txDataOut](ioatacontroller/1490652-txdataout.md)
- [- waitForU8Status](ioatacontroller/1490699-waitforu8status.md)
- [- writeExtRegister](ioatacontroller/1490676-writeextregister.md)
- [- writeExtRegister](ioatacontroller/3676015-writeextregister.md)
- [- writePacket](ioatacontroller/1490642-writepacket.md)
### Type Methods
- [+ executeCommandAction](ioatacontroller/1490634-executecommandaction.md)
- [+ timeoutOccured](ioatacontroller/1490688-timeoutoccured.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacontroller)*