# IOATAController

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The base class for ata controller family. Provides the interface common to all ata bus controllers.

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class IOATAController : IOService
```

#### Overview

The header doc for this class is incomplete. The source however is heavily commented and should be consulted until such time as complete header doc is available.

## Topics

### Miscellaneous
- [busCanDispatch](./ioatacontroller/api-1811873-buscandispatch.md)
  answers whether the bus is in state such that the next command can be dispatched.
- [dispatchNext](./ioatacontroller/api-1811887-dispatchnext.md)
  Causes the command at the front of the queue to dequeue, made the current command and begin execution.
- [handleCommand](./ioatacontroller/api-1811902-handlecommand.md)
  Called by executeCommand() to handle the client command from the workloop context.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./ioatacontroller/reserved.md)
### Instance Methods
- [- ATAPISecondaryExists](./ioatacontroller/api-3917635-atapisecondaryexists.md)
- [- ATAPISlaveExists](./ioatacontroller/api-1490687-atapislaveexists.md)
- [- allocateDoubleBuffer](./ioatacontroller/api-1490619-allocatedoublebuffer.md)
- [- asyncCommand](./ioatacontroller/api-1490682-asynccommand.md)
- [- asyncData](./ioatacontroller/api-1490697-asyncdata.md)
- [- asyncIO](./ioatacontroller/api-1490621-asyncio.md)
- [- asyncStatus](./ioatacontroller/api-1490643-asyncstatus.md)
- [- bitSigToNumeric](./ioatacontroller/api-1490639-bitsigtonumeric.md)
- [- busCanDispatch](./ioatacontroller/api-1490660-buscandispatch.md)
- [- checkTimeout](./ioatacontroller/api-1490701-checktimeout.md)
- [- completeIO](./ioatacontroller/api-1490684-completeio.md)
- [- configureTFPointers](./ioatacontroller/api-1490690-configuretfpointers.md)
- [- dequeueFirstCommand](./ioatacontroller/api-1490618-dequeuefirstcommand.md)
- [- determineATAPIState](./ioatacontroller/api-1490702-determineatapistate.md)
- [- dispatchNext](./ioatacontroller/api-1490645-dispatchnext.md)
- [- enqueueCommand](./ioatacontroller/api-1490655-enqueuecommand.md)
- [- executeCommand](./ioatacontroller/api-1490670-executecommand.md)
- [- executeEventCallouts](./ioatacontroller/api-1490623-executeeventcallouts.md)
- [- free](./ioatacontroller/api-1490669-free.md)
- [- getConfig](./ioatacontroller/api-1490665-getconfig.md)
- [- getMetaClass](./ioatacontroller/api-1490694-getmetaclass.md)
- [- handleBusReset](./ioatacontroller/api-1490710-handlebusreset.md)
- [- handleCommand](./ioatacontroller/api-1490650-handlecommand.md)
- [- handleDeviceInterrupt](./ioatacontroller/api-1490654-handledeviceinterrupt.md)
- [- handleExecIO](./ioatacontroller/api-1490663-handleexecio.md)
- [- handleOverrun](./ioatacontroller/api-1490706-handleoverrun.md)
- [- handleQueueFlush](./ioatacontroller/api-1490678-handlequeueflush.md)
- [- handleRegAccess](./ioatacontroller/api-1490708-handleregaccess.md)
- [- handleTimeout](./ioatacontroller/api-1490647-handletimeout.md)
- [- init](./ioatacontroller/api-1490629-init.md)
- [- issueCommand](./ioatacontroller/api-1490672-issuecommand.md)
- [- probe](./ioatacontroller/api-1490674-probe.md)
- [- provideBusInfo](./ioatacontroller/api-1490695-providebusinfo.md)
- [- readATAPIByteCount](./ioatacontroller/api-1490668-readatapibytecount.md)
- [- readExtRegister](./ioatacontroller/api-1490692-readextregister.md)
- [- readExtRegister](./ioatacontroller/api-3676014-readextregister.md)
- [- registerAccess](./ioatacontroller/api-1490637-registeraccess.md)
- [- scanForDrives](./ioatacontroller/api-1490649-scanfordrives.md)
- [- selectConfig](./ioatacontroller/api-1490626-selectconfig.md)
- [- selectDevice](./ioatacontroller/api-1490680-selectdevice.md)
- [- selectIOTiming](./ioatacontroller/api-1490666-selectiotiming.md)
- [- softResetBus](./ioatacontroller/api-1490635-softresetbus.md)
- [- start](./ioatacontroller/api-1490714-start.md)
- [- startDMA](./ioatacontroller/api-1490712-startdma.md)
- [- startTimer](./ioatacontroller/api-1490651-starttimer.md)
- [- stopDMA](./ioatacontroller/api-1490705-stopdma.md)
- [- stopTimer](./ioatacontroller/api-1490631-stoptimer.md)
- [- swapBytes16](./ioatacontroller/api-1490625-swapbytes16.md)
- [- synchronousIO](./ioatacontroller/api-1490703-synchronousio.md)
- [- txDataIn](./ioatacontroller/api-1490686-txdatain.md)
- [- txDataOut](./ioatacontroller/api-1490652-txdataout.md)
- [- waitForU8Status](./ioatacontroller/api-1490699-waitforu8status.md)
- [- writeExtRegister](./ioatacontroller/api-1490676-writeextregister.md)
- [- writeExtRegister](./ioatacontroller/api-3676015-writeextregister.md)
- [- writePacket](./ioatacontroller/api-1490642-writepacket.md)
### Type Methods
- [+ executeCommandAction](./ioatacontroller/api-1490634-executecommandaction.md)
- [+ timeoutOccured](./ioatacontroller/api-1490688-timeoutoccured.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacontroller)*