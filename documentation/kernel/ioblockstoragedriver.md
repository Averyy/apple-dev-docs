# IOBlockStorageDriver

**Framework**: Kernel  
**Kind**: cl

The common base class for generic block storage drivers.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOBlockStorageDriver : IOStorage
```

#### Overview

The IOBlockStorageDriver class is the common base class for generic block storage drivers. It matches and communicates via an IOBlockStorageDevice interface, and connects to the remainder of the storage framework via the IOStorage protocol. It extends the IOStorage protocol by implementing the appropriate open and close semantics, deblocking for unaligned transfers, polling for ejectable media, locking and ejection policies, media object creation and tear-down, and statistics gathering and reporting.

Block storage drivers are split into two parts: the generic driver handles all generic device issues, independent of the lower-level transport mechanism (e.g. SCSI, ATA, USB, FireWire). All storage operations at the generic driver level are translated into a series of generic device operations. These operations are passed via the IOBlockStorageDevice nub to a transport driver, which implements the appropriate transport-dependent protocol to execute these operations.

To determine the write-protect state of a device (or media), for example, the generic driver would issue a call to the Transport Driver's reportWriteProtection method. If this were a SCSI device, its transport driver would issue a Mode Sense command to extract the write-protection status bit. The transport driver then reports true or false to the generic driver.

The generic driver therefore has no knowledge of, or involvement with, the actual commands and mechanisms used to communicate with the device. It is expected that the generic driver will rarely, if ever, need to be subclassed to handle device idiosyncrasies; rather, the transport driver should be changed via overrides.

A generic driver could be subclassed to create a different type of generic device. The generic driver IOCDBlockStorageDriver class is a subclass of IOBlockStorageDriver, adding CD functions.

## Topics

### Miscellaneous
- [acceptNewMedia](ioblockstoragedriver/1811574-acceptnewmedia.md)
  React to new media insertion.
- [addToBytesTransferred](ioblockstoragedriver/1811596-addtobytestransferred.md)
- [allocateContext](ioblockstoragedriver/1811624-allocatecontext.md)
- [breakUpRequest](ioblockstoragedriver/1811639-breakuprequest.md)
- [checkForMedia](ioblockstoragedriver/1811654-checkformedia.md)
  Check if media has newly arrived or disappeared.
- [constrainByteCount](ioblockstoragedriver/1811669-constrainbytecount.md)
  Constrain the byte count for this IO to device limits.
- [copyPhysicalExtent](ioblockstoragedriver/1811687-copyphysicalextent.md)
- [deblockRequest](ioblockstoragedriver/1811703-deblockrequest.md)
- [decommissionMedia](ioblockstoragedriver/1811732-decommissionmedia.md)
  Decommission an existing piece of media that has gone away.
- [deleteContext](ioblockstoragedriver/1811760-deletecontext.md)
- [ejectMedia](ioblockstoragedriver/1811792-ejectmedia.md)
- [executeRequest](ioblockstoragedriver/1811817-executerequest.md)
- [formatMedia](ioblockstoragedriver/1811835-formatmedia.md)
- [getDeviceTypeName](ioblockstoragedriver/1811863-getdevicetypename.md)
  Return the desired device name.
- [getFormatCapacities](ioblockstoragedriver/1811884-getformatcapacities.md)
- [getMediaBlockSize](ioblockstoragedriver/1811916-getmediablocksize.md)
- [getMediaState](ioblockstoragedriver/1811940-getmediastate.md)
- [getStatistic](ioblockstoragedriver/1811958-getstatistic.md)
- [getStatistics](ioblockstoragedriver/1811976-getstatistics.md)
- [handleClose](ioblockstoragedriver/1811990-handleclose.md)
- [handleIsOpen](ioblockstoragedriver/1811999-handleisopen.md)
- [handleOpen](ioblockstoragedriver/1812007-handleopen.md)
- [handleStart](ioblockstoragedriver/1812019-handlestart.md)
- [incrementErrors](ioblockstoragedriver/1812024-incrementerrors.md)
- [incrementRetries](ioblockstoragedriver/1812030-incrementretries.md)
- [initMediaState](ioblockstoragedriver/1812034-initmediastate.md)
  Initialize media-related instance variables.
- [instantiateDesiredMediaObject](ioblockstoragedriver/1812038-instantiatedesiredmediaobject.md)
  Create an IOMedia object for media.
- [instantiateMediaObject](ioblockstoragedriver/1812042-instantiatemediaobject.md)
  Create an IOMedia object for media.
- [isMediaEjectable](ioblockstoragedriver/1812044-ismediaejectable.md)
- [isMediaRemovable](ioblockstoragedriver/1812049-ismediaremovable.md)
- [isMediaWritable](ioblockstoragedriver/1812052-ismediawritable.md)
- [lockPhysicalExtents](ioblockstoragedriver/1812055-lockphysicalextents.md)
- [mediaStateHasChanged](ioblockstoragedriver/1812057-mediastatehaschanged.md)
  React to a new media insertion or a media removal.
- [prepareRequest](ioblockstoragedriver/1812063-preparerequest.md)
- [read](ioblockstoragedriver/1812076-read.md)
- [recordMediaParameters](ioblockstoragedriver/1812090-recordmediaparameters.md)
  Obtain media-related parameters on media insertion.
- [rejectMedia](ioblockstoragedriver/1812100-rejectmedia.md)
  Reject new media.
- [requestIdle](ioblockstoragedriver/1812117-requestidle.md)
  Request that the device enter an idle state.
- [synchronizeCache](ioblockstoragedriver/1812132-synchronizecache.md)
- [unlockPhysicalExtents](ioblockstoragedriver/1812149-unlockphysicalextents.md)
- [unmap](ioblockstoragedriver/1812179-unmap.md)
- [validateNewMedia](ioblockstoragedriver/1812204-validatenewmedia.md)
  Verify that new media is acceptable.
- [write](ioblockstoragedriver/1812222-write.md)
### Instance Variables
- [_writeProtected](ioblockstoragedriver/writeprotected.md)
- [_removable](ioblockstoragedriver/removable.md)
- [_mediaType](ioblockstoragedriver/mediatype.md)
- [_mediaObject](ioblockstoragedriver/mediaobject.md)
- [_mediaBlockSize](ioblockstoragedriver/mediablocksize.md)
- [_maxWriteByteTransfer](ioblockstoragedriver/maxwritebytetransfer.md)
- [_maxReadByteTransfer](ioblockstoragedriver/maxreadbytetransfer.md)
- [_maxBlockNumber](ioblockstoragedriver/maxblocknumber.md)
- [_ejectable](ioblockstoragedriver/ejectable.md)
### Instance Methods
- [- acceptNewMedia](ioblockstoragedriver/1436318-acceptnewmedia.md)
- [- addToBytesTransferred](ioblockstoragedriver/1436279-addtobytestransferred.md)
- [- allocateContext](ioblockstoragedriver/1436306-allocatecontext.md)
- [- breakUpRequest](ioblockstoragedriver/1436348-breakuprequest.md)
- [- checkForMedia](ioblockstoragedriver/1436299-checkformedia.md)
- [- constrainByteCount](ioblockstoragedriver/1436336-constrainbytecount.md)
- [- copyPhysicalExtent](ioblockstoragedriver/1436330-copyphysicalextent.md)
- [- deblockRequest](ioblockstoragedriver/1436326-deblockrequest.md)
- [- decommissionMedia](ioblockstoragedriver/1436307-decommissionmedia.md)
- [- deleteContext](ioblockstoragedriver/1436301-deletecontext.md)
- [- didTerminate](ioblockstoragedriver/1436313-didterminate.md)
- [- ejectMedia](ioblockstoragedriver/1436291-ejectmedia.md)
- [- executeRequest](ioblockstoragedriver/1436337-executerequest.md)
- [- formatMedia](ioblockstoragedriver/1436366-formatmedia.md)
- [- free](ioblockstoragedriver/1436323-free.md)
- [- getDeviceTypeName](ioblockstoragedriver/1436287-getdevicetypename.md)
- [- getFormatCapacities](ioblockstoragedriver/1436316-getformatcapacities.md)
- [- getMediaBlockSize](ioblockstoragedriver/1436334-getmediablocksize.md)
- [- getMediaState](ioblockstoragedriver/1436352-getmediastate.md)
- [- getMetaClass](ioblockstoragedriver/1436332-getmetaclass.md)
- [- getProvider](ioblockstoragedriver/1436340-getprovider.md)
- [- getProvisionStatus](ioblockstoragedriver/1641853-getprovisionstatus.md)
- [- getStatistic](ioblockstoragedriver/1436342-getstatistic.md)
- [- getStatistics](ioblockstoragedriver/1436300-getstatistics.md)
- [- handleClose](ioblockstoragedriver/1436362-handleclose.md)
- [- handleIsOpen](ioblockstoragedriver/1436296-handleisopen.md)
- [- handleOpen](ioblockstoragedriver/1436363-handleopen.md)
- [- handleStart](ioblockstoragedriver/1436344-handlestart.md)
- [- handleYield](ioblockstoragedriver/1436347-handleyield.md)
- [- incrementErrors](ioblockstoragedriver/1436298-incrementerrors.md)
- [- incrementRetries](ioblockstoragedriver/1436274-incrementretries.md)
- [- init](ioblockstoragedriver/1436365-init.md)
- [- initMediaState](ioblockstoragedriver/1436320-initmediastate.md)
- [- instantiateDesiredMediaObject](ioblockstoragedriver/1436303-instantiatedesiredmediaobject.md)
- [- instantiateMediaObject](ioblockstoragedriver/1436360-instantiatemediaobject.md)
- [- isMediaEjectable](ioblockstoragedriver/1436356-ismediaejectable.md)
- [- isMediaPollExpensive](ioblockstoragedriver/1436315-ismediapollexpensive.md)
- [- isMediaPollRequired](ioblockstoragedriver/1436275-ismediapollrequired.md)
- [- isMediaRemovable](ioblockstoragedriver/1436290-ismediaremovable.md)
- [- isMediaWritable](ioblockstoragedriver/1436280-ismediawritable.md)
- [- lockMedia](ioblockstoragedriver/1436355-lockmedia.md)
- [- lockPhysicalExtents](ioblockstoragedriver/1436346-lockphysicalextents.md)
- [- mediaStateHasChanged](ioblockstoragedriver/1436310-mediastatehaschanged.md)
- [- message](ioblockstoragedriver/1436350-message.md)
- [- pollMedia](ioblockstoragedriver/1436364-pollmedia.md)
- [- prepareRequest](ioblockstoragedriver/1436345-preparerequest.md)
- [- read](ioblockstoragedriver/1436293-read.md)
- [- recordMediaParameters](ioblockstoragedriver/1436292-recordmediaparameters.md)
- [- rejectMedia](ioblockstoragedriver/1436349-rejectmedia.md)
- [- requestIdle](ioblockstoragedriver/1436335-requestidle.md)
- [- schedulePoller](ioblockstoragedriver/1436369-schedulepoller.md)
- [- setPriority](ioblockstoragedriver/1436339-setpriority.md)
- [- start](ioblockstoragedriver/1436368-start.md)
- [- stop](ioblockstoragedriver/1436367-stop.md)
- [- synchronize](ioblockstoragedriver/1436305-synchronize.md)
- [- systemWillShutdown](ioblockstoragedriver/4116465-systemwillshutdown.md)
- [- unlockPhysicalExtents](ioblockstoragedriver/1436359-unlockphysicalextents.md)
- [- unmap](ioblockstoragedriver/1436321-unmap.md)
- [- unschedulePoller](ioblockstoragedriver/1436357-unschedulepoller.md)
- [- validateNewMedia](ioblockstoragedriver/1436312-validatenewmedia.md)
- [- write](ioblockstoragedriver/1436304-write.md)
- [- yield](ioblockstoragedriver/1436294-yield.md)
### Type Methods
- [+ breakUpRequestCompletion](ioblockstoragedriver/1436358-breakuprequestcompletion.md)
- [+ breakUpRequestExecute](ioblockstoragedriver/1436311-breakuprequestexecute.md)
- [+ deblockRequestCompletion](ioblockstoragedriver/1436343-deblockrequestcompletion.md)
- [+ deblockRequestExecute](ioblockstoragedriver/1436282-deblockrequestexecute.md)
- [+ handlePowerEvent](ioblockstoragedriver/1436322-handlepowerevent.md)
- [+ prepareRequestCompletion](ioblockstoragedriver/1436333-preparerequestcompletion.md)

## Relationships

### Inherits From
- [IOStorage](iostorage.md)

## See Also

- [IOBDBlockStorageDriver](iobdblockstoragedriver.md)
- [IODVDBlockStorageDriver](iodvdblockstoragedriver.md)
- [IOCDBlockStorageDriver](iocdblockstoragedriver.md)
- [IOStorage](iostorage.md)
  The common base class for mass storage objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedriver)*