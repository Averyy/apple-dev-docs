# IOSCSIMultimediaCommandsDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOSCSIMultimediaCommandsDevice : IOSCSIPrimaryCommandsDevice
```

## Topics

### Instance Methods
- [- AsyncReadCD](./ioscsimultimediacommandsdevice/api-1576169-asyncreadcd.md)
- [- AsyncReadWrite](./ioscsimultimediacommandsdevice/api-1576318-asyncreadwrite.md)
- [- AsyncReadWriteCompletion](./ioscsimultimediacommandsdevice/api-1576295-asyncreadwritecompletion.md)
- [- CheckForBDMediaType](./ioscsimultimediacommandsdevice/api-1576313-checkforbdmediatype.md)
- [- CheckForCDMediaType](./ioscsimultimediacommandsdevice/api-1576285-checkforcdmediatype.md)
- [- CheckForDVDMediaType](./ioscsimultimediacommandsdevice/api-1576214-checkfordvdmediatype.md)
- [- CheckForLowPowerPollingSupport](./ioscsimultimediacommandsdevice/api-1576306-checkforlowpowerpollingsupport.md)
- [- CheckMediaPresence](./ioscsimultimediacommandsdevice/api-1576165-checkmediapresence.md)
- [- CheckWriteProtection](./ioscsimultimediacommandsdevice/api-1576220-checkwriteprotection.md)
- [- ClearNotReadyStatus](./ioscsimultimediacommandsdevice/api-1576256-clearnotreadystatus.md)
- [- ConvertBCDToHex](./ioscsimultimediacommandsdevice/api-1576263-convertbcdtohex.md)
- [- ConvertMSFToLBA](./ioscsimultimediacommandsdevice/api-1576328-convertmsftolba.md)
- [- CreateStorageServiceNub](./ioscsimultimediacommandsdevice/api-1576262-createstorageservicenub.md)
- [- DetermineDeviceCharacteristics](./ioscsimultimediacommandsdevice/api-1576310-determinedevicecharacteristics.md)
- [- DetermineDeviceFeatures](./ioscsimultimediacommandsdevice/api-1576334-determinedevicefeatures.md)
- [- DetermineIfMediaIsRemovable](./ioscsimultimediacommandsdevice/api-1576223-determineifmediaisremovable.md)
- [- DetermineMediaType](./ioscsimultimediacommandsdevice/api-1576176-determinemediatype.md)
- [- DisablePolling](./ioscsimultimediacommandsdevice/api-1576177-disablepolling.md)
- [- EjectTheMedia](./ioscsimultimediacommandsdevice/api-1576299-ejectthemedia.md)
- [- EnablePolling](./ioscsimultimediacommandsdevice/api-1576212-enablepolling.md)
- [- FormatMedia](./ioscsimultimediacommandsdevice/api-1576305-formatmedia.md)
- [- GET_CONFIGURATION](./ioscsimultimediacommandsdevice/api-1576303-get_configuration.md)
- [- GET_EVENT_STATUS_NOTIFICATION](./ioscsimultimediacommandsdevice/api-1576286-get_event_status_notification.md)
- [- GET_PERFORMANCE](./ioscsimultimediacommandsdevice/api-1576198-get_performance.md)
- [- GetBlockSize](./ioscsimultimediacommandsdevice/api-1576290-getblocksize.md)
- [- GetCurrentPowerStateOfDrive](./ioscsimultimediacommandsdevice/api-1576260-getcurrentpowerstateofdrive.md)
- [- GetDeviceConfiguration](./ioscsimultimediacommandsdevice/api-1576324-getdeviceconfiguration.md)
- [- GetDeviceConfigurationSize](./ioscsimultimediacommandsdevice/api-1576228-getdeviceconfigurationsize.md)
- [- GetFormatCapacities](./ioscsimultimediacommandsdevice/api-1576184-getformatcapacities.md)
- [- GetInitialPowerState](./ioscsimultimediacommandsdevice/api-1576352-getinitialpowerstate.md)
- [- GetMechanicalCapabilities](./ioscsimultimediacommandsdevice/api-1576297-getmechanicalcapabilities.md)
- [- GetMechanicalCapabilitiesSize](./ioscsimultimediacommandsdevice/api-1576327-getmechanicalcapabilitiessize.md)
- [- GetMediaAccessSpeed](./ioscsimultimediacommandsdevice/api-1576199-getmediaaccessspeed.md)
- [- GetMediaType](./ioscsimultimediacommandsdevice/api-1576302-getmediatype.md)
- [- GetNumberOfPowerStateTransitions](./ioscsimultimediacommandsdevice/api-1576155-getnumberofpowerstatetransitions.md)
- [- GetTrayState](./ioscsimultimediacommandsdevice/api-1576309-gettraystate.md)
- [- HandleCheckPowerState](./ioscsimultimediacommandsdevice/api-1576186-handlecheckpowerstate.md)
- [- HandlePowerChange](./ioscsimultimediacommandsdevice/api-1576233-handlepowerchange.md)
- [- HandleSetUserClientExclusivityState](./ioscsimultimediacommandsdevice/api-1576347-handlesetuserclientexclusivityst.md)
- [- InitializeDeviceSupport](./ioscsimultimediacommandsdevice/api-1576245-initializedevicesupport.md)
- [- InitializePowerManagement](./ioscsimultimediacommandsdevice/api-1576267-initializepowermanagement.md)
- [- IssueRead](./ioscsimultimediacommandsdevice/api-1576323-issueread.md)
- [- IssueRead](./ioscsimultimediacommandsdevice/api-3516753-issueread.md)
- [- IssueWrite](./ioscsimultimediacommandsdevice/api-1576304-issuewrite.md)
- [- IssueWrite](./ioscsimultimediacommandsdevice/api-3516754-issuewrite.md)
- [- LOAD_UNLOAD_MEDIUM](./ioscsimultimediacommandsdevice/api-1576201-load_unload_medium.md)
- [- LockUnlockMedia](./ioscsimultimediacommandsdevice/api-1576190-lockunlockmedia.md)
- [- MECHANISM_STATUS](./ioscsimultimediacommandsdevice/api-1576333-mechanism_status.md)
- [- ParseFeatureList](./ioscsimultimediacommandsdevice/api-1576200-parsefeaturelist.md)
- [- ParseMechanicalCapabilities](./ioscsimultimediacommandsdevice/api-1576191-parsemechanicalcapabilities.md)
- [- PollForMedia](./ioscsimultimediacommandsdevice/api-1576289-pollformedia.md)
- [- PowerDownHandler](./ioscsimultimediacommandsdevice/api-1576322-powerdownhandler.md)
- [- READ_10](./ioscsimultimediacommandsdevice/api-1576213-read_10.md)
- [- READ_CAPACITY](./ioscsimultimediacommandsdevice/api-1576194-read_capacity.md)
- [- READ_CD](./ioscsimultimediacommandsdevice/api-1576346-read_cd.md)
- [- READ_CD_MSF](./ioscsimultimediacommandsdevice/api-1576252-read_cd_msf.md)
- [- READ_DISC_INFORMATION](./ioscsimultimediacommandsdevice/api-1576281-read_disc_information.md)
- [- READ_DISC_STRUCTURE](./ioscsimultimediacommandsdevice/api-1576170-read_disc_structure.md)
- [- READ_DVD_STRUCTURE](./ioscsimultimediacommandsdevice/api-1576192-read_dvd_structure.md)
- [- READ_FORMAT_CAPACITIES](./ioscsimultimediacommandsdevice/api-1576224-read_format_capacities.md)
- [- READ_SUB_CHANNEL](./ioscsimultimediacommandsdevice/api-1576342-read_sub_channel.md)
- [- READ_TOC_PMA_ATIP](./ioscsimultimediacommandsdevice/api-1576197-read_toc_pma_atip.md)
- [- READ_TRACK_INFORMATION](./ioscsimultimediacommandsdevice/api-1576331-read_track_information.md)
- [- REPORT_KEY_V2](./ioscsimultimediacommandsdevice/api-1576242-report_key_v2.md)
- [- REPORT_KEY_V3](./ioscsimultimediacommandsdevice/api-1911645-report_key_v3.md)
- [- RESERVE_TRACK_V2](./ioscsimultimediacommandsdevice/api-1576247-reserve_track_v2.md)
- [- ReadDVDStructure](./ioscsimultimediacommandsdevice/api-1576236-readdvdstructure.md)
- [- ReadDiscInfo](./ioscsimultimediacommandsdevice/api-1576171-readdiscinfo.md)
- [- ReadDiscStructure](./ioscsimultimediacommandsdevice/api-1576273-readdiscstructure.md)
- [- ReadISRC](./ioscsimultimediacommandsdevice/api-1576280-readisrc.md)
- [- ReadMCN](./ioscsimultimediacommandsdevice/api-1576231-readmcn.md)
- [- ReadTOC](./ioscsimultimediacommandsdevice/api-1576156-readtoc.md)
- [- ReadTOC](./ioscsimultimediacommandsdevice/api-3516755-readtoc.md)
- [- ReadTrackInfo](./ioscsimultimediacommandsdevice/api-1576278-readtrackinfo.md)
- [- ReportBlockSize](./ioscsimultimediacommandsdevice/api-1576282-reportblocksize.md)
- [- ReportEjectability](./ioscsimultimediacommandsdevice/api-1576240-reportejectability.md)
- [- ReportKey](./ioscsimultimediacommandsdevice/api-4520029-reportkey.md)
- [- ReportKey](./ioscsimultimediacommandsdevice/api-4520030-reportkey.md)
- [- ReportLockability](./ioscsimultimediacommandsdevice/api-1576354-reportlockability.md)
- [- ReportMaxReadTransfer](./ioscsimultimediacommandsdevice/api-1576207-reportmaxreadtransfer.md)
- [- ReportMaxValidBlock](./ioscsimultimediacommandsdevice/api-1576226-reportmaxvalidblock.md)
- [- ReportMaxWriteTransfer](./ioscsimultimediacommandsdevice/api-1576195-reportmaxwritetransfer.md)
- [- ReportMediaState](./ioscsimultimediacommandsdevice/api-1576330-reportmediastate.md)
- [- ReportPollRequirements](./ioscsimultimediacommandsdevice/api-1576326-reportpollrequirements.md)
- [- ReportRemovability](./ioscsimultimediacommandsdevice/api-1576272-reportremovability.md)
- [- ReportWriteProtection](./ioscsimultimediacommandsdevice/api-1576301-reportwriteprotection.md)
- [- RequestIdle](./ioscsimultimediacommandsdevice/api-1576209-requestidle.md)
- [- ReserveTrack](./ioscsimultimediacommandsdevice/api-1576284-reservetrack.md)
- [- ResetMediaCharacteristics](./ioscsimultimediacommandsdevice/api-1576167-resetmediacharacteristics.md)
- [- ResumeDeviceSupport](./ioscsimultimediacommandsdevice/api-1576269-resumedevicesupport.md)
- [- SEND_KEY_V2](./ioscsimultimediacommandsdevice/api-1576216-send_key_v2.md)
- [- SET_CD_SPEED](./ioscsimultimediacommandsdevice/api-1576315-set_cd_speed.md)
- [- SET_READ_AHEAD](./ioscsimultimediacommandsdevice/api-1576187-set_read_ahead.md)
- [- SET_STREAMING](./ioscsimultimediacommandsdevice/api-1576271-set_streaming.md)
- [- START_STOP_UNIT](./ioscsimultimediacommandsdevice/api-1576210-start_stop_unit.md)
- [- SYNCHRONIZE_CACHE](./ioscsimultimediacommandsdevice/api-1576261-synchronize_cache.md)
- [- SendKey](./ioscsimultimediacommandsdevice/api-1576204-sendkey.md)
- [- SetMediaAccessSpeed](./ioscsimultimediacommandsdevice/api-1576215-setmediaaccessspeed.md)
- [- SetMediaCharacteristics](./ioscsimultimediacommandsdevice/api-1576345-setmediacharacteristics.md)
- [- SetPollingMode](./ioscsimultimediacommandsdevice/api-1576312-setpollingmode.md)
- [- SetTrayState](./ioscsimultimediacommandsdevice/api-1576250-settraystate.md)
- [- StartDeviceSupport](./ioscsimultimediacommandsdevice/api-1576293-startdevicesupport.md)
- [- StopDeviceSupport](./ioscsimultimediacommandsdevice/api-1576203-stopdevicesupport.md)
- [- SuspendDeviceSupport](./ioscsimultimediacommandsdevice/api-1576159-suspenddevicesupport.md)
- [- SyncReadWrite](./ioscsimultimediacommandsdevice/api-1576178-syncreadwrite.md)
- [- SynchronizeCache](./ioscsimultimediacommandsdevice/api-1576268-synchronizecache.md)
- [- TerminateDeviceSupport](./ioscsimultimediacommandsdevice/api-1576249-terminatedevicesupport.md)
- [- TicklePowerManager](./ioscsimultimediacommandsdevice/api-1576251-ticklepowermanager.md)
- [- VerifyDeviceState](./ioscsimultimediacommandsdevice/api-1576353-verifydevicestate.md)
- [- WRITE_10](./ioscsimultimediacommandsdevice/api-1576243-write_10.md)
- [- WRITE_AND_VERIFY_10](./ioscsimultimediacommandsdevice/api-1576294-write_and_verify_10.md)
- [- free](./ioscsimultimediacommandsdevice/api-1576234-free.md)
- [- getMetaClass](./ioscsimultimediacommandsdevice/api-1576248-getmetaclass.md)
- [- setAggressiveness](./ioscsimultimediacommandsdevice/api-1576239-setaggressiveness.md)
- [- setProperties](./ioscsimultimediacommandsdevice/api-1576179-setproperties.md)
### Type Methods
- [+ AsyncReadWriteComplete](./ioscsimultimediacommandsdevice/api-1576339-asyncreadwritecomplete.md)
- [+ sPollForMedia](./ioscsimultimediacommandsdevice/api-1576237-spollformedia.md)

## Relationships

### Inherits From
- [IOSCSIPrimaryCommandsDevice](./ioscsiprimarycommandsdevice.md)

## See Also

### Multimedia Devices
- [IOSCSILogicalUnitNub](./ioscsilogicalunitnub.md)
- [IOSCSIParallelInterfaceController](./ioscsiparallelinterfacecontroller.md)
  Class that represents a SCSI Host Bus Adapter.
- [IOSCSIPeripheralDeviceType05](./ioscsiperipheraldevicetype05.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice)*