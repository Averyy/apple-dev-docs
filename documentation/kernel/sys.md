# sys

**Framework**: Kernel  
**Role**: API Collection

Access general system utilities for time, file systems, and system information.

## Topics

### Block Device
- [bdevsw_add](./api-1457957-bdevsw_add.md)
- [bdevsw_isfree](./api-1457925-bdevsw_isfree.md)
- [bdevsw_remove](./api-1457943-bdevsw_remove.md)
- [cdevsw_add](./api-1457951-cdevsw_add.md)
- [cdevsw_add_with_bdev](./api-1458015-cdevsw_add_with_bdev.md)
- [cdevsw_isfree](./api-1457965-cdevsw_isfree.md)
- [cdevsw_remove](./api-1458013-cdevsw_remove.md)
### Buffers
- [buf_alloc](./api-1561906-buf_alloc.md)
  Allocate an uninitialized buffer.
- [buf_attr](./api-1561894-buf_attr.md)
  Gets the attributes for this buf.
- [buf_bawrite](./api-1561823-buf_bawrite.md)
  Start an asychronous write on a buffer.
- [buf_bdwrite](./api-1561858-buf_bdwrite.md)
  Mark a buffer for delayed write.
- [buf_biodone](./api-1561914-buf_biodone.md)
  Mark an I/O as completed.
- [buf_biowait](./api-1561908-buf_biowait.md)
  Wait for I/O on a buffer to complete.
- [buf_blkno](./api-1561926-buf_blkno.md)
  Get physical block number associated with a buffer, in the sense of VNOP_BLOCKMAP.
- [buf_bread](./api-1561851-buf_bread.md)
  Synchronously read a block of a file.
- [buf_breadn](./api-1561873-buf_breadn.md)
  Read a block from a file with read-ahead.
- [buf_brelse](./api-1561897-buf_brelse.md)
  Release any claim to a buffer, sending it back to free lists.
- [buf_bwrite](./api-1561886-buf_bwrite.md)
  Write a buffer's data to backing store.
- [buf_callback](./api-1561902-buf_callback.md)
  Get the function set to be called when I/O on a buffer completes.
- [buf_clear](./api-1561901-buf_clear.md)
  Zero out the storage associated with a buffer.
- [buf_clear_redundancy_flags](./api-1561898-buf_clear_redundancy_flags.md)
  Clear flags on a buffer. @discussion: buffer_redundancy_flags &= ~flags
- [buf_clearflags](./api-1561837-buf_clearflags.md)
  Clear flags on a buffer. @discussion: buffer_flags &= ~flags
- [buf_clone](./api-1561867-buf_clone.md)
  Clone a buffer with a restricted range and an optional callback.
- [buf_count](./api-1561820-buf_count.md)
  Get count of valid bytes in a buffer. This may be less than the space allocated to the buffer.
- [buf_create_shadow](./api-1561838-buf_create_shadow.md)
  Create a shadow buffer with optional private storage and an optional callback.
- [buf_dataptr](./api-1561881-buf_dataptr.md)
  Get the address at which a buffer's data is stored; for iobufs, this must be set with buf_setdataptr(). See buf_map().
- [buf_device](./api-1561922-buf_device.md)
  Get the device ID associated with a buffer.
- [buf_dirtyend](./api-1561850-buf_dirtyend.md)
  Get the ending offset of the dirty region associated with a buffer.
- [buf_dirtyoff](./api-1561923-buf_dirtyoff.md)
  Get the starting offset of the dirty region associated with a buffer.
- [buf_drvdata](./api-1561866-buf_drvdata.md)
  Get driver-specific data from a buffer.
- [buf_error](./api-1561818-buf_error.md)
  Get the error value associated with a buffer.
- [buf_flags](./api-1561844-buf_flags.md)
  Get flags set on a buffer.
- [buf_flushdirtyblks](./api-1561822-buf_flushdirtyblks.md)
  Write dirty file blocks to disk.
- [buf_free](./api-1561907-buf_free.md)
  Free a buffer that was allocated with buf_alloc().
- [buf_fromcache](./api-1561933-buf_fromcache.md)
  Check if a buffer's data was found in core.
- [buf_fsprivate](./api-1561929-buf_fsprivate.md)
  Get filesystem-specific data from a buffer.
- [buf_fua](./api-1561842-buf_fua.md)
  Check if a buffer is marked for write through disk caches.
- [buf_getblk](./api-1561932-buf_getblk.md)
  Traditional buffer cache routine to get a buffer corresponding to a logical block in a file.
- [buf_geteblk](./api-1561862-buf_geteblk.md)
  Get a metadata buffer which is marked invalid and not associated with any vnode.
- [buf_invalblkno](./api-1561843-buf_invalblkno.md)
  Invalidate a filesystem logical block in a file.
- [buf_invalidateblks](./api-1561910-buf_invalidateblks.md)
  Invalidate all the blocks associated with a vnode.
- [buf_iterate](./api-1561857-buf_iterate.md)
  Perform some operation on all buffers associated with a vnode.
- [buf_lblkno](./api-1561825-buf_lblkno.md)
  Get logical block number associated with a buffer.
- [buf_map](./api-1561890-buf_map.md)
  Get virtual mappings for buffer data.
- [buf_markaged](./api-1561845-buf_markaged.md)
  Mark a buffer as "aged," i.e. as a good candidate to be discarded and reused after buf_brelse().
- [buf_markclean](./api-1561834-buf_markclean.md)
- [buf_markdelayed](./api-1561911-buf_markdelayed.md)
  Mark a buffer as a delayed write: mark it dirty without actually scheduling I/O.
- [buf_markeintr](./api-1561892-buf_markeintr.md)
  Mark a buffer as having been interrupted during I/O.
- [buf_markfua](./api-1561841-buf_markfua.md)
  Mark a buffer for write through disk cache, if disk supports it.
- [buf_markinvalid](./api-1561863-buf_markinvalid.md)
  Mark a buffer as not having valid data and being ready for immediate reuse after buf_brelse().
- [buf_markstatic](./api-1561839-buf_markstatic.md)
  Mark a buffer as being likely to contain static data.
- [buf_meta_bread](./api-1561871-buf_meta_bread.md)
  Synchronously read a metadata block of a file.
- [buf_meta_breadn](./api-1561821-buf_meta_breadn.md)
  Read a metadata block from a file with read-ahead.
- [buf_proc](./api-1561855-buf_proc.md)
  Get the process associated with this buffer.
- [buf_rcred](./api-1561836-buf_rcred.md)
  Get the credential associated with a buffer for reading.
- [buf_redundancy_flags](./api-1561872-buf_redundancy_flags.md)
  Get redundancy flags set on a buffer.
- [buf_reset](./api-1561928-buf_reset.md)
  Reset I/O flag state on a buffer.
- [buf_resid](./api-1561835-buf_resid.md)
  Get a count of bytes which were not consumed by an I/O on a buffer.
- [buf_set_redundancy_flags](./api-1561865-buf_set_redundancy_flags.md)
  Set redundancy flags on a buffer. @discussion: buffer_redundancy_flags |= flags
- [buf_setblkno](./api-1561888-buf_setblkno.md)
  Set physical block number associated with a buffer.
- [buf_setcallback](./api-1561885-buf_setcallback.md)
  Set a function to be called once when I/O on a buffer completes.
- [buf_setcount](./api-1561852-buf_setcount.md)
  Set count of valid bytes in a buffer. This may be less than the space allocated to the buffer.
- [buf_setdataptr](./api-1561861-buf_setdataptr.md)
  Set the address at which a buffer's data will be stored.
- [buf_setdevice](./api-1561859-buf_setdevice.md)
  Set the device associated with a buffer.
- [buf_setdirtyend](./api-1561826-buf_setdirtyend.md)
  Set the ending offset of the dirty region associated with a buffer.
- [buf_setdirtyoff](./api-1561924-buf_setdirtyoff.md)
  Set the starting offset of the dirty region associated with a buffer.
- [buf_setdrvdata](./api-1561880-buf_setdrvdata.md)
  Set driver-specific data on a buffer.
- [buf_seterror](./api-1561934-buf_seterror.md)
  Set an error value on a buffer.
- [buf_setflags](./api-1561931-buf_setflags.md)
  Set flags on a buffer. @discussion: buffer_flags |= flags
- [buf_setfsprivate](./api-1561927-buf_setfsprivate.md)
  Set filesystem-specific data on a buffer.
- [buf_setlblkno](./api-1561900-buf_setlblkno.md)
  Set logical block number associated with a buffer.
- [buf_setresid](./api-1561849-buf_setresid.md)
  Set a count of bytes outstanding for I/O in a buffer.
- [buf_setsize](./api-1561921-buf_setsize.md)
  Set size of data region allocated to a buffer.
- [buf_setupl](./api-1561846-buf_setupl.md)
  Set the UPL (Universal Page List), and offset therein, on a buffer.
- [buf_setvnode](./api-1561833-buf_setvnode.md)
  Set the vnode associated with a buffer.
- [buf_shadow](./api-1561877-buf_shadow.md)
  returns true if 'bp' is a shadow of another buffer.
- [buf_size](./api-1561917-buf_size.md)
  Get size of data region allocated to a buffer.
- [buf_static](./api-1561912-buf_static.md)
  Check if a buffer contains static data.
- [buf_strategy](./api-1561893-buf_strategy.md)
  Pass an I/O request for a buffer down to the device layer.
- [buf_unmap](./api-1561876-buf_unmap.md)
  Release mappings for buffer data.
- [buf_upl](./api-1561918-buf_upl.md)
  Get the upl (Universal Page List) associated with a buffer.
- [buf_uploffset](./api-1561860-buf_uploffset.md)
  Get the offset into a UPL at which this buffer begins.
- [buf_valid](./api-1561915-buf_valid.md)
  Check if a buffer contains valid data.
- [buf_vnode](./api-1561919-buf_vnode.md)
  Get the vnode associated with a buffer.
- [buf_wcred](./api-1561896-buf_wcred.md)
  Get the credential associated with a buffer for writing.
- [bufattr_ioscheduled](./api-3325830-bufattr_ioscheduled.md)
- [bufattr_markioscheduled](./api-3325831-bufattr_markioscheduled.md)
### General
- [bsd_timeout](./api-1519651-bsd_timeout.md)
- [bsd_untimeout](./api-1519608-bsd_untimeout.md)
### Serialization
- [OSUnserialize](./api-1584516-osunserialize.md)
- [OSUnserializeBinary](./api-1575008-osunserializebinary.md)
- [OSUnserializeXML](./api-1584515-osunserializexml.md)
### control
- [ctl_deregister](./api-1809161-ctl_deregister.md)
- [ctl_enqueuedata](./api-1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](./api-1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](./api-2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](./api-1809173-ctl_getenqueuespace.md)
- [ctl_register](./api-1809176-ctl_register.md)
### file
- [file_drop](./api-1434981-file_drop.md)
- [file_flags](./api-1434975-file_flags.md)
- [file_socket](./api-1434977-file_socket.md)
- [file_vnode](./api-1434979-file_vnode.md)
- [file_vnode_withvid](./api-1434973-file_vnode_withvid.md)
### proc
- [proc_best_name](./api-3020681-proc_best_name.md)
- [proc_chrooted](./api-1488999-proc_chrooted.md)
- [proc_csflags](./api-3538582-proc_csflags.md)
- [proc_exiting](./api-1489000-proc_exiting.md)
- [proc_find](./api-1488987-proc_find.md)
- [proc_forcequota](./api-1488993-proc_forcequota.md)
- [proc_gettty](./api-3538583-proc_gettty.md)
- [proc_gettty_dev](./api-3538584-proc_gettty_dev.md)
- [proc_in_teardown](./api-2990533-proc_in_teardown.md)
- [proc_is64bit](./api-1488977-proc_is64bit.md)
- [proc_is64bit_data](./api-2967400-proc_is64bit_data.md)
- [proc_is_classic](./api-1488982-proc_is_classic.md)
- [proc_isinferior](./api-1489001-proc_isinferior.md)
- [proc_issetugid](./api-2998888-proc_issetugid.md)
- [proc_issignal](./api-1488967-proc_issignal.md)
- [proc_name](./api-1488959-proc_name.md)
- [proc_noremotehang](./api-1488981-proc_noremotehang.md)
- [proc_original_ppid](./api-3325836-proc_original_ppid.md)
- [proc_pgrpid](./api-1488969-proc_pgrpid.md)
  Get the process group id for the passed-in process.
- [proc_pid](./api-1488997-proc_pid.md)
- [proc_platform](./api-3194345-proc_platform.md)
- [proc_ppid](./api-1488964-proc_ppid.md)
- [proc_rele](./api-1488988-proc_rele.md)
- [proc_sdk](./api-3194346-proc_sdk.md)
- [proc_self](./api-1488975-proc_self.md)
- [proc_selfcsflags](./api-1488989-proc_selfcsflags.md)
- [proc_selfname](./api-1488979-proc_selfname.md)
- [proc_selfpgrpid](./api-1488978-proc_selfpgrpid.md)
  Get the process group id for the current process, as with proc_pgrpid().
- [proc_selfpid](./api-1488971-proc_selfpid.md)
- [proc_selfppid](./api-1488985-proc_selfppid.md)
- [proc_send_synchronous_EXC_RESOURCE](./api-3013826-proc_send_synchronous_exc_resour.md)
- [proc_sessionid](./api-3366028-proc_sessionid.md)
- [proc_signal](./api-1488994-proc_signal.md)
- [proc_suser](./api-1488961-proc_suser.md)
- [proc_tbe](./api-1488984-proc_tbe.md)
- [proc_ucred](./api-1488996-proc_ucred.md)
- [current_proc](./api-1427365-current_proc.md)
- [current_proc_EXTERNAL](./api-1488991-current_proc_external.md)
### sysctl
- [sysctl_handle_int](./api-1404317-sysctl_handle_int.md)
- [sysctl_handle_int2quad](./api-1404249-sysctl_handle_int2quad.md)
- [sysctl_handle_long](./api-1404379-sysctl_handle_long.md)
- [sysctl_handle_opaque](./api-1404289-sysctl_handle_opaque.md)
- [sysctl_handle_quad](./api-1404243-sysctl_handle_quad.md)
- [sysctl_handle_string](./api-1404297-sysctl_handle_string.md)
- [sysctl_io_number](./api-1404223-sysctl_io_number.md)
- [sysctl_io_opaque](./api-1404235-sysctl_io_opaque.md)
- [sysctl_io_string](./api-1404325-sysctl_io_string.md)
- [sysctl_register_oid](./api-1404241-sysctl_register_oid.md)
- [sysctl_unregister_oid](./api-1404403-sysctl_unregister_oid.md)
- [sysctlbyname](./api-1387446-sysctlbyname.md)
  Gets or sets information about the system and environment.
- [sysctl__children](./sysctl_children.md)
- [sysctl__debug_children](./sysctl_debug_children.md)
- [sysctl__hw_children](./sysctl_hw_children.md)
- [sysctl__kern_children](./sysctl_kern_children.md)
- [sysctl__machdep_children](./sysctl_machdep_children.md)
- [sysctl__net_children](./sysctl_net_children.md)
- [sysctl__sysctl_children](./sysctl_sysctl_children.md)
- [sysctl__user_children](./sysctl_user_children.md)
- [sysctl__vfs_children](./sysctl_vfs_children.md)
- [sysctl__vm_children](./sysctl_vm_children.md)
### throttle
- [throttle_info_create](./api-1519622-throttle_info_create.md)
- [throttle_info_disable_throttle](./api-1519606-throttle_info_disable_throttle.md)
- [throttle_info_io_will_be_throttled](./api-1519647-throttle_info_io_will_be_throttl.md)
- [throttle_info_mount_ref](./api-1519621-throttle_info_mount_ref.md)
- [throttle_info_mount_rel](./api-1519613-throttle_info_mount_rel.md)
- [throttle_info_ref_by_mask](./api-1519602-throttle_info_ref_by_mask.md)
- [throttle_info_rel_by_mask](./api-1519618-throttle_info_rel_by_mask.md)
- [throttle_info_release](./api-1519640-throttle_info_release.md)
- [throttle_info_update](./api-1519620-throttle_info_update.md)
- [throttle_info_update_by_mask](./api-1519642-throttle_info_update_by_mask.md)
- [throttle_lowpri_io](./api-1519650-throttle_lowpri_io.md)
- [throttle_lowpri_io_will_be_throttled](./api-3192010-throttle_lowpri_io_will_be_throt.md)
- [throttle_set_thread_io_policy](./api-1519605-throttle_set_thread_io_policy.md)
### ubc
- [ubc_blktooff](./api-1463720-ubc_blktooff.md)
- [ubc_create_upl](./api-1463758-ubc_create_upl.md)
- [ubc_getcred](./api-1463771-ubc_getcred.md)
- [ubc_getsize](./api-1463713-ubc_getsize.md)
- [ubc_msync](./api-1463717-ubc_msync.md)
- [ubc_offtoblk](./api-1463760-ubc_offtoblk.md)
- [ubc_page_op](./api-1463700-ubc_page_op.md)
- [ubc_pages_resident](./api-1463777-ubc_pages_resident.md)
- [ubc_range_op](./api-1463728-ubc_range_op.md)
- [ubc_setsize](./api-1463764-ubc_setsize.md)
- [ubc_setthreadcred](./api-1463732-ubc_setthreadcred.md)
- [ubc_upl_abort](./api-1463754-ubc_upl_abort.md)
- [ubc_upl_abort_range](./api-1463762-ubc_upl_abort_range.md)
- [ubc_upl_commit](./api-1463702-ubc_upl_commit.md)
- [ubc_upl_commit_range](./api-1463734-ubc_upl_commit_range.md)
- [ubc_upl_map](./api-1463744-ubc_upl_map.md)
- [ubc_upl_maxbufsize](./api-1463748-ubc_upl_maxbufsize.md)
- [ubc_upl_pageinfo](./api-1463704-ubc_upl_pageinfo.md)
- [ubc_upl_range_needed](./api-1463746-ubc_upl_range_needed.md)
- [ubc_upl_unmap](./api-1463778-ubc_upl_unmap.md)
- [cluster_bp](./api-1463769-cluster_bp.md)
- [cluster_bp_ext](./api-1463742-cluster_bp_ext.md)
- [cluster_copy_ubc_data](./api-1463730-cluster_copy_ubc_data.md)
- [cluster_copy_upl_data](./api-1463719-cluster_copy_upl_data.md)
- [cluster_lock_direct_read](./api-1463706-cluster_lock_direct_read.md)
- [cluster_pagein](./api-1463765-cluster_pagein.md)
- [cluster_pagein_ext](./api-1463709-cluster_pagein_ext.md)
- [cluster_pageout](./api-1463710-cluster_pageout.md)
- [cluster_pageout_ext](./api-1463750-cluster_pageout_ext.md)
- [cluster_push](./api-1463738-cluster_push.md)
- [cluster_push_err](./api-2852886-cluster_push_err.md)
- [cluster_push_ext](./api-1463714-cluster_push_ext.md)
- [cluster_read](./api-1463724-cluster_read.md)
- [cluster_read_ext](./api-1463712-cluster_read_ext.md)
- [cluster_unlock_direct_read](./api-1463731-cluster_unlock_direct_read.md)
- [cluster_update_state](./api-2967405-cluster_update_state.md)
- [cluster_write](./api-1463767-cluster_write.md)
- [cluster_write_ext](./api-1463756-cluster_write_ext.md)
- [cluster_zero](./api-1463752-cluster_zero.md)
### vnode
- [vnop_access_desc](./vnop_access_desc.md)
- [vnop_advlock_desc](./vnop_advlock_desc.md)
- [vnop_allocate_desc](./vnop_allocate_desc.md)
- [vnop_blktooff_desc](./vnop_blktooff_desc.md)
- [vnop_blockmap_desc](./vnop_blockmap_desc.md)
- [vnop_bwrite_desc](./vnop_bwrite_desc.md)
- [vnop_clonefile_desc](./vnop_clonefile_desc.md)
- [vnop_close_desc](./vnop_close_desc.md)
- [vnop_copyfile_desc](./vnop_copyfile_desc.md)
- [vnop_create_desc](./vnop_create_desc.md)
- [vnop_default_desc](./vnop_default_desc.md)
- [vnop_exchange_desc](./vnop_exchange_desc.md)
- [vnop_fsync_desc](./vnop_fsync_desc.md)
- [vnop_getattr_desc](./vnop_getattr_desc.md)
- [vnop_getattrlistbulk_desc](./vnop_getattrlistbulk_desc.md)
- [vnop_getxattr_desc](./vnop_getxattr_desc.md)
  Write data from a mapped file back to disk.
- [vnop_inactive_desc](./vnop_inactive_desc.md)
- [vnop_ioctl_desc](./vnop_ioctl_desc.md)
- [vnop_kqfilt_add_desc](./vnop_kqfilt_add_desc.md)
- [vnop_kqfilt_remove_desc](./vnop_kqfilt_remove_desc.md)
- [vnop_link_desc](./vnop_link_desc.md)
- [vnop_listxattr_desc](./vnop_listxattr_desc.md)
  Remove extended file attributes.
- [vnop_lookup_desc](./vnop_lookup_desc.md)
- [vnop_mkdir_desc](./vnop_mkdir_desc.md)
- [vnop_mknod_desc](./vnop_mknod_desc.md)
- [vnop_mmap_check_desc](./vnop_mmap_check_desc.md)
- [vnop_mmap_desc](./vnop_mmap_desc.md)
- [vnop_mnomap_desc](./vnop_mnomap_desc.md)
- [vnop_offtoblk_desc](./vnop_offtoblk_desc.md)
- [vnop_open_desc](./vnop_open_desc.md)
- [vnop_pagein_desc](./vnop_pagein_desc.md)
- [vnop_pageout_desc](./vnop_pageout_desc.md)
- [vnop_pathconf_desc](./vnop_pathconf_desc.md)
- [vnop_print_desc](./vnop_print_desc.md)
- [vnop_read_desc](./vnop_read_desc.md)
- [vnop_readdir_desc](./vnop_readdir_desc.md)
- [vnop_readdirattr_desc](./vnop_readdirattr_desc.md)
- [vnop_readlink_desc](./vnop_readlink_desc.md)
- [vnop_reclaim_desc](./vnop_reclaim_desc.md)
- [vnop_remove_desc](./vnop_remove_desc.md)
- [vnop_removexattr_desc](./vnop_removexattr_desc.md)
- [vnop_rename_desc](./vnop_rename_desc.md)
- [vnop_renamex_desc](./vnop_renamex_desc.md)
- [vnop_revoke_desc](./vnop_revoke_desc.md)
- [vnop_rmdir_desc](./vnop_rmdir_desc.md)
- [vnop_searchfs_desc](./vnop_searchfs_desc.md)
- [vnop_select_desc](./vnop_select_desc.md)
- [vnop_setattr_desc](./vnop_setattr_desc.md)
- [vnop_setlabel_desc](./vnop_setlabel_desc.md)
- [vnop_setxattr_desc](./vnop_setxattr_desc.md)
- [vnop_strategy_desc](./vnop_strategy_desc.md)
- [vnop_symlink_desc](./vnop_symlink_desc.md)
- [vnop_truncate_desc](./vnop_truncate_desc.md)
- [vnop_whiteout_desc](./vnop_whiteout_desc.md)
- [vnop_write_desc](./vnop_write_desc.md)
- [vnode_addfsref](./api-1562216-vnode_addfsref.md)
  Mark a vnode as being stored in a filesystem hash.
- [vnode_authattr](./api-1562106-vnode_authattr.md)
  Given a vnode_attr structure, determine what kauth-style actions must be authorized in order to set those attributes.
- [vnode_authattr_new](./api-1562184-vnode_authattr_new.md)
  Initialize and validate file creation parameters with respect to the current context.
- [vnode_authorize](./api-1562084-vnode_authorize.md)
  Authorize a kauth-style action on a vnode.
- [vnode_clearautocandidate](./api-1562373-vnode_clearautocandidate.md)
- [vnode_cleardirty](./api-1562294-vnode_cleardirty.md)
- [vnode_clearfastdevicecandidate](./api-1562403-vnode_clearfastdevicecandidate.md)
- [vnode_clearfsnode](./api-1562353-vnode_clearfsnode.md)
  Sets a vnode's filesystem-specific data to be NULL.
- [vnode_clearmountedon](./api-1562415-vnode_clearmountedon.md)
  Clear flags indicating that a block device vnode has been mounted as a filesystem.
- [vnode_clearnocache](./api-1562430-vnode_clearnocache.md)
  Clear the flag on a vnode indicating that data should not be cached in memory (i.e. we write-through to disk and always read from disk).
- [vnode_clearnoreadahead](./api-1562228-vnode_clearnoreadahead.md)
  Clear the flag indicating that a vnode should not have data speculatively read in.
- [vnode_close](./api-1562091-vnode_close.md)
  Close a file as opened with vnode_open().
- [vnode_create](./api-1562117-vnode_create.md)
  Create and initialize a vnode.
- [vnode_fsnode](./api-1562316-vnode_fsnode.md)
  Gets the filesystem-specific data associated with a vnode.
- [vnode_get](./api-1562083-vnode_get.md)
  Increase the iocount on a vnode.
- [vnode_get_va_fsid](./api-3130334-vnode_get_va_fsid.md)
- [vnode_getattr](./api-1562270-vnode_getattr.md)
  Get vnode attributes.
- [vnode_getbackingvnode](./api-2977321-vnode_getbackingvnode.md)
- [vnode_getname](./api-1562283-vnode_getname.md)
  Get the name of a vnode from the VFS namecache.
- [vnode_getparent](./api-1562185-vnode_getparent.md)
  Get an iocount on the parent of a vnode.
- [vnode_getwithref](./api-1562306-vnode_getwithref.md)
  Increase the iocount on a vnode on which a usecount (persistent reference) is held.
- [vnode_getwithvid](./api-1562409-vnode_getwithvid.md)
  Increase the iocount on a vnode, checking that the vnode is alive and has not changed vid (i.e. been recycled)
- [vnode_hascleanblks](./api-1562371-vnode_hascleanblks.md)
  Check if a vnode has clean buffers associated with it.
- [vnode_hasdirtyblks](./api-1562463-vnode_hasdirtyblks.md)
  Check if a vnode has dirty data waiting to be written to disk.
- [vnode_isautocandidate](./api-1562339-vnode_isautocandidate.md)
- [vnode_isblk](./api-1562233-vnode_isblk.md)
  Determine if a vnode is a block device special file.
- [vnode_ischr](./api-1562401-vnode_ischr.md)
  Determine if a vnode is a character device special file.
- [vnode_isdir](./api-1562276-vnode_isdir.md)
  Determine if a vnode is a directory.
- [vnode_isdirty](./api-1562357-vnode_isdirty.md)
- [vnode_isfastdevicecandidate](./api-1562391-vnode_isfastdevicecandidate.md)
- [vnode_isfifo](./api-1562153-vnode_isfifo.md)
  Determine if a vnode is a named pipe.
- [vnode_isinuse](./api-1562179-vnode_isinuse.md)
  Determine if the number of persistent (usecount) references on a vnode is greater than a given count.
- [vnode_islnk](./api-1562202-vnode_islnk.md)
  Determine if a vnode is a symbolic link.
- [vnode_ismount](./api-1562400-vnode_ismount.md)
  Determine if there is currently a mount occurring which will cover this vnode.
- [vnode_ismountedon](./api-1562452-vnode_ismountedon.md)
  Determine if a vnode is a block device on which a filesystem has been mounted.
- [vnode_isnamedstream](./api-1562161-vnode_isnamedstream.md)
  Determine if a vnode is a named stream.
- [vnode_isnocache](./api-1562192-vnode_isnocache.md)
  Check if a vnode is set to not have its data cached in memory (i.e. we write-through to disk and always read from disk).
- [vnode_isnoreadahead](./api-1562307-vnode_isnoreadahead.md)
  Check if a vnode is set to not have data speculatively read in in hopes of future cache hits.
- [vnode_isonexternalstorage](./api-3175002-vnode_isonexternalstorage.md)
- [vnode_israge](./api-1562229-vnode_israge.md)
  Check if a vnode is marked for rapid aging
- [vnode_isrecycled](./api-1562214-vnode_isrecycled.md)
  Check if a vnode is dead or in the process of being killed (recycled).
- [vnode_isreg](./api-1562441-vnode_isreg.md)
  Determine if a vnode is a regular file.
- [vnode_isswap](./api-1562252-vnode_isswap.md)
  Determine if a vnode is being used as a swap file.
- [vnode_issystem](./api-1562350-vnode_issystem.md)
  Determine if a vnode is marked as a System vnode.
- [vnode_isvroot](./api-1562236-vnode_isvroot.md)
  Determine if a vnode is the root of its filesystem.
- [vnode_iterate](./api-1562464-vnode_iterate.md)
  Perform an operation on (almost) all vnodes from a given mountpoint.
- [vnode_lookup](./api-1562245-vnode_lookup.md)
  Convert a path into a vnode.
- [vnode_mount](./api-1562358-vnode_mount.md)
  Get the mount structure for the filesystem that a vnode belongs to.
- [vnode_mountedhere](./api-1562327-vnode_mountedhere.md)
  Returns a pointer to a mount placed on top of a vnode, should it exist.
- [vnode_needssnapshots](./api-1562160-vnode_needssnapshots.md)
  Check if a vnode needs snapshots events (regardless of its ctime status)
- [vnode_notify](./api-1562393-vnode_notify.md)
- [vnode_open](./api-1562149-vnode_open.md)
  Open a file identified by a path--roughly speaking an in-kernel open(2).
- [vnode_put](./api-1562280-vnode_put.md)
  Decrement the iocount on a vnode.
- [vnode_putname](./api-1562445-vnode_putname.md)
  Release a reference on a name from the VFS cache.
- [vnode_recycle](./api-1562237-vnode_recycle.md)
  Cause a vnode to be reclaimed and prepared for reuse.
- [vnode_ref](./api-1562240-vnode_ref.md)
  Increment the usecount on a vnode.
- [vnode_rele](./api-1562121-vnode_rele.md)
  Decrement the usecount on a vnode.
- [vnode_removefsref](./api-1562210-vnode_removefsref.md)
  Mark a vnode as no longer being stored in a filesystem hash.
- [vnode_setattr](./api-1562455-vnode_setattr.md)
  Set vnode attributes.
- [vnode_setautocandidate](./api-1562116-vnode_setautocandidate.md)
- [vnode_setdirty](./api-1562289-vnode_setdirty.md)
- [vnode_setfastdevicecandidate](./api-1562221-vnode_setfastdevicecandidate.md)
- [vnode_setmountedon](./api-1562370-vnode_setmountedon.md)
  Set flags indicating that a block device vnode has been mounted as a filesystem.
- [vnode_setmultipath](./api-1562201-vnode_setmultipath.md)
  Mark a vnode as being reachable by multiple paths, i.e. as a hard link.
- [vnode_setnocache](./api-1562318-vnode_setnocache.md)
  Set a vnode to not have its data cached in memory (i.e. we write-through to disk and always read from disk).
- [vnode_setnoreadahead](./api-1562123-vnode_setnoreadahead.md)
  Set a vnode to not have data speculatively read in in hopes of hitting in cache.
- [vnode_settag](./api-1562288-vnode_settag.md)
  Set a vnode filesystem-specific "tag."
- [vnode_specrdev](./api-1562443-vnode_specrdev.md)
  Return the device id of the device associated with a special file.
- [vnode_startwrite](./api-1562369-vnode_startwrite.md)
- [vnode_tag](./api-1562337-vnode_tag.md)
  Get the vnode filesystem-specific "tag."
- [vnode_uncache_credentials](./api-1562109-vnode_uncache_credentials.md)
  Clear out cached credentials on a vnode.
- [vnode_update_identity](./api-1562361-vnode_update_identity.md)
  Update vnode data associated with the vfs cache.
- [vnode_vfs64bitready](./api-1562169-vnode_vfs64bitready.md)
  Determine if the filesystem to which a vnode belongs is marked as ready to interact with 64-bit user processes.
- [vnode_vfsisrdonly](./api-1562081-vnode_vfsisrdonly.md)
  Determine if the filesystem to which a vnode belongs is mounted read-only.
- [vnode_vfsmaxsymlen](./api-1562159-vnode_vfsmaxsymlen.md)
  Determine the maximum length of a symbolic link for the filesystem on which a vnode resides.
- [vnode_vfsname](./api-1562467-vnode_vfsname.md)
  Get the name of the filesystem to which a vnode belongs.
- [vnode_vfstypenum](./api-1562295-vnode_vfstypenum.md)
  Get the "type number" of the filesystem to which a vnode belongs.
- [vnode_vid](./api-1562119-vnode_vid.md)
  Return a vnode's vid (generation number), which is constant from creation until reclaim.
- [vnode_vtype](./api-1562175-vnode_vtype.md)
  Return a vnode's type.
- [vnode_waitforwrites](./api-1562434-vnode_waitforwrites.md)
  Wait for the number of pending writes on a vnode to drop below a target.
- [vnode_writedone](./api-1562375-vnode_writedone.md)
  Decrement the count of pending writes on a vnode .
- [vnode_attr](./vnode_attr.md)
- [vnode_fsparam](./vnode_fsparam.md)
- [vnode_t](./vnode_t.md)
- [vnodeopv_desc](./vnodeopv_desc.md)
- [vnodeopv_entry_desc](./vnodeopv_entry_desc.md)
- [vnop_access_args](./vnop_access_args.md)
  Call down to a filesystem to close a file.
- [vnop_advlock_args](./vnop_advlock_args.md)
  Query a filesystem for path properties.
- [vnop_allocate_args](./vnop_allocate_args.md)
  Aquire or release and advisory lock on a vnode.
- [vnop_blktooff_args](./vnop_blktooff_args.md)
  List extended attribute keys.
- [vnop_blockmap_args](./vnop_blockmap_args.md)
  Call down to a filesystem to convert a file offset to a logical block number.
- [vnop_bwrite_args](./vnop_bwrite_args.md)
- [vnop_clonefile_args](./vnop_clonefile_args.md)
- [vnop_close_args](./vnop_close_args.md)
  Call down to a filesystem to open a file.
- [vnop_copyfile_args](./vnop_copyfile_args.md)
  Write data from a mapped file back to disk.
- [vnop_create_args](./vnop_create_args.md)
  Call down to a filesystem to look for a directory entry by name.
- [vnop_exchange_args](./vnop_exchange_args.md)
  Call down to a filesystem or device to check if a file is ready for I/O and request later notification if it is not currently ready.
- [vnop_fsync_args](./vnop_fsync_args.md)
  Inform a filesystem that a file is no longer mapped.
- [vnop_generic_args](./vnop_generic_args.md)
- [vnop_getattr_args](./vnop_getattr_args.md)
  Call down to a filesystem to see if a kauth-style operation is permitted.
- [vnop_getattrlistbulk_args](./vnop_getattrlistbulk_args.md)
- [vnop_getxattr_args](./vnop_getxattr_args.md)
  Write data from a mapped file back to disk.
- [vnop_inactive_args](./vnop_inactive_args.md)
  Call down to a filesystem to get the pathname represented by a symbolic link.
- [vnop_ioctl_args](./vnop_ioctl_args.md)
- [vnop_kqfilt_add_args](./vnop_kqfilt_add_args.md)
- [vnop_kqfilt_remove_args](./vnop_kqfilt_remove_args.md)
- [vnop_link_args](./vnop_link_args.md)
  Call down to a filesystem to delete a file.
- [vnop_listxattr_args](./vnop_listxattr_args.md)
  Remove extended file attributes.
- [vnop_lookup_args](./vnop_lookup_args.md)
- [vnop_mkdir_args](./vnop_mkdir_args.md)
  Call down to a filesystem to rename a file.
- [vnop_mknod_args](./vnop_mknod_args.md)
  Call down to a filesystem to create a whiteout.
- [vnop_mmap_args](./vnop_mmap_args.md)
  Call down to a filesystem to invalidate all open file descriptors for a vnode.
- [vnop_mmap_check_args](./vnop_mmap_check_args.md)
- [vnop_mnomap_args](./vnop_mnomap_args.md)
  Notify a filesystem that a file is being mmap-ed.
- [vnop_offtoblk_args](./vnop_offtoblk_args.md)
  Call down to a filesystem to convert a logical block number to a file offset.
- [vnop_open_args](./vnop_open_args.md)
  Call down to a filesystem to create a special file.
- [vnop_pagein_args](./vnop_pagein_args.md)
  Pre-allocate space for a file.
- [vnop_pageout_args](./vnop_pageout_args.md)
  Pull file data into memory.
- [vnop_pathconf_args](./vnop_pathconf_args.md)
  Release filesystem-internal resources for a vnode.
- [vnop_read_args](./vnop_read_args.md)
  Call down to a filesystem to set vnode attributes.
- [vnop_readdir_args](./vnop_readdir_args.md)
  Call down to a filesystem to create a symbolic link.
- [vnop_readdirattr_args](./vnop_readdirattr_args.md)
  Call down to a filesystem to enumerate directory entries.
- [vnop_readlink_args](./vnop_readlink_args.md)
  Call down to get file attributes for many files in a directory at once.
- [vnop_reclaim_args](./vnop_reclaim_args.md)
  Notify a filesystem that the last usecount (persistent reference) on a vnode has been dropped.
- [vnop_remove_args](./vnop_remove_args.md)
- [vnop_removexattr_args](./vnop_removexattr_args.md)
- [vnop_rename_args](./vnop_rename_args.md)
  Call down to a filesystem to create a hardlink to a file.
- [vnop_renamex_args](./vnop_renamex_args.md)
- [vnop_revoke_args](./vnop_revoke_args.md)
  Call down to a filesystem to atomically exchange the data of two files.
- [vnop_rmdir_args](./vnop_rmdir_args.md)
  Call down to a filesystem to create a directory.
- [vnop_searchfs_args](./vnop_searchfs_args.md)
  Write data from a mapped file back to disk.
- [vnop_select_args](./vnop_select_args.md)
- [vnop_setattr_args](./vnop_setattr_args.md)
  Call down to a filesystem to get vnode attributes.
- [vnop_setlabel_args](./vnop_setlabel_args.md)
- [vnop_setxattr_args](./vnop_setxattr_args.md)
- [vnop_strategy_args](./vnop_strategy_args.md)
  Call down to a filesystem to get information about the on-disk layout of a file region.
- [vnop_symlink_args](./vnop_symlink_args.md)
  Call down to a filesystem to delete a directory.
- [vnop_whiteout_args](./vnop_whiteout_args.md)
  Call down to a filesystem to create a regular file (VREG).
- [vnop_write_args](./vnop_write_args.md)

## See Also

### BSD
- [architecture](./architecture.md)
  Access machine-level and architectural information about the current platform.
- [bsm](./bsm.md)
  Audit resource usage on the system.
- [hfs](./hfs.md)
  Access HFS file-system data structures. 
- [kern](./kern.md)
  Access kernel-level interfaces including clock, task, kernel extension, lock, and compression utilities.  
- [Math](./math.md)
  Perform mathematical operations and manipulate integer, float, and double values.  
- [miscfs](./miscfs.md)
  Access device nodes and other file-system entities.
- [net](./net.md)
  Access network-related utilities.
- [Strings](./strings.md)
  Compare, convert, and catenate strings and access the resulting content of those strings.
- [vfs](./vfs.md)
  Access the virtual file-system interfaces.
- [vm](./vm.md)
  Interact with the virtual memory system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sys)*