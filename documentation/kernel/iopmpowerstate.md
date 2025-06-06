# IOPMPowerState

**Framework**: Kernel  
**Kind**: struct

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOPMPowerState {
    ...
} IOPMPowerState;
```

## Topics

### Instance Properties
- [capabilityFlags](iopmpowerstate/1386965-capabilityflags.md)
  Describes the capability of the device in this state.
- [inputPowerRequirement](iopmpowerstate/1386979-inputpowerrequirement.md)
  Describes the input power required in this state.
- [outputPowerCharacter](iopmpowerstate/1386991-outputpowercharacter.md)
  Describes the power provided in this state.
- [powerDomainBudget](iopmpowerstate/1386971-powerdomainbudget.md)
  Describes power in milliWatts a domain in this state can deliver to its children. Unused; drivers may specify 0. }
- [powerToAttain](iopmpowerstate/1386975-powertoattain.md)
  Describes dditional power to attain this state from next lower state (in milliWatts). Unused; drivers may specify 0.
- [settleDownTime](iopmpowerstate/1386983-settledowntime.md)
  Settle time required after entering next lower state from this state (microseconds). Unused; drivers may specify 0.
- [settleUpTime](iopmpowerstate/1386989-settleuptime.md)
  Describes settle time required after entering this state from next lower state (microseconds). Unused; drivers may specify 0.
- [stateOrder](iopmpowerstate/1386977-stateorder.md)
  Valid in version kIOPMPowerStateVersion2 or greater of this structure. Defines ordering of power states independently of the power state ordinal.
- [staticPower](iopmpowerstate/1386967-staticpower.md)
  Describes average consumption in milliwatts. Unused; drivers may specify 0.
- [timeToAttain](iopmpowerstate/1386973-timetoattain.md)
  Describes time required to enter this state from next lower state (in microseconds). Unused; drivers may specify 0.
- [timeToLower](iopmpowerstate/1386981-timetolower.md)
  Describes time required to enter next lower state from this one (microseconds). Unused; drivers may specify 0.
- [version](iopmpowerstate/1386987-version.md)
  Defines version number of this struct. Just use the value "1" when defining an IOPMPowerState.

## See Also

- [IOACPIPlatformDevice](ioacpiplatformdevice.md)
- [IOACPIPlatformExpert](ioacpiplatformexpert.md)
- [IOPMPowerSource](iopmpowersource.md)
- [IOPMPowerSourceList](iopmpowersourcelist.md)
- [IOPMrootDomain](iopmrootdomain.md)
- [IOPowerConnection](iopowerconnection.md)
- [IOPwrController](iopwrcontroller.md)
- [IOACPIAddress](ioacpiaddress.md)
- [IOACPIAddressSpaceDescriptor](ioacpiaddressspacedescriptor.md)
- [IOACPIAddressSpaceHandler](ioacpiaddressspacehandler.md)
- [IOACPIAddressSpaceID](ioacpiaddressspaceid.md)
- [acknowledgeSleepWakeNotification](1579170-acknowledgesleepwakenotification.md)
- [gIOACPIAddressKey](gioacpiaddresskey.md)
- [gIOACPIDeviceStatusKey](gioacpidevicestatuskey.md)
- [gIOACPIHardwareIDKey](gioacpihardwareidkey.md)
- [gIOACPIPlane](gioacpiplane.md)
- [gIOACPIUniqueIDKey](gioacpiuniqueidkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmpowerstate)*