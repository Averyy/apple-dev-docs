# IOSCSIBlockCommandsDevice

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOSCSIBlockCommandsDevice : IOSCSIPrimaryCommandsDevice
```

## Topics

### Instance Methods
- [- AsyncReadWrite](ioscsiblockcommandsdevice/1521962-asyncreadwrite.md)
- [- AsyncReadWrite](ioscsiblockcommandsdevice/3516743-asyncreadwrite.md)
- [- AsyncReadWriteCompletion](ioscsiblockcommandsdevice/1522034-asyncreadwritecompletion.md)
- [- CheckMediumCapacityData](ioscsiblockcommandsdevice/1522018-checkmediumcapacitydata.md)
- [- ClearNotReadyStatus](ioscsiblockcommandsdevice/1521949-clearnotreadystatus.md)
- [- CreateStorageServiceNub](ioscsiblockcommandsdevice/1521967-createstorageservicenub.md)
- [- DetermineDeviceCharacteristics](ioscsiblockcommandsdevice/1521955-determinedevicecharacteristics.md)
- [- DetermineMediaPresence](ioscsiblockcommandsdevice/1522025-determinemediapresence.md)
- [- DetermineMediumCapacity](ioscsiblockcommandsdevice/1522010-determinemediumcapacity.md)
- [- DetermineMediumGeometry](ioscsiblockcommandsdevice/1521994-determinemediumgeometry.md)
- [- DetermineMediumWriteProtectState](ioscsiblockcommandsdevice/1522030-determinemediumwriteprotectstate.md)
- [- DisablePolling](ioscsiblockcommandsdevice/1522035-disablepolling.md)
- [- EjectTheMedium](ioscsiblockcommandsdevice/1521996-ejectthemedium.md)
- [- EnablePolling](ioscsiblockcommandsdevice/1521982-enablepolling.md)
- [- FormatMedium](ioscsiblockcommandsdevice/1521991-formatmedium.md)
- [- GET_LBA_STATUS](ioscsiblockcommandsdevice/1792145-get_lba_status.md)
- [- GetDeviceUnmapCharacteristics](ioscsiblockcommandsdevice/1792150-getdeviceunmapcharacteristics.md)
- [- GetFormatCapacities](ioscsiblockcommandsdevice/1521936-getformatcapacities.md)
- [- GetInitialPowerState](ioscsiblockcommandsdevice/1522028-getinitialpowerstate.md)
- [- GetMediumRotationRate](ioscsiblockcommandsdevice/1522024-getmediumrotationrate.md)
- [- GetNumberOfPowerStateTransitions](ioscsiblockcommandsdevice/1522002-getnumberofpowerstatetransitions.md)
- [- GetProvisionStatus](ioscsiblockcommandsdevice/1792146-getprovisionstatus.md)
- [- GetWriteCacheState](ioscsiblockcommandsdevice/1522023-getwritecachestate.md)
- [- GetWriteCacheState](ioscsiblockcommandsdevice/3516744-getwritecachestate.md)
- [- HandleCheckPowerState](ioscsiblockcommandsdevice/1521947-handlecheckpowerstate.md)
- [- HandlePowerChange](ioscsiblockcommandsdevice/1521985-handlepowerchange.md)
- [- InitializeDeviceSupport](ioscsiblockcommandsdevice/1521939-initializedevicesupport.md)
- [- InitializePowerManagement](ioscsiblockcommandsdevice/1521984-initializepowermanagement.md)
- [- IsUnmapAllowed](ioscsiblockcommandsdevice/1792132-isunmapallowed.md)
- [- IsUseWriteSame](ioscsiblockcommandsdevice/1792143-isusewritesame.md)
- [- IssueRead](ioscsiblockcommandsdevice/1521963-issueread.md)
- [- IssueRead](ioscsiblockcommandsdevice/3516745-issueread.md)
- [- IssueUnmap](ioscsiblockcommandsdevice/1792137-issueunmap.md)
- [- IssueWrite](ioscsiblockcommandsdevice/1521940-issuewrite.md)
- [- IssueWrite](ioscsiblockcommandsdevice/3516746-issuewrite.md)
- [- LockUnlockMedium](ioscsiblockcommandsdevice/1522026-lockunlockmedium.md)
- [- LogicalBlockProvisioningUnmapSupport](ioscsiblockcommandsdevice/1792151-logicalblockprovisioningunmapsup.md)
- [- PollForMediaRemoval](ioscsiblockcommandsdevice/1521968-pollformediaremoval.md)
- [- PollForNewMedia](ioscsiblockcommandsdevice/1522031-pollfornewmedia.md)
- [- PowerDownHandler](ioscsiblockcommandsdevice/1522000-powerdownhandler.md)
- [- PreventMediumRemoval](ioscsiblockcommandsdevice/1521990-preventmediumremoval.md)
- [- ProcessPoll](ioscsiblockcommandsdevice/1522008-processpoll.md)
- [- READ_10](ioscsiblockcommandsdevice/1522033-read_10.md)
- [- READ_10](ioscsiblockcommandsdevice/3516747-read_10.md)
- [- READ_12](ioscsiblockcommandsdevice/1522011-read_12.md)
- [- READ_12](ioscsiblockcommandsdevice/3516748-read_12.md)
- [- READ_16](ioscsiblockcommandsdevice/1522020-read_16.md)
- [- READ_CAPACITY](ioscsiblockcommandsdevice/1521959-read_capacity.md)
- [- READ_CAPACITY_16](ioscsiblockcommandsdevice/1521981-read_capacity_16.md)
- [- REPORT_PROVISIONING_INITIALIZATION_PATTERN](ioscsiblockcommandsdevice/1792136-report_provisioning_initializati.md)
- [- ReportDeviceMaxBlocksReadTransfer](ioscsiblockcommandsdevice/1522009-reportdevicemaxblocksreadtransfe.md)
- [- ReportDeviceMaxBlocksWriteTransfer](ioscsiblockcommandsdevice/1521999-reportdevicemaxblockswritetransf.md)
- [- ReportDeviceMediaRemovability](ioscsiblockcommandsdevice/1522029-reportdevicemediaremovability.md)
- [- ReportMediumBlockSize](ioscsiblockcommandsdevice/1521989-reportmediumblocksize.md)
- [- ReportMediumTotalBlockCount](ioscsiblockcommandsdevice/1521975-reportmediumtotalblockcount.md)
- [- ReportMediumWriteProtection](ioscsiblockcommandsdevice/1521933-reportmediumwriteprotection.md)
- [- ReportProvisioningInitializationPattern](ioscsiblockcommandsdevice/1792134-reportprovisioninginitialization.md)
- [- ResetMediumCharacteristics](ioscsiblockcommandsdevice/1522007-resetmediumcharacteristics.md)
- [- ResumeDeviceSupport](ioscsiblockcommandsdevice/1521961-resumedevicesupport.md)
- [- START_STOP_UNIT](ioscsiblockcommandsdevice/1521932-start_stop_unit.md)
- [- SYNCHRONIZE_CACHE](ioscsiblockcommandsdevice/1522004-synchronize_cache.md)
- [- SYNCHRONIZE_CACHE](ioscsiblockcommandsdevice/3516749-synchronize_cache.md)
- [- SYNCRONIZE_CACHE_16](ioscsiblockcommandsdevice/1521930-syncronize_cache_16.md)
- [- SetMediumCharacteristics](ioscsiblockcommandsdevice/1521934-setmediumcharacteristics.md)
- [- SetMediumCharacteristics](ioscsiblockcommandsdevice/3516750-setmediumcharacteristics.md)
- [- SetMediumIcon](ioscsiblockcommandsdevice/1522012-setmediumicon.md)
- [- SetWriteCacheState](ioscsiblockcommandsdevice/1521945-setwritecachestate.md)
- [- StartDeviceSupport](ioscsiblockcommandsdevice/1522006-startdevicesupport.md)
- [- StopDeviceSupport](ioscsiblockcommandsdevice/1521978-stopdevicesupport.md)
- [- SuspendDeviceSupport](ioscsiblockcommandsdevice/1521953-suspenddevicesupport.md)
- [- SyncReadWrite](ioscsiblockcommandsdevice/1521998-syncreadwrite.md)
- [- SynchronizeCache](ioscsiblockcommandsdevice/1522017-synchronizecache.md)
- [- TerminateDeviceSupport](ioscsiblockcommandsdevice/1521986-terminatedevicesupport.md)
- [- TicklePowerManager](ioscsiblockcommandsdevice/1521942-ticklepowermanager.md)
- [- UNMAP](ioscsiblockcommandsdevice/1792152-unmap.md)
- [- Unmap](ioscsiblockcommandsdevice/1792147-unmap.md)
- [- UnmapTruncateAndAccumulate](ioscsiblockcommandsdevice/1792131-unmaptruncateandaccumulate.md)
- [- UnmapTryExtentCoalesce](ioscsiblockcommandsdevice/1792129-unmaptryextentcoalesce.md)
- [- UpdateLBAProvisionStatus](ioscsiblockcommandsdevice/1792148-updatelbaprovisionstatus.md)
- [- VerifyMediumPresence](ioscsiblockcommandsdevice/1521992-verifymediumpresence.md)
- [- WRITE_10](ioscsiblockcommandsdevice/1521993-write_10.md)
- [- WRITE_10](ioscsiblockcommandsdevice/3516751-write_10.md)
- [- WRITE_12](ioscsiblockcommandsdevice/1521948-write_12.md)
- [- WRITE_12](ioscsiblockcommandsdevice/3516752-write_12.md)
- [- WRITE_16](ioscsiblockcommandsdevice/1521972-write_16.md)
- [- WRITE_SAME_10](ioscsiblockcommandsdevice/1792140-write_same_10.md)
- [- WRITE_SAME_16](ioscsiblockcommandsdevice/1792139-write_same_16.md)
- [- WriteSame](ioscsiblockcommandsdevice/1792144-writesame.md)
- [- WriteSameUnmap](ioscsiblockcommandsdevice/1792149-writesameunmap.md)
- [- free](ioscsiblockcommandsdevice/1522027-free.md)
- [- getMetaClass](ioscsiblockcommandsdevice/1521970-getmetaclass.md)
- [- message](ioscsiblockcommandsdevice/1521995-message.md)
- [- systemWillShutdown](ioscsiblockcommandsdevice/1521987-systemwillshutdown.md)
### Type Methods
- [+ AbortPMTransition](ioscsiblockcommandsdevice/3921321-abortpmtransition.md)
- [+ AsyncReadWriteComplete](ioscsiblockcommandsdevice/1521937-asyncreadwritecomplete.md)
- [+ sProcessPoll](ioscsiblockcommandsdevice/1522001-sprocesspoll.md)

## Relationships

### Inherits From
- [IOSCSIPrimaryCommandsDevice](ioscsiprimarycommandsdevice.md)

## See Also

- [IOSCSIPeripheralDeviceType00](ioscsiperipheraldevicetype00.md)
- [IOSCSIPeripheralDeviceType07](ioscsiperipheraldevicetype07.md)
- [IOSCSIPeripheralDeviceType0E](ioscsiperipheraldevicetype0e.md)
- [IOSCSIReducedBlockCommandsDevice](ioscsireducedblockcommandsdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice)*