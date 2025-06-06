# buf_getblk

**Framework**: Kernel  
**Kind**: func

Traditional buffer cache routine to get a buffer corresponding to a logical block in a file.

**Availability**:
- macOS 10.4+

## Declaration

```swift
buf_t buf_getblk(vnode_t vp, daddr64_t blkno, int size, int slpflag, int slptimeo, int operation);
```

#### Return_value

Buffer found in core or newly allocated, either containing valid data or ready for I/O.

#### Discussion

buf_getblk() gets a buffer, not necessarily containing valid data, representing a block in a file. A metadata buffer will be returned with its own zone-allocated storage, managed by the traditional buffer-cache layer, whereas data buffers will be returned hooked into backing by the UBC (which in fact controls the caching of data). buf_getblk() first looks for the buffer header in cache; if the buffer is in-core but busy, buf_getblk() will wait for it to become unbusy, depending on the slpflag and slptimeo parameters. If the buffer is found unbusy and is a metadata buffer, it must already contain valid data and will be returned directly; data buffers will have a UPL configured to prepare for interaction with the underlying UBC. If the buffer is found in core, it will be marked as such and buf_fromcache() will return truth. A buffer is allocated and initialized (but not filled with data) if none is found in core. buf_bread(), buf_breadn(), buf_meta_bread(), and buf_meta_breadn() all return buffers obtained with buf_getblk().

## Parameters

- `vp`: File for which to get block.
- `blkno`: Logical block number.
- `size`: Size of block.
- `slpflag`: Flag to pass to msleep() while waiting for buffer to become unbusy.
- `slptimeo`: Time, in milliseconds, to wait for buffer to become unbusy. 0 means to wait indefinitely.
- `operation`: BLK_READ: want a read buffer. BLK_WRITE: want a write buffer. BLK_META: want a metadata buffer. BLK_ONLYVALID: only return buffers which are found in core (do not allocate anew), and do not change buffer size. The last remark means that if a given logical block is found in core with a different size than what is requested, the buffer size will not be modified.

## See Also

- [buf_alloc](1561906-buf_alloc.md)
  Allocate an uninitialized buffer.
- [buf_attr](1561894-buf_attr.md)
  Gets the attributes for this buf.
- [buf_bawrite](1561823-buf_bawrite.md)
  Start an asychronous write on a buffer.
- [buf_bdwrite](1561858-buf_bdwrite.md)
  Mark a buffer for delayed write.
- [buf_biodone](1561914-buf_biodone.md)
  Mark an I/O as completed.
- [buf_biowait](1561908-buf_biowait.md)
  Wait for I/O on a buffer to complete.
- [buf_blkno](1561926-buf_blkno.md)
  Get physical block number associated with a buffer, in the sense of VNOP_BLOCKMAP.
- [buf_bread](1561851-buf_bread.md)
  Synchronously read a block of a file.
- [buf_breadn](1561873-buf_breadn.md)
  Read a block from a file with read-ahead.
- [buf_brelse](1561897-buf_brelse.md)
  Release any claim to a buffer, sending it back to free lists.
- [buf_bwrite](1561886-buf_bwrite.md)
  Write a buffer's data to backing store.
- [buf_callback](1561902-buf_callback.md)
  Get the function set to be called when I/O on a buffer completes.
- [buf_clear](1561901-buf_clear.md)
  Zero out the storage associated with a buffer.
- [buf_clear_redundancy_flags](1561898-buf_clear_redundancy_flags.md)
  Clear flags on a buffer. @discussion: buffer_redundancy_flags &= ~flags
- [buf_clearflags](1561837-buf_clearflags.md)
  Clear flags on a buffer. @discussion: buffer_flags &= ~flags
- [buf_clone](1561867-buf_clone.md)
  Clone a buffer with a restricted range and an optional callback.
- [buf_count](1561820-buf_count.md)
  Get count of valid bytes in a buffer. This may be less than the space allocated to the buffer.
- [buf_create_shadow](1561838-buf_create_shadow.md)
  Create a shadow buffer with optional private storage and an optional callback.
- [buf_dataptr](1561881-buf_dataptr.md)
  Get the address at which a buffer's data is stored; for iobufs, this must be set with buf_setdataptr(). See buf_map().
- [buf_device](1561922-buf_device.md)
  Get the device ID associated with a buffer.
- [buf_dirtyend](1561850-buf_dirtyend.md)
  Get the ending offset of the dirty region associated with a buffer.
- [buf_dirtyoff](1561923-buf_dirtyoff.md)
  Get the starting offset of the dirty region associated with a buffer.
- [buf_drvdata](1561866-buf_drvdata.md)
  Get driver-specific data from a buffer.
- [buf_error](1561818-buf_error.md)
  Get the error value associated with a buffer.
- [buf_flags](1561844-buf_flags.md)
  Get flags set on a buffer.
- [buf_flushdirtyblks](1561822-buf_flushdirtyblks.md)
  Write dirty file blocks to disk.
- [buf_free](1561907-buf_free.md)
  Free a buffer that was allocated with buf_alloc().
- [buf_fromcache](1561933-buf_fromcache.md)
  Check if a buffer's data was found in core.
- [buf_fsprivate](1561929-buf_fsprivate.md)
  Get filesystem-specific data from a buffer.
- [buf_fua](1561842-buf_fua.md)
  Check if a buffer is marked for write through disk caches.
- [buf_geteblk](1561862-buf_geteblk.md)
  Get a metadata buffer which is marked invalid and not associated with any vnode.
- [buf_invalblkno](1561843-buf_invalblkno.md)
  Invalidate a filesystem logical block in a file.
- [buf_invalidateblks](1561910-buf_invalidateblks.md)
  Invalidate all the blocks associated with a vnode.
- [buf_iterate](1561857-buf_iterate.md)
  Perform some operation on all buffers associated with a vnode.
- [buf_lblkno](1561825-buf_lblkno.md)
  Get logical block number associated with a buffer.
- [buf_map](1561890-buf_map.md)
  Get virtual mappings for buffer data.
- [buf_markaged](1561845-buf_markaged.md)
  Mark a buffer as "aged," i.e. as a good candidate to be discarded and reused after buf_brelse().
- [buf_markclean](1561834-buf_markclean.md)
- [buf_markdelayed](1561911-buf_markdelayed.md)
  Mark a buffer as a delayed write: mark it dirty without actually scheduling I/O.
- [buf_markeintr](1561892-buf_markeintr.md)
  Mark a buffer as having been interrupted during I/O.
- [buf_markfua](1561841-buf_markfua.md)
  Mark a buffer for write through disk cache, if disk supports it.
- [buf_markinvalid](1561863-buf_markinvalid.md)
  Mark a buffer as not having valid data and being ready for immediate reuse after buf_brelse().
- [buf_markstatic](1561839-buf_markstatic.md)
  Mark a buffer as being likely to contain static data.
- [buf_meta_bread](1561871-buf_meta_bread.md)
  Synchronously read a metadata block of a file.
- [buf_meta_breadn](1561821-buf_meta_breadn.md)
  Read a metadata block from a file with read-ahead.
- [buf_proc](1561855-buf_proc.md)
  Get the process associated with this buffer.
- [buf_rcred](1561836-buf_rcred.md)
  Get the credential associated with a buffer for reading.
- [buf_redundancy_flags](1561872-buf_redundancy_flags.md)
  Get redundancy flags set on a buffer.
- [buf_reset](1561928-buf_reset.md)
  Reset I/O flag state on a buffer.
- [buf_resid](1561835-buf_resid.md)
  Get a count of bytes which were not consumed by an I/O on a buffer.
- [buf_set_redundancy_flags](1561865-buf_set_redundancy_flags.md)
  Set redundancy flags on a buffer. @discussion: buffer_redundancy_flags |= flags
- [buf_setblkno](1561888-buf_setblkno.md)
  Set physical block number associated with a buffer.
- [buf_setcallback](1561885-buf_setcallback.md)
  Set a function to be called once when I/O on a buffer completes.
- [buf_setcount](1561852-buf_setcount.md)
  Set count of valid bytes in a buffer. This may be less than the space allocated to the buffer.
- [buf_setdataptr](1561861-buf_setdataptr.md)
  Set the address at which a buffer's data will be stored.
- [buf_setdevice](1561859-buf_setdevice.md)
  Set the device associated with a buffer.
- [buf_setdirtyend](1561826-buf_setdirtyend.md)
  Set the ending offset of the dirty region associated with a buffer.
- [buf_setdirtyoff](1561924-buf_setdirtyoff.md)
  Set the starting offset of the dirty region associated with a buffer.
- [buf_setdrvdata](1561880-buf_setdrvdata.md)
  Set driver-specific data on a buffer.
- [buf_seterror](1561934-buf_seterror.md)
  Set an error value on a buffer.
- [buf_setflags](1561931-buf_setflags.md)
  Set flags on a buffer. @discussion: buffer_flags |= flags
- [buf_setfsprivate](1561927-buf_setfsprivate.md)
  Set filesystem-specific data on a buffer.
- [buf_setlblkno](1561900-buf_setlblkno.md)
  Set logical block number associated with a buffer.
- [buf_setresid](1561849-buf_setresid.md)
  Set a count of bytes outstanding for I/O in a buffer.
- [buf_setsize](1561921-buf_setsize.md)
  Set size of data region allocated to a buffer.
- [buf_setupl](1561846-buf_setupl.md)
  Set the UPL (Universal Page List), and offset therein, on a buffer.
- [buf_setvnode](1561833-buf_setvnode.md)
  Set the vnode associated with a buffer.
- [buf_shadow](1561877-buf_shadow.md)
  returns true if 'bp' is a shadow of another buffer.
- [buf_size](1561917-buf_size.md)
  Get size of data region allocated to a buffer.
- [buf_static](1561912-buf_static.md)
  Check if a buffer contains static data.
- [buf_strategy](1561893-buf_strategy.md)
  Pass an I/O request for a buffer down to the device layer.
- [buf_unmap](1561876-buf_unmap.md)
  Release mappings for buffer data.
- [buf_upl](1561918-buf_upl.md)
  Get the upl (Universal Page List) associated with a buffer.
- [buf_uploffset](1561860-buf_uploffset.md)
  Get the offset into a UPL at which this buffer begins.
- [buf_valid](1561915-buf_valid.md)
  Check if a buffer contains valid data.
- [buf_vnode](1561919-buf_vnode.md)
  Get the vnode associated with a buffer.
- [buf_wcred](1561896-buf_wcred.md)
  Get the credential associated with a buffer for writing.
- [bufattr_ioscheduled](3325830-bufattr_ioscheduled.md)
- [bufattr_markioscheduled](3325831-bufattr_markioscheduled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1561932-buf_getblk)*