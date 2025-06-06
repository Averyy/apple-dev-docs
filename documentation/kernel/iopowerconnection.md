# IOPowerConnection

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOPowerConnection : IOService
```

#### Overview

Do not use IOPowerConnection. This class is an implementation detail defined for IOPM's management of the IORegistry IOPower plane.

Only Kernel IOKit power management should reference the IOPowerConnection class.

## Topics

### Miscellaneous
- [childHasRequestedPower](iopowerconnection/1810220-childhasrequestedpower.md)
  Return the flag that says whether the child has called requestPowerDomainState.
- [getAwaitingAck](iopowerconnection/1810241-getawaitingack.md)
  Returns the awaitingAck variable.
- [getDesiredDomainState](iopowerconnection/1810268-getdesireddomainstate.md)
  Returns the desiredDomainState variable.
- [getPreventIdleSleepFlag](iopowerconnection/1810287-getpreventidlesleepflag.md)
  Returns the preventIdleSleepFlag variable.
- [getPreventSystemSleepFlag](iopowerconnection/1810313-getpreventsystemsleepflag.md)
  Returns the preventSystemSleepFlag variable.
- [getReadyFlag](iopowerconnection/1810329-getreadyflag.md)
  Returns the readyFlag variable.
- [parentCurrentPowerFlags](iopowerconnection/1810355-parentcurrentpowerflags.md)
  Returns the currentPowerFlags variable.
- [parentKnowsState](iopowerconnection/1810379-parentknowsstate.md)
  Returns the stateKnown variable.
- [setAwaitingAck](iopowerconnection/1810405-setawaitingack.md)
  Sets the awaitingAck variable.
- [setChildHasRequestedPower](iopowerconnection/1810436-setchildhasrequestedpower.md)
  Set the flag that says that the child has called requestPowerDomainState.
- [setDesiredDomainState](iopowerconnection/1810465-setdesireddomainstate.md)
  Sets the desiredDomainState variable.
- [setParentCurrentPowerFlags](iopowerconnection/1810489-setparentcurrentpowerflags.md)
  Sets the currentPowerFlags variable.
- [setParentKnowsState](iopowerconnection/1810522-setparentknowsstate.md)
  Sets the stateKnown variable.
- [setPreventIdleSleepFlag](iopowerconnection/1810555-setpreventidlesleepflag.md)
  Sets the preventIdleSleepFlag variable.
- [setPreventSystemSleepFlag](iopowerconnection/1810587-setpreventsystemsleepflag.md)
  Sets the preventSystemSleepFlag variable.
- [setReadyFlag](iopowerconnection/1810620-setreadyflag.md)
  Sets the readyFlag variable.
### Instance Variables
- [stateKnown](iopowerconnection/stateknown.md)
- [requestFlag](iopowerconnection/requestflag.md)
- [readyFlag](iopowerconnection/readyflag.md)
- [preventSystemSleepFlag](iopowerconnection/preventsystemsleepflag.md)
- [preventIdleSleepFlag](iopowerconnection/preventidlesleepflag.md)
- [desiredDomainState](iopowerconnection/desireddomainstate.md)
- [currentPowerFlags](iopowerconnection/currentpowerflags.md)
- [awaitingAck](iopowerconnection/awaitingack.md)
### Instance Methods
- [- childHasRequestedPower](iopowerconnection/1490506-childhasrequestedpower.md)
- [- getAwaitingAck](iopowerconnection/1490500-getawaitingack.md)
- [- getDesiredDomainState](iopowerconnection/1490484-getdesireddomainstate.md)
- [- getMetaClass](iopowerconnection/1490481-getmetaclass.md)
- [- getPreventIdleSleepFlag](iopowerconnection/1490489-getpreventidlesleepflag.md)
- [- getPreventSystemSleepFlag](iopowerconnection/1490490-getpreventsystemsleepflag.md)
- [- getReadyFlag](iopowerconnection/1490499-getreadyflag.md)
- [- parentCurrentPowerFlags](iopowerconnection/1490505-parentcurrentpowerflags.md)
- [- parentKnowsState](iopowerconnection/1490492-parentknowsstate.md)
- [- setAwaitingAck](iopowerconnection/1490485-setawaitingack.md)
- [- setChildHasRequestedPower](iopowerconnection/1490502-setchildhasrequestedpower.md)
- [- setDesiredDomainState](iopowerconnection/1490496-setdesireddomainstate.md)
- [- setParentCurrentPowerFlags](iopowerconnection/1490503-setparentcurrentpowerflags.md)
- [- setParentKnowsState](iopowerconnection/1490479-setparentknowsstate.md)
- [- setPreventIdleSleepFlag](iopowerconnection/1490508-setpreventidlesleepflag.md)
- [- setPreventSystemSleepFlag](iopowerconnection/1490483-setpreventsystemsleepflag.md)
- [- setReadyFlag](iopowerconnection/1490487-setreadyflag.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOACPIPlatformDevice](ioacpiplatformdevice.md)
- [IOACPIPlatformExpert](ioacpiplatformexpert.md)
- [IOPMPowerSource](iopmpowersource.md)
- [IOPMPowerSourceList](iopmpowersourcelist.md)
- [IOPMrootDomain](iopmrootdomain.md)
- [IOPwrController](iopwrcontroller.md)
- [IOACPIAddress](ioacpiaddress.md)
- [IOACPIAddressSpaceDescriptor](ioacpiaddressspacedescriptor.md)
- [IOACPIAddressSpaceHandler](ioacpiaddressspacehandler.md)
- [IOACPIAddressSpaceID](ioacpiaddressspaceid.md)
- [IOPMPowerState](iopmpowerstate.md)
- [acknowledgeSleepWakeNotification](1579170-acknowledgesleepwakenotification.md)
- [gIOACPIAddressKey](gioacpiaddresskey.md)
- [gIOACPIDeviceStatusKey](gioacpidevicestatuskey.md)
- [gIOACPIHardwareIDKey](gioacpihardwareidkey.md)
- [gIOACPIPlane](gioacpiplane.md)
- [gIOACPIUniqueIDKey](gioacpiuniqueidkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopowerconnection)*