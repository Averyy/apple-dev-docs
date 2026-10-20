# IOPMrootDomain

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOPMrootDomain : IOService
```

## Topics

### Instance Methods
- [- askChangeDown](./iopmrootdomain/api-1579191-askchangedown.md)
- [- callPlatformFunction](./iopmrootdomain/api-1579143-callplatformfunction.md)
- [- changePowerStateTo](./iopmrootdomain/api-1579182-changepowerstateto.md)
- [- changePowerStateToPriv](./iopmrootdomain/api-1579153-changepowerstatetopriv.md)
- [- claimSystemBootEvent](./iopmrootdomain/api-3553417-claimsystembootevent.md)
- [- claimSystemShutdownEvent](./iopmrootdomain/api-3674620-claimsystemshutdownevent.md)
- [- claimSystemWakeEvent](./iopmrootdomain/api-1579148-claimsystemwakeevent.md)
- [- configureReport](./iopmrootdomain/api-1579150-configurereport.md)
- [- configureReportGated](./iopmrootdomain/api-1579139-configurereportgated.md)
- [- copyPMSetting](./iopmrootdomain/api-1579190-copypmsetting.md)
- [- copyProperty](./iopmrootdomain/api-1579180-copyproperty.md)
- [- copyWakeReasonString](./iopmrootdomain/api-4320722-copywakereasonstring.md)
- [- createPMAssertion](./iopmrootdomain/api-1579132-createpmassertion.md)
- [- getAggressiveness](./iopmrootdomain/api-1579186-getaggressiveness.md)
- [- getMetaClass](./iopmrootdomain/api-1579165-getmetaclass.md)
- [- getPMAssertionLevel](./iopmrootdomain/api-1579141-getpmassertionlevel.md)
- [- getRUN_STATE](./iopmrootdomain/api-3113972-getrun_state.md)
- [- getSleepSupported](./iopmrootdomain/api-1579177-getsleepsupported.md)
- [- powerChangeDone](./iopmrootdomain/api-1579123-powerchangedone.md)
- [- publishFeature](./iopmrootdomain/api-1579147-publishfeature.md)
- [- publishFeature](./iopmrootdomain/api-3516721-publishfeature.md)
- [- receivePowerNotification](./iopmrootdomain/api-1579172-receivepowernotification.md)
- [- registerInterest](./iopmrootdomain/api-1579167-registerinterest.md)
- [- registerPMSettingController](./iopmrootdomain/api-1579179-registerpmsettingcontroller.md)
- [- registerPMSettingController](./iopmrootdomain/api-3516722-registerpmsettingcontroller.md)
- [- releasePMAssertion](./iopmrootdomain/api-1579135-releasepmassertion.md)
- [- removePublishedFeature](./iopmrootdomain/api-1579154-removepublishedfeature.md)
- [- requestPowerDomainState](./iopmrootdomain/api-1579174-requestpowerdomainstate.md)
- [- requestUserActive](./iopmrootdomain/api-3573961-requestuseractive.md)
- [- restartWithStackshot](./iopmrootdomain/api-1579138-restartwithstackshot.md)
- [- serializeProperties](./iopmrootdomain/api-1579183-serializeproperties.md)
- [- setAggressiveness](./iopmrootdomain/api-1579163-setaggressiveness.md)
- [- setPMAssertionLevel](./iopmrootdomain/api-1579151-setpmassertionlevel.md)
- [- setProperties](./iopmrootdomain/api-1579158-setproperties.md)
- [- setSleepSupported](./iopmrootdomain/api-1579128-setsleepsupported.md)
- [- setWakeTime](./iopmrootdomain/api-3113973-setwaketime.md)
- [- sleepSystem](./iopmrootdomain/api-1579178-sleepsystem.md)
- [- sleepSystemOptions](./iopmrootdomain/api-1579145-sleepsystemoptions.md)
- [- start](./iopmrootdomain/api-1579144-start.md)
- [- systemPowerEventOccurred](./iopmrootdomain/api-1579176-systempowereventoccurred.md)
- [- systemPowerEventOccurred](./iopmrootdomain/api-3516723-systempowereventoccurred.md)
- [- tellChangeDown](./iopmrootdomain/api-1579156-tellchangedown.md)
- [- tellChangeUp](./iopmrootdomain/api-1579159-tellchangeup.md)
- [- tellNoChangeDown](./iopmrootdomain/api-1579118-tellnochangedown.md)
- [- updateReport](./iopmrootdomain/api-1579185-updatereport.md)
- [- updateReportGated](./iopmrootdomain/api-1579142-updatereportgated.md)
- [- wakeFromDoze](./iopmrootdomain/api-1579122-wakefromdoze.md)
### Type Methods
- [+ construct](./iopmrootdomain/api-1579160-construct.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Power Management
- [IOACPIPlatformDevice](./ioacpiplatformdevice.md)
- [IOACPIPlatformExpert](./ioacpiplatformexpert.md)
- [IOPMPowerSource](./iopmpowersource.md)
- [IOPMPowerSourceList](./iopmpowersourcelist.md)
- [IOPowerConnection](./iopowerconnection.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmrootdomain)*