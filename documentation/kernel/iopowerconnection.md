# IOPowerConnection

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOPowerConnection : IOService
```

#### Overview

Do not use IOPowerConnection. This class is an implementation detail defined for IOPM's management of the IORegistry IOPower plane.

Only Kernel IOKit power management should reference the IOPowerConnection class.

## Topics

### Miscellaneous
- [childHasRequestedPower](./iopowerconnection/api-1810220-childhasrequestedpower.md)
  Return the flag that says whether the child has called requestPowerDomainState.
- [getAwaitingAck](./iopowerconnection/api-1810241-getawaitingack.md)
  Returns the awaitingAck variable.
- [getDesiredDomainState](./iopowerconnection/api-1810268-getdesireddomainstate.md)
  Returns the desiredDomainState variable.
- [getPreventIdleSleepFlag](./iopowerconnection/api-1810287-getpreventidlesleepflag.md)
  Returns the preventIdleSleepFlag variable.
- [getPreventSystemSleepFlag](./iopowerconnection/api-1810313-getpreventsystemsleepflag.md)
  Returns the preventSystemSleepFlag variable.
- [getReadyFlag](./iopowerconnection/api-1810329-getreadyflag.md)
  Returns the readyFlag variable.
- [parentCurrentPowerFlags](./iopowerconnection/api-1810355-parentcurrentpowerflags.md)
  Returns the currentPowerFlags variable.
- [parentKnowsState](./iopowerconnection/api-1810379-parentknowsstate.md)
  Returns the stateKnown variable.
- [setAwaitingAck](./iopowerconnection/api-1810405-setawaitingack.md)
  Sets the awaitingAck variable.
- [setChildHasRequestedPower](./iopowerconnection/api-1810436-setchildhasrequestedpower.md)
  Set the flag that says that the child has called requestPowerDomainState.
- [setDesiredDomainState](./iopowerconnection/api-1810465-setdesireddomainstate.md)
  Sets the desiredDomainState variable.
- [setParentCurrentPowerFlags](./iopowerconnection/api-1810489-setparentcurrentpowerflags.md)
  Sets the currentPowerFlags variable.
- [setParentKnowsState](./iopowerconnection/api-1810522-setparentknowsstate.md)
  Sets the stateKnown variable.
- [setPreventIdleSleepFlag](./iopowerconnection/api-1810555-setpreventidlesleepflag.md)
  Sets the preventIdleSleepFlag variable.
- [setPreventSystemSleepFlag](./iopowerconnection/api-1810587-setpreventsystemsleepflag.md)
  Sets the preventSystemSleepFlag variable.
- [setReadyFlag](./iopowerconnection/api-1810620-setreadyflag.md)
  Sets the readyFlag variable.
### Instance Variables
- [stateKnown](./iopowerconnection/stateknown.md)
- [requestFlag](./iopowerconnection/requestflag.md)
- [readyFlag](./iopowerconnection/readyflag.md)
- [preventSystemSleepFlag](./iopowerconnection/preventsystemsleepflag.md)
- [preventIdleSleepFlag](./iopowerconnection/preventidlesleepflag.md)
- [desiredDomainState](./iopowerconnection/desireddomainstate.md)
- [currentPowerFlags](./iopowerconnection/currentpowerflags.md)
- [awaitingAck](./iopowerconnection/awaitingack.md)
### Instance Methods
- [- childHasRequestedPower](./iopowerconnection/api-1490506-childhasrequestedpower.md)
- [- getAwaitingAck](./iopowerconnection/api-1490500-getawaitingack.md)
- [- getDesiredDomainState](./iopowerconnection/api-1490484-getdesireddomainstate.md)
- [- getMetaClass](./iopowerconnection/api-1490481-getmetaclass.md)
- [- getPreventIdleSleepFlag](./iopowerconnection/api-1490489-getpreventidlesleepflag.md)
- [- getPreventSystemSleepFlag](./iopowerconnection/api-1490490-getpreventsystemsleepflag.md)
- [- getReadyFlag](./iopowerconnection/api-1490499-getreadyflag.md)
- [- parentCurrentPowerFlags](./iopowerconnection/api-1490505-parentcurrentpowerflags.md)
- [- parentKnowsState](./iopowerconnection/api-1490492-parentknowsstate.md)
- [- setAwaitingAck](./iopowerconnection/api-1490485-setawaitingack.md)
- [- setChildHasRequestedPower](./iopowerconnection/api-1490502-setchildhasrequestedpower.md)
- [- setDesiredDomainState](./iopowerconnection/api-1490496-setdesireddomainstate.md)
- [- setParentCurrentPowerFlags](./iopowerconnection/api-1490503-setparentcurrentpowerflags.md)
- [- setParentKnowsState](./iopowerconnection/api-1490479-setparentknowsstate.md)
- [- setPreventIdleSleepFlag](./iopowerconnection/api-1490508-setpreventidlesleepflag.md)
- [- setPreventSystemSleepFlag](./iopowerconnection/api-1490483-setpreventsystemsleepflag.md)
- [- setReadyFlag](./iopowerconnection/api-1490487-setreadyflag.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Power Management
- [IOACPIPlatformDevice](./ioacpiplatformdevice.md)
- [IOACPIPlatformExpert](./ioacpiplatformexpert.md)
- [IOPMPowerSource](./iopmpowersource.md)
- [IOPMPowerSourceList](./iopmpowersourcelist.md)
- [IOPMrootDomain](./iopmrootdomain.md)
- [IOPwrController](./iopwrcontroller.md)
- [IOACPIAddress](./ioacpiaddress.md)
- [IOACPIAddressSpaceDescriptor](./ioacpiaddressspacedescriptor.md)
- [IOACPIAddressSpaceHandler](./ioacpiaddressspacehandler.md)
- [IOACPIAddressSpaceID](./ioacpiaddressspaceid.md)
- [IOPMPowerState](./iopmpowerstate.md)
- [acknowledgeSleepWakeNotification](./api-1579170-acknowledgesleepwakenotification.md)
- [gIOACPIAddressKey](./gioacpiaddresskey.md)
- [gIOACPIDeviceStatusKey](./gioacpidevicestatuskey.md)
- [gIOACPIHardwareIDKey](./gioacpihardwareidkey.md)
- [gIOACPIPlane](./gioacpiplane.md)
- [gIOACPIUniqueIDKey](./gioacpiuniqueidkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopowerconnection)*