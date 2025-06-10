# decommissionMedia

**Framework**: Kernel  
**Kind**: instm

Decommission an existing piece of media that has gone away.

## Declaration

```swift
virtual IOReturn decommissionMedia(
 boolforcible);
```

#### Overview

This method wraps a call to terminate, to tear down the stack and the IOMedia object for the media. If "forcible" is true, the media object will be forgotten, and initMediaState will be called. A forcible decommission would occur when an unrecoverable error happens during tear-down (e.g. perhaps a client is still open), but we must still forget about the media.

## Parameters

- `forcible`: True to force forgetting of the media object even if terminate reports that there was an active client.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedriver/1811732-decommissionmedia)*