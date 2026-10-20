# vfs

**Framework**: Kernel  
**Role**: API Collection

Access the virtual file-system interfaces.

## Topics

### Functions
- [vflush](./api-1562120-vflush.md)
  Reclaim the vnodes for a mount.
- [vfs_64bitready](./api-1523312-vfs_64bitready.md)
  Check if the filesystem associated with a mountpoint is marked ready for interaction with 64-bit user processes.
- [vfs_addname](./api-1562422-vfs_addname.md)
  Deprecated
- [vfs_attr_pack](./api-1562242-vfs_attr_pack.md)
- [vfs_attr_pack_ext](./api-3353091-vfs_attr_pack_ext.md)
- [vfs_authcache_ttl](./api-1523180-vfs_authcache_ttl.md)
  Determine the time-to-live of cached authorized credentials for files in this filesystem.
- [vfs_authopaque](./api-1523276-vfs_authopaque.md)
  Determine if a filesystem's authorization decisions occur remotely.
- [vfs_authopaqueaccess](./api-1523247-vfs_authopaqueaccess.md)
  Check if a filesystem is marked as having reliable remote VNOP_ACCESS support.
- [vfs_busy](./api-1523389-vfs_busy.md)
  "Busy" a mountpoint.
- [vfs_clearauthcache_ttl](./api-1523469-vfs_clearauthcache_ttl.md)
  Remove time-to-live controls for cached credentials on a filesytem. Filesystems with remote authorization decisions (opaque) will still have KAUTH_VNODE_SEARCH rights cached for a default of CACHED_LOOKUP_RIGHT_TTL seconds.
- [vfs_clearauthopaque](./api-1523223-vfs_clearauthopaque.md)
- [vfs_clearauthopaqueaccess](./api-1523231-vfs_clearauthopaqueaccess.md)
  Mark a filesystem as not having remote VNOP_ACCESS support.
- [vfs_clearextendedsecurity](./api-1523368-vfs_clearextendedsecurity.md)
  Mark a filesystem as NOT supporting security controls beyond POSIX permissions.
- [vfs_clearflags](./api-1523299-vfs_clearflags.md)
  Clear flags on a mount.
- [vfs_context_create](./api-1562360-vfs_context_create.md)
  Create a new vfs_context_t with appropriate references held.
- [vfs_context_current](./api-1562223-vfs_context_current.md)
  Get the vfs_context for the current thread, or the kernel context if there is no context for current thread.
- [vfs_context_get_special_port](./api-1562113-vfs_context_get_special_port.md)
- [vfs_context_is64bit](./api-1562122-vfs_context_is64bit.md)
  Determine if a vfs_context_t corresponds to a 64-bit user process.
- [vfs_context_issignal](./api-1562448-vfs_context_issignal.md)
  Get a bitfield of pending signals for the BSD process associated with a vfs_context_t.
- [vfs_context_pid](./api-1562461-vfs_context_pid.md)
  Get the process id of the BSD process associated with a vfs_context_t.
- [vfs_context_proc](./api-1562390-vfs_context_proc.md)
  Get the BSD process structure associated with a vfs_context_t.
- [vfs_context_rele](./api-1562367-vfs_context_rele.md)
  Release references on components of a context and deallocate it.
- [vfs_context_set_special_port](./api-1562263-vfs_context_set_special_port.md)
- [vfs_context_suser](./api-1562261-vfs_context_suser.md)
  Determine if a vfs_context_t corresponds to the superuser.
- [vfs_context_ucred](./api-1562308-vfs_context_ucred.md)
  Get the credential associated with a vfs_context_t.
- [vfs_devblocksize](./api-1523172-vfs_devblocksize.md)
  Get the block size of the device underlying a mount.
- [vfs_event_init](./api-1523461-vfs_event_init.md)
  This function should not be called by kexts.
- [vfs_event_signal](./api-1523107-vfs_event_signal.md)
  Post a kqueue-style event on a filesystem (EVFILT_FS).
- [vfs_flags](./api-1523261-vfs_flags.md)
  Retrieve mount flags.
- [vfs_fsadd](./api-1523490-vfs_fsadd.md)
  Register a filesystem with VFS.
- [vfs_fsprivate](./api-1523301-vfs_fsprivate.md)
  Get filesystem-private mount data.
- [vfs_fsremove](./api-1523194-vfs_fsremove.md)
  Unregister a filesystem with VFS.
- [vfs_get_notify_attributes](./api-1562277-vfs_get_notify_attributes.md)
- [vfs_getnewfsid](./api-1523259-vfs_getnewfsid.md)
  Generate a unique filesystem ID for a mount and store it in the mount structure.
- [vfs_getvfs](./api-1523465-vfs_getvfs.md)
  Given a filesystem ID, look up a mount structure.
- [vfs_init_io_attributes](./api-1523109-vfs_init_io_attributes.md)
  Set I/O attributes on a mountpoint based on device properties.
- [vfs_ioattr](./api-1523411-vfs_ioattr.md)
  Get I/O attributes associated with a mounpoint.
- [vfs_isforce](./api-1523525-vfs_isforce.md)
  Determine if a forced unmount is in progress.
- [vfs_isrdonly](./api-1523242-vfs_isrdonly.md)
  Determine if a filesystem is mounted read-only.
- [vfs_isrdwr](./api-1523454-vfs_isrdwr.md)
  Determine if a filesystem is mounted with writes enabled.
- [vfs_isreload](./api-1523537-vfs_isreload.md)
  Determine if a reload of filesystem data is in progress. This can only be the case for a read-only filesystem; all data is brought in from secondary storage.
- [vfs_issynchronous](./api-1523327-vfs_issynchronous.md)
  Determine if writes to a filesystem occur synchronously.
- [vfs_isunmount](./api-1523380-vfs_isunmount.md)
  Determine if an unmount is in progress.
- [vfs_isupdate](./api-1523536-vfs_isupdate.md)
  Determine if a mount update is in progress.
- [vfs_iswriteupgrade](./api-1523486-vfs_iswriteupgrade.md)
  Determine if a filesystem is mounted read-only but a request has been made to upgrade to read-write.
- [vfs_iterate](./api-1523233-vfs_iterate.md)
  Iterate over all mountpoints with a callback. Used, for example, by sync().
- [vfs_maxsymlen](./api-1523507-vfs_maxsymlen.md)
  Get the maximum length of a symbolic link on a filesystem.
- [vfs_mountedon](./api-1523197-vfs_mountedon.md)
  Check whether a given block device has a filesystem mounted on it.
- [vfs_name](./api-1523128-vfs_name.md)
  Copy filesystem name into a buffer.
- [vfs_nspace_server](./api-3042879-vfs_nspace_server.md)
- [vfs_nspace_server_routine](./api-3042880-vfs_nspace_server_routine.md)
- [vfs_removename](./api-1562343-vfs_removename.md)
  Deprecated
- [vfs_rootvnode](./api-1562439-vfs_rootvnode.md)
  Returns the root vnode with an iocount.
- [vfs_set_root_unmounted_cleanly](./api-2872995-vfs_set_root_unmounted_cleanly.md)
- [vfs_setauthcache_ttl](./api-1523286-vfs_setauthcache_ttl.md)
  Enable credential caching and set time-to-live of cached authorized credentials for files in this filesystem.
- [vfs_setauthopaque](./api-1523440-vfs_setauthopaque.md)
  Mark a filesystem as having authorization decisions controlled remotely.
- [vfs_setauthopaqueaccess](./api-1523218-vfs_setauthopaqueaccess.md)
  Mark a filesystem as having remote VNOP_ACCESS support.
- [vfs_setextendedsecurity](./api-1523360-vfs_setextendedsecurity.md)
  Mark a filesystem as supporting security controls beyond POSIX permissions.
- [vfs_setflags](./api-1523521-vfs_setflags.md)
  Set flags on a mount.
- [vfs_setfsprivate](./api-1523413-vfs_setfsprivate.md)
  Set filesystem-private mount data.
- [vfs_setioattr](./api-1523458-vfs_setioattr.md)
  Set I/O attributes associated with a mounpoint.
- [vfs_setlocklocal](./api-1523104-vfs_setlocklocal.md)
  Mark a filesystem as using VFS-level advisory locking support.
- [vfs_setmaxsymlen](./api-1523316-vfs_setmaxsymlen.md)
  Set the maximum length of a symbolic link on a filesystem.
- [vfs_setup_vattr_from_attrlist](./api-1562135-vfs_setup_vattr_from_attrlist.md)
- [vfs_statfs](./api-1523098-vfs_statfs.md)
  Get information about filesystem status.
- [vfs_typenum](./api-1523418-vfs_typenum.md)
  Get (archaic) filesystem type number.
- [vfs_unbusy](./api-1523451-vfs_unbusy.md)
  "Unbusy" a mountpoint by releasing its read-write lock.
- [vfs_unmountbyfsid](./api-1523503-vfs_unmountbyfsid.md)
  Find a filesystem by ID and unmount it.
- [vfs_update_vfsstat](./api-1523278-vfs_update_vfsstat.md)
  Update cached filesystem status information in the VFS mount structure.
### Support
- [nop_access](./api-1523716-nop_access.md)
- [nop_advlock](./api-1523779-nop_advlock.md)
- [nop_allocate](./api-1523773-nop_allocate.md)
- [nop_blktooff](./api-1523748-nop_blktooff.md)
- [nop_blockmap](./api-1523729-nop_blockmap.md)
- [nop_bwrite](./api-1523755-nop_bwrite.md)
- [nop_close](./api-1523718-nop_close.md)
- [nop_copyfile](./api-1523720-nop_copyfile.md)
- [nop_create](./api-1523722-nop_create.md)
- [nop_exchange](./api-1523694-nop_exchange.md)
- [nop_fsync](./api-1523723-nop_fsync.md)
- [nop_getattr](./api-1523698-nop_getattr.md)
- [nop_inactive](./api-1523711-nop_inactive.md)
- [nop_ioctl](./api-1523715-nop_ioctl.md)
- [nop_link](./api-1523693-nop_link.md)
- [nop_mkdir](./api-1523677-nop_mkdir.md)
- [nop_mknod](./api-1523731-nop_mknod.md)
- [nop_mmap](./api-1523753-nop_mmap.md)
- [nop_offtoblk](./api-1523783-nop_offtoblk.md)
- [nop_open](./api-1523733-nop_open.md)
- [nop_pagein](./api-1523686-nop_pagein.md)
- [nop_pageout](./api-1523770-nop_pageout.md)
- [nop_pathconf](./api-1523727-nop_pathconf.md)
- [nop_read](./api-1523765-nop_read.md)
- [nop_readdir](./api-1523710-nop_readdir.md)
- [nop_readdirattr](./api-1523717-nop_readdirattr.md)
- [nop_readlink](./api-1523774-nop_readlink.md)
- [nop_reclaim](./api-1523708-nop_reclaim.md)
- [nop_remove](./api-1523713-nop_remove.md)
- [nop_rename](./api-1523741-nop_rename.md)
- [nop_revoke](./api-1523764-nop_revoke.md)
- [nop_rmdir](./api-1523767-nop_rmdir.md)
- [nop_searchfs](./api-1523744-nop_searchfs.md)
- [nop_select](./api-1523738-nop_select.md)
- [nop_setattr](./api-1523719-nop_setattr.md)
- [nop_strategy](./api-1523746-nop_strategy.md)
- [nop_symlink](./api-1523696-nop_symlink.md)
- [nop_whiteout](./api-1523682-nop_whiteout.md)
- [nop_write](./api-1523695-nop_write.md)
- [err_access](./api-1523742-err_access.md)
- [err_advlock](./api-1523766-err_advlock.md)
- [err_allocate](./api-1523740-err_allocate.md)
- [err_blktooff](./api-1523777-err_blktooff.md)
- [err_blockmap](./api-1523771-err_blockmap.md)
- [err_bwrite](./api-1523737-err_bwrite.md)
- [err_close](./api-1523768-err_close.md)
- [err_copyfile](./api-1523763-err_copyfile.md)
- [err_create](./api-1523690-err_create.md)
- [err_exchange](./api-1523683-err_exchange.md)
- [err_fsync](./api-1523761-err_fsync.md)
- [err_getattr](./api-1523757-err_getattr.md)
- [err_inactive](./api-1523681-err_inactive.md)
- [err_ioctl](./api-1523684-err_ioctl.md)
- [err_link](./api-1523732-err_link.md)
- [err_mkdir](./api-1523751-err_mkdir.md)
- [err_mknod](./api-1523750-err_mknod.md)
- [err_mmap](./api-1523704-err_mmap.md)
- [err_offtoblk](./api-1523781-err_offtoblk.md)
- [err_open](./api-1523735-err_open.md)
- [err_pagein](./api-1523688-err_pagein.md)
- [err_pageout](./api-1523700-err_pageout.md)
- [err_pathconf](./api-1523679-err_pathconf.md)
- [err_read](./api-1523775-err_read.md)
- [err_readdir](./api-1523691-err_readdir.md)
- [err_readdirattr](./api-1523705-err_readdirattr.md)
- [err_readlink](./api-1523739-err_readlink.md)
- [err_reclaim](./api-1523726-err_reclaim.md)
- [err_remove](./api-1523769-err_remove.md)
- [err_rename](./api-1523706-err_rename.md)
- [err_revoke](./api-1523736-err_revoke.md)
- [err_rmdir](./api-1523772-err_rmdir.md)
- [err_searchfs](./api-1523702-err_searchfs.md)
- [err_select](./api-1523714-err_select.md)
- [err_setattr](./api-1523786-err_setattr.md)
- [err_strategy](./api-1523730-err_strategy.md)
- [err_symlink](./api-1523759-err_symlink.md)
- [err_whiteout](./api-1523785-err_whiteout.md)
- [err_write](./api-1523725-err_write.md)
- [advisory_read](./api-1463716-advisory_read.md)
- [advisory_read_ext](./api-1463707-advisory_read_ext.md)
- [VNOP_BWRITE](./api-1585961-vnop_bwrite.md)
  Write a buffer to backing store.
- [VNOP_FSYNC](./api-1586212-vnop_fsync.md)
  Call down to a filesystem to synchronize a file with on-disk state.
- [VNOP_GETXATTR](./api-1586289-vnop_getxattr.md)
  Get extended file attributes.
- [VNOP_IOCTL](./api-1586258-vnop_ioctl.md)
  Call down to a filesystem or device driver to execute various control operations on or request data about a file.
- [VNOP_READ](./api-1586326-vnop_read.md)
  Call down to a filesystem to read file data.
- [VNOP_SETXATTR](./api-1586200-vnop_setxattr.md)
  Set extended file attributes.
- [VNOP_STRATEGY](./api-1586257-vnop_strategy.md)
  Initiate I/O on a file (both read and write).
- [VNOP_WRITE](./api-1586129-vnop_write.md)
  Call down to the filesystem to write file data.
- [cache_enter](./api-1562285-cache_enter.md)
  Add a (name,vnode) entry to the VFS namecache.
- [cache_lookup](./api-1562195-cache_lookup.md)
  Check for a filename in a directory using the VFS name cache.
- [cache_purge](./api-1562225-cache_purge.md)
  Remove all data relating to a vnode from the namecache.
- [cache_purge_negatives](./api-1562456-cache_purge_negatives.md)
  Remove all negative cache entries which are children of a given vnode.

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
- [sys](./sys.md)
  Access general system utilities for time, file systems, and system information.
- [vm](./vm.md)
  Interact with the virtual memory system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/vfs)*