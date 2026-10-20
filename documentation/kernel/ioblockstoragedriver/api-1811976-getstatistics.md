# getStatistics

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual UInt32 getStatistics(
 UInt64 *statistics, 
 UInt32statisticsMaxCount) const;
```

#### Return Value

Actual number of statistic values copied to the buffer, or if no buffer is given, the total number of statistic values available.

#### Overview

Ask the driver to report its operating statistics.

The statistics are each indexed by IOBlockStorageDriver::Statistics indices. This routine fills the caller's buffer, up to the maximum count specified if the real number of statistics would overflow the buffer. The return value indicates the actual number of statistics copied to the buffer.

If the statistics buffer is not supplied or if the maximum count is zero, the routine returns the proposed count of statistics instead.

## Parameters

- `statistics`: Buffer that will receive the UInt64 statistic values.
- `statisticsMaxCount`: Maximum number of statistic values that can be held in the buffer.

## See Also

### Miscellaneous
- [acceptNewMedia](./api-1811574-acceptnewmedia.md)
  React to new media insertion.
- [addToBytesTransferred](./api-1811596-addtobytestransferred.md)
- [allocateContext](./api-1811624-allocatecontext.md)
- [breakUpRequest](./api-1811639-breakuprequest.md)
- [checkForMedia](./api-1811654-checkformedia.md)
  Check if media has newly arrived or disappeared.
- [constrainByteCount](./api-1811669-constrainbytecount.md)
  Constrain the byte count for this IO to device limits.
- [copyPhysicalExtent](./api-1811687-copyphysicalextent.md)
- [deblockRequest](./api-1811703-deblockrequest.md)
- [decommissionMedia](./api-1811732-decommissionmedia.md)
  Decommission an existing piece of media that has gone away.
- [deleteContext](./api-1811760-deletecontext.md)
- [ejectMedia](./api-1811792-ejectmedia.md)
- [executeRequest](./api-1811817-executerequest.md)
- [formatMedia](./api-1811835-formatmedia.md)
- [getDeviceTypeName](./api-1811863-getdevicetypename.md)
  Return the desired device name.
- [getFormatCapacities](./api-1811884-getformatcapacities.md)
- [getMediaBlockSize](./api-1811916-getmediablocksize.md)
- [getMediaState](./api-1811940-getmediastate.md)
- [getStatistic](./api-1811958-getstatistic.md)
- [handleClose](./api-1811990-handleclose.md)
- [handleIsOpen](./api-1811999-handleisopen.md)
- [handleOpen](./api-1812007-handleopen.md)
- [handleStart](./api-1812019-handlestart.md)
- [incrementErrors](./api-1812024-incrementerrors.md)
- [incrementRetries](./api-1812030-incrementretries.md)
- [initMediaState](./api-1812034-initmediastate.md)
  Initialize media-related instance variables.
- [instantiateDesiredMediaObject](./api-1812038-instantiatedesiredmediaobject.md)
  Create an IOMedia object for media.
- [instantiateMediaObject](./api-1812042-instantiatemediaobject.md)
  Create an IOMedia object for media.
- [isMediaEjectable](./api-1812044-ismediaejectable.md)
- [isMediaRemovable](./api-1812049-ismediaremovable.md)
- [isMediaWritable](./api-1812052-ismediawritable.md)
- [lockPhysicalExtents](./api-1812055-lockphysicalextents.md)
- [mediaStateHasChanged](./api-1812057-mediastatehaschanged.md)
  React to a new media insertion or a media removal.
- [prepareRequest](./api-1812063-preparerequest.md)
- [read](./api-1812076-read.md)
- [recordMediaParameters](./api-1812090-recordmediaparameters.md)
  Obtain media-related parameters on media insertion.
- [rejectMedia](./api-1812100-rejectmedia.md)
  Reject new media.
- [requestIdle](./api-1812117-requestidle.md)
  Request that the device enter an idle state.
- [synchronizeCache](./api-1812132-synchronizecache.md)
- [unlockPhysicalExtents](./api-1812149-unlockphysicalextents.md)
- [unmap](./api-1812179-unmap.md)
- [validateNewMedia](./api-1812204-validatenewmedia.md)
  Verify that new media is acceptable.
- [write](./api-1812222-write.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedriver/1811976-getstatistics)*