# IOSCSIReducedBlockCommandsDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOSCSIReducedBlockCommandsDevice : IOSCSIPrimaryCommandsDevice
```

## Topics

### Instance Methods
- [- AsyncReadWrite](./ioscsireducedblockcommandsdevice/api-1473305-asyncreadwrite.md)
- [- AsyncReadWriteCompletion](./ioscsireducedblockcommandsdevice/api-1473431-asyncreadwritecompletion.md)
- [- CheckMediaPresence](./ioscsireducedblockcommandsdevice/api-1473210-checkmediapresence.md)
- [- CheckWriteProtection](./ioscsireducedblockcommandsdevice/api-1473313-checkwriteprotection.md)
- [- ClearNotReadyStatus](./ioscsireducedblockcommandsdevice/api-1473303-clearnotreadystatus.md)
- [- CreateStorageServiceNub](./ioscsireducedblockcommandsdevice/api-1473416-createstorageservicenub.md)
- [- DetermineDeviceCharacteristics](./ioscsireducedblockcommandsdevice/api-1473295-determinedevicecharacteristics.md)
- [- DisablePolling](./ioscsireducedblockcommandsdevice/api-1473326-disablepolling.md)
- [- EjectTheMedia](./ioscsireducedblockcommandsdevice/api-1473407-ejectthemedia.md)
- [- EnablePolling](./ioscsireducedblockcommandsdevice/api-1473419-enablepolling.md)
- [- FORMAT_UNIT](./ioscsireducedblockcommandsdevice/api-1473330-format_unit.md)
- [- FormatMedia](./ioscsireducedblockcommandsdevice/api-1473262-formatmedia.md)
- [- GetFormatCapacities](./ioscsireducedblockcommandsdevice/api-1473288-getformatcapacities.md)
- [- GetInitialPowerState](./ioscsireducedblockcommandsdevice/api-1473252-getinitialpowerstate.md)
- [- GetNumberOfPowerStateTransitions](./ioscsireducedblockcommandsdevice/api-1473410-getnumberofpowerstatetransitions.md)
- [- HandleCheckPowerState](./ioscsireducedblockcommandsdevice/api-1473394-handlecheckpowerstate.md)
- [- HandlePowerChange](./ioscsireducedblockcommandsdevice/api-1473301-handlepowerchange.md)
- [- INQUIRY](./ioscsireducedblockcommandsdevice/api-1473207-inquiry.md)
- [- InitializeDeviceSupport](./ioscsireducedblockcommandsdevice/api-1473351-initializedevicesupport.md)
- [- InitializePowerManagement](./ioscsireducedblockcommandsdevice/api-1473413-initializepowermanagement.md)
- [- IssueRead](./ioscsireducedblockcommandsdevice/api-1473258-issueread.md)
- [- IssueRead](./ioscsireducedblockcommandsdevice/api-3516770-issueread.md)
- [- IssueWrite](./ioscsireducedblockcommandsdevice/api-1473192-issuewrite.md)
- [- IssueWrite](./ioscsireducedblockcommandsdevice/api-3516771-issuewrite.md)
- [- LockUnlockMedia](./ioscsireducedblockcommandsdevice/api-1473401-lockunlockmedia.md)
- [- MODE_SELECT_6](./ioscsireducedblockcommandsdevice/api-1473197-mode_select_6.md)
- [- MODE_SENSE_6](./ioscsireducedblockcommandsdevice/api-1473235-mode_sense_6.md)
- [- PERSISTENT_RESERVE_IN](./ioscsireducedblockcommandsdevice/api-1473376-persistent_reserve_in.md)
- [- PERSISTENT_RESERVE_OUT](./ioscsireducedblockcommandsdevice/api-1473265-persistent_reserve_out.md)
- [- PREVENT_ALLOW_MEDIUM_REMOVAL](./ioscsireducedblockcommandsdevice/api-1473423-prevent_allow_medium_removal.md)
- [- PollForMedia](./ioscsireducedblockcommandsdevice/api-1473386-pollformedia.md)
- [- PowerDownHandler](./ioscsireducedblockcommandsdevice/api-1473203-powerdownhandler.md)
- [- READ_10](./ioscsireducedblockcommandsdevice/api-1473322-read_10.md)
- [- READ_CAPACITY](./ioscsireducedblockcommandsdevice/api-1473356-read_capacity.md)
- [- RELEASE_6](./ioscsireducedblockcommandsdevice/api-1473278-release_6.md)
- [- REQUEST_SENSE](./ioscsireducedblockcommandsdevice/api-1473308-request_sense.md)
- [- RESERVE_6](./ioscsireducedblockcommandsdevice/api-1473379-reserve_6.md)
- [- ReportBlockSize](./ioscsireducedblockcommandsdevice/api-1473239-reportblocksize.md)
- [- ReportEjectability](./ioscsireducedblockcommandsdevice/api-1473214-reportejectability.md)
- [- ReportLockability](./ioscsireducedblockcommandsdevice/api-1473231-reportlockability.md)
- [- ReportMaxReadTransfer](./ioscsireducedblockcommandsdevice/api-1473298-reportmaxreadtransfer.md)
- [- ReportMaxValidBlock](./ioscsireducedblockcommandsdevice/api-1473302-reportmaxvalidblock.md)
- [- ReportMaxWriteTransfer](./ioscsireducedblockcommandsdevice/api-1473404-reportmaxwritetransfer.md)
- [- ReportMediaState](./ioscsireducedblockcommandsdevice/api-1473373-reportmediastate.md)
- [- ReportPollRequirements](./ioscsireducedblockcommandsdevice/api-1473390-reportpollrequirements.md)
- [- ReportRemovability](./ioscsireducedblockcommandsdevice/api-1473284-reportremovability.md)
- [- ReportWriteProtection](./ioscsireducedblockcommandsdevice/api-1473291-reportwriteprotection.md)
- [- ResetMediaCharacteristics](./ioscsireducedblockcommandsdevice/api-1473187-resetmediacharacteristics.md)
- [- ResumeDeviceSupport](./ioscsireducedblockcommandsdevice/api-1473275-resumedevicesupport.md)
- [- START_STOP_UNIT](./ioscsireducedblockcommandsdevice/api-1473222-start_stop_unit.md)
- [- SYNCHRONIZE_CACHE](./ioscsireducedblockcommandsdevice/api-1473360-synchronize_cache.md)
- [- SetMediaCharacteristics](./ioscsireducedblockcommandsdevice/api-1473254-setmediacharacteristics.md)
- [- SetMediaIcon](./ioscsireducedblockcommandsdevice/api-1473348-setmediaicon.md)
- [- StartDeviceSupport](./ioscsireducedblockcommandsdevice/api-1473200-startdevicesupport.md)
- [- StopDeviceSupport](./ioscsireducedblockcommandsdevice/api-1473342-stopdevicesupport.md)
- [- SuspendDeviceSupport](./ioscsireducedblockcommandsdevice/api-1473333-suspenddevicesupport.md)
- [- SyncReadWrite](./ioscsireducedblockcommandsdevice/api-1473245-syncreadwrite.md)
- [- SynchronizeCache](./ioscsireducedblockcommandsdevice/api-1473218-synchronizecache.md)
- [- TEST_UNIT_READY](./ioscsireducedblockcommandsdevice/api-1473367-test_unit_ready.md)
- [- TerminateDeviceSupport](./ioscsireducedblockcommandsdevice/api-1473272-terminatedevicesupport.md)
- [- TicklePowerManager](./ioscsireducedblockcommandsdevice/api-1473319-ticklepowermanager.md)
- [- VERIFY](./ioscsireducedblockcommandsdevice/api-1473382-verify.md)
- [- WRITE_10](./ioscsireducedblockcommandsdevice/api-1473316-write_10.md)
- [- WRITE_BUFFER](./ioscsireducedblockcommandsdevice/api-1473428-write_buffer.md)
- [- free](./ioscsireducedblockcommandsdevice/api-1473248-free.md)
- [- getMetaClass](./ioscsireducedblockcommandsdevice/api-1473227-getmetaclass.md)
### Type Methods
- [+ AsyncReadWriteComplete](./ioscsireducedblockcommandsdevice/api-1473269-asyncreadwritecomplete.md)
- [+ sPollForMedia](./ioscsireducedblockcommandsdevice/api-1473338-spollformedia.md)

## Relationships

### Inherits From
- [IOSCSIPrimaryCommandsDevice](./ioscsiprimarycommandsdevice.md)

## See Also

### Block Devices
- [IOSCSIPeripheralDeviceType00](./ioscsiperipheraldevicetype00.md)
- [IOSCSIPeripheralDeviceType07](./ioscsiperipheraldevicetype07.md)
- [IOSCSIPeripheralDeviceType0E](./ioscsiperipheraldevicetype0e.md)
- [IOSCSIBlockCommandsDevice](./ioscsiblockcommandsdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsireducedblockcommandsdevice)*