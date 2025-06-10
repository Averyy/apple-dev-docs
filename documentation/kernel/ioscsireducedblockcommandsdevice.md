# IOSCSIReducedBlockCommandsDevice

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOSCSIReducedBlockCommandsDevice : IOSCSIPrimaryCommandsDevice
```

## Topics

### Instance Methods
- [- AsyncReadWrite](ioscsireducedblockcommandsdevice/1473305-asyncreadwrite.md)
- [- AsyncReadWriteCompletion](ioscsireducedblockcommandsdevice/1473431-asyncreadwritecompletion.md)
- [- CheckMediaPresence](ioscsireducedblockcommandsdevice/1473210-checkmediapresence.md)
- [- CheckWriteProtection](ioscsireducedblockcommandsdevice/1473313-checkwriteprotection.md)
- [- ClearNotReadyStatus](ioscsireducedblockcommandsdevice/1473303-clearnotreadystatus.md)
- [- CreateStorageServiceNub](ioscsireducedblockcommandsdevice/1473416-createstorageservicenub.md)
- [- DetermineDeviceCharacteristics](ioscsireducedblockcommandsdevice/1473295-determinedevicecharacteristics.md)
- [- DisablePolling](ioscsireducedblockcommandsdevice/1473326-disablepolling.md)
- [- EjectTheMedia](ioscsireducedblockcommandsdevice/1473407-ejectthemedia.md)
- [- EnablePolling](ioscsireducedblockcommandsdevice/1473419-enablepolling.md)
- [- FORMAT_UNIT](ioscsireducedblockcommandsdevice/1473330-format_unit.md)
- [- FormatMedia](ioscsireducedblockcommandsdevice/1473262-formatmedia.md)
- [- GetFormatCapacities](ioscsireducedblockcommandsdevice/1473288-getformatcapacities.md)
- [- GetInitialPowerState](ioscsireducedblockcommandsdevice/1473252-getinitialpowerstate.md)
- [- GetNumberOfPowerStateTransitions](ioscsireducedblockcommandsdevice/1473410-getnumberofpowerstatetransitions.md)
- [- HandleCheckPowerState](ioscsireducedblockcommandsdevice/1473394-handlecheckpowerstate.md)
- [- HandlePowerChange](ioscsireducedblockcommandsdevice/1473301-handlepowerchange.md)
- [- INQUIRY](ioscsireducedblockcommandsdevice/1473207-inquiry.md)
- [- InitializeDeviceSupport](ioscsireducedblockcommandsdevice/1473351-initializedevicesupport.md)
- [- InitializePowerManagement](ioscsireducedblockcommandsdevice/1473413-initializepowermanagement.md)
- [- IssueRead](ioscsireducedblockcommandsdevice/1473258-issueread.md)
- [- IssueRead](ioscsireducedblockcommandsdevice/3516770-issueread.md)
- [- IssueWrite](ioscsireducedblockcommandsdevice/1473192-issuewrite.md)
- [- IssueWrite](ioscsireducedblockcommandsdevice/3516771-issuewrite.md)
- [- LockUnlockMedia](ioscsireducedblockcommandsdevice/1473401-lockunlockmedia.md)
- [- MODE_SELECT_6](ioscsireducedblockcommandsdevice/1473197-mode_select_6.md)
- [- MODE_SENSE_6](ioscsireducedblockcommandsdevice/1473235-mode_sense_6.md)
- [- PERSISTENT_RESERVE_IN](ioscsireducedblockcommandsdevice/1473376-persistent_reserve_in.md)
- [- PERSISTENT_RESERVE_OUT](ioscsireducedblockcommandsdevice/1473265-persistent_reserve_out.md)
- [- PREVENT_ALLOW_MEDIUM_REMOVAL](ioscsireducedblockcommandsdevice/1473423-prevent_allow_medium_removal.md)
- [- PollForMedia](ioscsireducedblockcommandsdevice/1473386-pollformedia.md)
- [- PowerDownHandler](ioscsireducedblockcommandsdevice/1473203-powerdownhandler.md)
- [- READ_10](ioscsireducedblockcommandsdevice/1473322-read_10.md)
- [- READ_CAPACITY](ioscsireducedblockcommandsdevice/1473356-read_capacity.md)
- [- RELEASE_6](ioscsireducedblockcommandsdevice/1473278-release_6.md)
- [- REQUEST_SENSE](ioscsireducedblockcommandsdevice/1473308-request_sense.md)
- [- RESERVE_6](ioscsireducedblockcommandsdevice/1473379-reserve_6.md)
- [- ReportBlockSize](ioscsireducedblockcommandsdevice/1473239-reportblocksize.md)
- [- ReportEjectability](ioscsireducedblockcommandsdevice/1473214-reportejectability.md)
- [- ReportLockability](ioscsireducedblockcommandsdevice/1473231-reportlockability.md)
- [- ReportMaxReadTransfer](ioscsireducedblockcommandsdevice/1473298-reportmaxreadtransfer.md)
- [- ReportMaxValidBlock](ioscsireducedblockcommandsdevice/1473302-reportmaxvalidblock.md)
- [- ReportMaxWriteTransfer](ioscsireducedblockcommandsdevice/1473404-reportmaxwritetransfer.md)
- [- ReportMediaState](ioscsireducedblockcommandsdevice/1473373-reportmediastate.md)
- [- ReportPollRequirements](ioscsireducedblockcommandsdevice/1473390-reportpollrequirements.md)
- [- ReportRemovability](ioscsireducedblockcommandsdevice/1473284-reportremovability.md)
- [- ReportWriteProtection](ioscsireducedblockcommandsdevice/1473291-reportwriteprotection.md)
- [- ResetMediaCharacteristics](ioscsireducedblockcommandsdevice/1473187-resetmediacharacteristics.md)
- [- ResumeDeviceSupport](ioscsireducedblockcommandsdevice/1473275-resumedevicesupport.md)
- [- START_STOP_UNIT](ioscsireducedblockcommandsdevice/1473222-start_stop_unit.md)
- [- SYNCHRONIZE_CACHE](ioscsireducedblockcommandsdevice/1473360-synchronize_cache.md)
- [- SetMediaCharacteristics](ioscsireducedblockcommandsdevice/1473254-setmediacharacteristics.md)
- [- SetMediaIcon](ioscsireducedblockcommandsdevice/1473348-setmediaicon.md)
- [- StartDeviceSupport](ioscsireducedblockcommandsdevice/1473200-startdevicesupport.md)
- [- StopDeviceSupport](ioscsireducedblockcommandsdevice/1473342-stopdevicesupport.md)
- [- SuspendDeviceSupport](ioscsireducedblockcommandsdevice/1473333-suspenddevicesupport.md)
- [- SyncReadWrite](ioscsireducedblockcommandsdevice/1473245-syncreadwrite.md)
- [- SynchronizeCache](ioscsireducedblockcommandsdevice/1473218-synchronizecache.md)
- [- TEST_UNIT_READY](ioscsireducedblockcommandsdevice/1473367-test_unit_ready.md)
- [- TerminateDeviceSupport](ioscsireducedblockcommandsdevice/1473272-terminatedevicesupport.md)
- [- TicklePowerManager](ioscsireducedblockcommandsdevice/1473319-ticklepowermanager.md)
- [- VERIFY](ioscsireducedblockcommandsdevice/1473382-verify.md)
- [- WRITE_10](ioscsireducedblockcommandsdevice/1473316-write_10.md)
- [- WRITE_BUFFER](ioscsireducedblockcommandsdevice/1473428-write_buffer.md)
- [- free](ioscsireducedblockcommandsdevice/1473248-free.md)
- [- getMetaClass](ioscsireducedblockcommandsdevice/1473227-getmetaclass.md)
### Type Methods
- [+ AsyncReadWriteComplete](ioscsireducedblockcommandsdevice/1473269-asyncreadwritecomplete.md)
- [+ sPollForMedia](ioscsireducedblockcommandsdevice/1473338-spollformedia.md)

## Relationships

### Inherits From
- [IOSCSIPrimaryCommandsDevice](ioscsiprimarycommandsdevice.md)

## See Also

- [IOSCSIPeripheralDeviceType00](ioscsiperipheraldevicetype00.md)
- [IOSCSIPeripheralDeviceType07](ioscsiperipheraldevicetype07.md)
- [IOSCSIPeripheralDeviceType0E](ioscsiperipheraldevicetype0e.md)
- [IOSCSIBlockCommandsDevice](ioscsiblockcommandsdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsireducedblockcommandsdevice)*