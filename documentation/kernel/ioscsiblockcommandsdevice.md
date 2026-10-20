# IOSCSIBlockCommandsDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOSCSIBlockCommandsDevice : IOSCSIPrimaryCommandsDevice
```

## Topics

### Instance Methods
- [- AsyncReadWrite](./ioscsiblockcommandsdevice/api-1521962-asyncreadwrite.md)
- [- AsyncReadWrite](./ioscsiblockcommandsdevice/api-3516743-asyncreadwrite.md)
- [- AsyncReadWriteCompletion](./ioscsiblockcommandsdevice/api-1522034-asyncreadwritecompletion.md)
- [- CheckMediumCapacityData](./ioscsiblockcommandsdevice/api-1522018-checkmediumcapacitydata.md)
- [- ClearNotReadyStatus](./ioscsiblockcommandsdevice/api-1521949-clearnotreadystatus.md)
- [- CreateStorageServiceNub](./ioscsiblockcommandsdevice/api-1521967-createstorageservicenub.md)
- [- DetermineDeviceCharacteristics](./ioscsiblockcommandsdevice/api-1521955-determinedevicecharacteristics.md)
- [- DetermineMediaPresence](./ioscsiblockcommandsdevice/api-1522025-determinemediapresence.md)
- [- DetermineMediumCapacity](./ioscsiblockcommandsdevice/api-1522010-determinemediumcapacity.md)
- [- DetermineMediumGeometry](./ioscsiblockcommandsdevice/api-1521994-determinemediumgeometry.md)
- [- DetermineMediumWriteProtectState](./ioscsiblockcommandsdevice/api-1522030-determinemediumwriteprotectstate.md)
- [- DisablePolling](./ioscsiblockcommandsdevice/api-1522035-disablepolling.md)
- [- EjectTheMedium](./ioscsiblockcommandsdevice/api-1521996-ejectthemedium.md)
- [- EnablePolling](./ioscsiblockcommandsdevice/api-1521982-enablepolling.md)
- [- FormatMedium](./ioscsiblockcommandsdevice/api-1521991-formatmedium.md)
- [- GET_LBA_STATUS](./ioscsiblockcommandsdevice/api-1792145-get_lba_status.md)
- [- GetDeviceUnmapCharacteristics](./ioscsiblockcommandsdevice/api-1792150-getdeviceunmapcharacteristics.md)
- [- GetFormatCapacities](./ioscsiblockcommandsdevice/api-1521936-getformatcapacities.md)
- [- GetInitialPowerState](./ioscsiblockcommandsdevice/api-1522028-getinitialpowerstate.md)
- [- GetMediumRotationRate](./ioscsiblockcommandsdevice/api-1522024-getmediumrotationrate.md)
- [- GetNumberOfPowerStateTransitions](./ioscsiblockcommandsdevice/api-1522002-getnumberofpowerstatetransitions.md)
- [- GetProvisionStatus](./ioscsiblockcommandsdevice/api-1792146-getprovisionstatus.md)
- [- GetWriteCacheState](./ioscsiblockcommandsdevice/api-1522023-getwritecachestate.md)
- [- GetWriteCacheState](./ioscsiblockcommandsdevice/api-3516744-getwritecachestate.md)
- [- HandleCheckPowerState](./ioscsiblockcommandsdevice/api-1521947-handlecheckpowerstate.md)
- [- HandlePowerChange](./ioscsiblockcommandsdevice/api-1521985-handlepowerchange.md)
- [- InitializeDeviceSupport](./ioscsiblockcommandsdevice/api-1521939-initializedevicesupport.md)
- [- InitializePowerManagement](./ioscsiblockcommandsdevice/api-1521984-initializepowermanagement.md)
- [- IsUnmapAllowed](./ioscsiblockcommandsdevice/api-1792132-isunmapallowed.md)
- [- IsUseWriteSame](./ioscsiblockcommandsdevice/api-1792143-isusewritesame.md)
- [- IssueRead](./ioscsiblockcommandsdevice/api-1521963-issueread.md)
- [- IssueRead](./ioscsiblockcommandsdevice/api-3516745-issueread.md)
- [- IssueUnmap](./ioscsiblockcommandsdevice/api-1792137-issueunmap.md)
- [- IssueWrite](./ioscsiblockcommandsdevice/api-1521940-issuewrite.md)
- [- IssueWrite](./ioscsiblockcommandsdevice/api-3516746-issuewrite.md)
- [- LockUnlockMedium](./ioscsiblockcommandsdevice/api-1522026-lockunlockmedium.md)
- [- LogicalBlockProvisioningUnmapSupport](./ioscsiblockcommandsdevice/api-1792151-logicalblockprovisioningunmapsup.md)
- [- PollForMediaRemoval](./ioscsiblockcommandsdevice/api-1521968-pollformediaremoval.md)
- [- PollForNewMedia](./ioscsiblockcommandsdevice/api-1522031-pollfornewmedia.md)
- [- PowerDownHandler](./ioscsiblockcommandsdevice/api-1522000-powerdownhandler.md)
- [- PreventMediumRemoval](./ioscsiblockcommandsdevice/api-1521990-preventmediumremoval.md)
- [- ProcessPoll](./ioscsiblockcommandsdevice/api-1522008-processpoll.md)
- [- READ_10](./ioscsiblockcommandsdevice/api-1522033-read_10.md)
- [- READ_10](./ioscsiblockcommandsdevice/api-3516747-read_10.md)
- [- READ_12](./ioscsiblockcommandsdevice/api-1522011-read_12.md)
- [- READ_12](./ioscsiblockcommandsdevice/api-3516748-read_12.md)
- [- READ_16](./ioscsiblockcommandsdevice/api-1522020-read_16.md)
- [- READ_CAPACITY](./ioscsiblockcommandsdevice/api-1521959-read_capacity.md)
- [- READ_CAPACITY_16](./ioscsiblockcommandsdevice/api-1521981-read_capacity_16.md)
- [- REPORT_PROVISIONING_INITIALIZATION_PATTERN](./ioscsiblockcommandsdevice/api-1792136-report_provisioning_initializati.md)
- [- ReportDeviceMaxBlocksReadTransfer](./ioscsiblockcommandsdevice/api-1522009-reportdevicemaxblocksreadtransfe.md)
- [- ReportDeviceMaxBlocksWriteTransfer](./ioscsiblockcommandsdevice/api-1521999-reportdevicemaxblockswritetransf.md)
- [- ReportDeviceMediaRemovability](./ioscsiblockcommandsdevice/api-1522029-reportdevicemediaremovability.md)
- [- ReportMediumBlockSize](./ioscsiblockcommandsdevice/api-1521989-reportmediumblocksize.md)
- [- ReportMediumTotalBlockCount](./ioscsiblockcommandsdevice/api-1521975-reportmediumtotalblockcount.md)
- [- ReportMediumWriteProtection](./ioscsiblockcommandsdevice/api-1521933-reportmediumwriteprotection.md)
- [- ReportProvisioningInitializationPattern](./ioscsiblockcommandsdevice/api-1792134-reportprovisioninginitialization.md)
- [- ResetMediumCharacteristics](./ioscsiblockcommandsdevice/api-1522007-resetmediumcharacteristics.md)
- [- ResumeDeviceSupport](./ioscsiblockcommandsdevice/api-1521961-resumedevicesupport.md)
- [- START_STOP_UNIT](./ioscsiblockcommandsdevice/api-1521932-start_stop_unit.md)
- [- SYNCHRONIZE_CACHE](./ioscsiblockcommandsdevice/api-1522004-synchronize_cache.md)
- [- SYNCHRONIZE_CACHE](./ioscsiblockcommandsdevice/api-3516749-synchronize_cache.md)
- [- SYNCRONIZE_CACHE_16](./ioscsiblockcommandsdevice/api-1521930-syncronize_cache_16.md)
- [- SetMediumCharacteristics](./ioscsiblockcommandsdevice/api-1521934-setmediumcharacteristics.md)
- [- SetMediumCharacteristics](./ioscsiblockcommandsdevice/api-3516750-setmediumcharacteristics.md)
- [- SetMediumIcon](./ioscsiblockcommandsdevice/api-1522012-setmediumicon.md)
- [- SetWriteCacheState](./ioscsiblockcommandsdevice/api-1521945-setwritecachestate.md)
- [- StartDeviceSupport](./ioscsiblockcommandsdevice/api-1522006-startdevicesupport.md)
- [- StopDeviceSupport](./ioscsiblockcommandsdevice/api-1521978-stopdevicesupport.md)
- [- SuspendDeviceSupport](./ioscsiblockcommandsdevice/api-1521953-suspenddevicesupport.md)
- [- SyncReadWrite](./ioscsiblockcommandsdevice/api-1521998-syncreadwrite.md)
- [- SynchronizeCache](./ioscsiblockcommandsdevice/api-1522017-synchronizecache.md)
- [- TerminateDeviceSupport](./ioscsiblockcommandsdevice/api-1521986-terminatedevicesupport.md)
- [- TicklePowerManager](./ioscsiblockcommandsdevice/api-1521942-ticklepowermanager.md)
- [- UNMAP](./ioscsiblockcommandsdevice/api-1792152-unmap.md)
- [- Unmap](./ioscsiblockcommandsdevice/api-1792147-unmap.md)
- [- UnmapTruncateAndAccumulate](./ioscsiblockcommandsdevice/api-1792131-unmaptruncateandaccumulate.md)
- [- UnmapTryExtentCoalesce](./ioscsiblockcommandsdevice/api-1792129-unmaptryextentcoalesce.md)
- [- UpdateLBAProvisionStatus](./ioscsiblockcommandsdevice/api-1792148-updatelbaprovisionstatus.md)
- [- VerifyMediumPresence](./ioscsiblockcommandsdevice/api-1521992-verifymediumpresence.md)
- [- WRITE_10](./ioscsiblockcommandsdevice/api-1521993-write_10.md)
- [- WRITE_10](./ioscsiblockcommandsdevice/api-3516751-write_10.md)
- [- WRITE_12](./ioscsiblockcommandsdevice/api-1521948-write_12.md)
- [- WRITE_12](./ioscsiblockcommandsdevice/api-3516752-write_12.md)
- [- WRITE_16](./ioscsiblockcommandsdevice/api-1521972-write_16.md)
- [- WRITE_SAME_10](./ioscsiblockcommandsdevice/api-1792140-write_same_10.md)
- [- WRITE_SAME_16](./ioscsiblockcommandsdevice/api-1792139-write_same_16.md)
- [- WriteSame](./ioscsiblockcommandsdevice/api-1792144-writesame.md)
- [- WriteSameUnmap](./ioscsiblockcommandsdevice/api-1792149-writesameunmap.md)
- [- free](./ioscsiblockcommandsdevice/api-1522027-free.md)
- [- getMetaClass](./ioscsiblockcommandsdevice/api-1521970-getmetaclass.md)
- [- message](./ioscsiblockcommandsdevice/api-1521995-message.md)
- [- systemWillShutdown](./ioscsiblockcommandsdevice/api-1521987-systemwillshutdown.md)
### Type Methods
- [+ AbortPMTransition](./ioscsiblockcommandsdevice/api-3921321-abortpmtransition.md)
- [+ AsyncReadWriteComplete](./ioscsiblockcommandsdevice/api-1521937-asyncreadwritecomplete.md)
- [+ sProcessPoll](./ioscsiblockcommandsdevice/api-1522001-sprocesspoll.md)

## Relationships

### Inherits From
- [IOSCSIPrimaryCommandsDevice](./ioscsiprimarycommandsdevice.md)

## See Also

### Block Devices
- [IOSCSIPeripheralDeviceType00](./ioscsiperipheraldevicetype00.md)
- [IOSCSIPeripheralDeviceType07](./ioscsiperipheraldevicetype07.md)
- [IOSCSIPeripheralDeviceType0E](./ioscsiperipheraldevicetype0e.md)
- [IOSCSIReducedBlockCommandsDevice](./ioscsireducedblockcommandsdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiblockcommandsdevice)*