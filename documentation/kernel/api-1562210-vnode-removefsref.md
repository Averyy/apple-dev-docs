# vnode_removefsref

**Framework**: Kernel  
**Kind**: func

Mark a vnode as no longer being stored in a filesystem hash.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vnode_removefsref(vnode_t vp);
```

#### Return_value

Always 0.

#### Discussion

Should only be called once on a vnode (during a reclaim), and only after the vnode has either been created with VNFS_ADDFSREF or marked by vnode_addfsref().

## Parameters

- `vp`: The vnode to unmark.

## See Also

- [vnop_access_desc](vnop_access_desc.md)
- [vnop_advlock_desc](vnop_advlock_desc.md)
- [vnop_allocate_desc](vnop_allocate_desc.md)
- [vnop_blktooff_desc](vnop_blktooff_desc.md)
- [vnop_blockmap_desc](vnop_blockmap_desc.md)
- [vnop_bwrite_desc](vnop_bwrite_desc.md)
- [vnop_clonefile_desc](vnop_clonefile_desc.md)
- [vnop_close_desc](vnop_close_desc.md)
- [vnop_copyfile_desc](vnop_copyfile_desc.md)
- [vnop_create_desc](vnop_create_desc.md)
- [vnop_default_desc](vnop_default_desc.md)
- [vnop_exchange_desc](vnop_exchange_desc.md)
- [vnop_fsync_desc](vnop_fsync_desc.md)
- [vnop_getattr_desc](vnop_getattr_desc.md)
- [vnop_getattrlistbulk_desc](vnop_getattrlistbulk_desc.md)
- [vnop_getxattr_desc](vnop_getxattr_desc.md)
  Write data from a mapped file back to disk.
- [vnop_inactive_desc](vnop_inactive_desc.md)
- [vnop_ioctl_desc](vnop_ioctl_desc.md)
- [vnop_kqfilt_add_desc](vnop_kqfilt_add_desc.md)
- [vnop_kqfilt_remove_desc](vnop_kqfilt_remove_desc.md)
- [vnop_link_desc](vnop_link_desc.md)
- [vnop_listxattr_desc](vnop_listxattr_desc.md)
  Remove extended file attributes.
- [vnop_lookup_desc](vnop_lookup_desc.md)
- [vnop_mkdir_desc](vnop_mkdir_desc.md)
- [vnop_mknod_desc](vnop_mknod_desc.md)
- [vnop_mmap_check_desc](vnop_mmap_check_desc.md)
- [vnop_mmap_desc](vnop_mmap_desc.md)
- [vnop_mnomap_desc](vnop_mnomap_desc.md)
- [vnop_offtoblk_desc](vnop_offtoblk_desc.md)
- [vnop_open_desc](vnop_open_desc.md)
- [vnop_pagein_desc](vnop_pagein_desc.md)
- [vnop_pageout_desc](vnop_pageout_desc.md)
- [vnop_pathconf_desc](vnop_pathconf_desc.md)
- [vnop_print_desc](vnop_print_desc.md)
- [vnop_read_desc](vnop_read_desc.md)
- [vnop_readdir_desc](vnop_readdir_desc.md)
- [vnop_readdirattr_desc](vnop_readdirattr_desc.md)
- [vnop_readlink_desc](vnop_readlink_desc.md)
- [vnop_reclaim_desc](vnop_reclaim_desc.md)
- [vnop_remove_desc](vnop_remove_desc.md)
- [vnop_removexattr_desc](vnop_removexattr_desc.md)
- [vnop_rename_desc](vnop_rename_desc.md)
- [vnop_renamex_desc](vnop_renamex_desc.md)
- [vnop_revoke_desc](vnop_revoke_desc.md)
- [vnop_rmdir_desc](vnop_rmdir_desc.md)
- [vnop_searchfs_desc](vnop_searchfs_desc.md)
- [vnop_select_desc](vnop_select_desc.md)
- [vnop_setattr_desc](vnop_setattr_desc.md)
- [vnop_setlabel_desc](vnop_setlabel_desc.md)
- [vnop_setxattr_desc](vnop_setxattr_desc.md)
- [vnop_strategy_desc](vnop_strategy_desc.md)
- [vnop_symlink_desc](vnop_symlink_desc.md)
- [vnop_truncate_desc](vnop_truncate_desc.md)
- [vnop_whiteout_desc](vnop_whiteout_desc.md)
- [vnop_write_desc](vnop_write_desc.md)
- [vnode_addfsref](1562216-vnode_addfsref.md)
  Mark a vnode as being stored in a filesystem hash.
- [vnode_authattr](1562106-vnode_authattr.md)
  Given a vnode_attr structure, determine what kauth-style actions must be authorized in order to set those attributes.
- [vnode_authattr_new](1562184-vnode_authattr_new.md)
  Initialize and validate file creation parameters with respect to the current context.
- [vnode_authorize](1562084-vnode_authorize.md)
  Authorize a kauth-style action on a vnode.
- [vnode_clearautocandidate](1562373-vnode_clearautocandidate.md)
- [vnode_cleardirty](1562294-vnode_cleardirty.md)
- [vnode_clearfastdevicecandidate](1562403-vnode_clearfastdevicecandidate.md)
- [vnode_clearfsnode](1562353-vnode_clearfsnode.md)
  Sets a vnode's filesystem-specific data to be NULL.
- [vnode_clearmountedon](1562415-vnode_clearmountedon.md)
  Clear flags indicating that a block device vnode has been mounted as a filesystem.
- [vnode_clearnocache](1562430-vnode_clearnocache.md)
  Clear the flag on a vnode indicating that data should not be cached in memory (i.e. we write-through to disk and always read from disk).
- [vnode_clearnoreadahead](1562228-vnode_clearnoreadahead.md)
  Clear the flag indicating that a vnode should not have data speculatively read in.
- [vnode_close](1562091-vnode_close.md)
  Close a file as opened with vnode_open().
- [vnode_create](1562117-vnode_create.md)
  Create and initialize a vnode.
- [vnode_fsnode](1562316-vnode_fsnode.md)
  Gets the filesystem-specific data associated with a vnode.
- [vnode_get](1562083-vnode_get.md)
  Increase the iocount on a vnode.
- [vnode_get_va_fsid](3130334-vnode_get_va_fsid.md)
- [vnode_getattr](1562270-vnode_getattr.md)
  Get vnode attributes.
- [vnode_getbackingvnode](2977321-vnode_getbackingvnode.md)
- [vnode_getname](1562283-vnode_getname.md)
  Get the name of a vnode from the VFS namecache.
- [vnode_getparent](1562185-vnode_getparent.md)
  Get an iocount on the parent of a vnode.
- [vnode_getwithref](1562306-vnode_getwithref.md)
  Increase the iocount on a vnode on which a usecount (persistent reference) is held.
- [vnode_getwithvid](1562409-vnode_getwithvid.md)
  Increase the iocount on a vnode, checking that the vnode is alive and has not changed vid (i.e. been recycled)
- [vnode_hascleanblks](1562371-vnode_hascleanblks.md)
  Check if a vnode has clean buffers associated with it.
- [vnode_hasdirtyblks](1562463-vnode_hasdirtyblks.md)
  Check if a vnode has dirty data waiting to be written to disk.
- [vnode_isautocandidate](1562339-vnode_isautocandidate.md)
- [vnode_isblk](1562233-vnode_isblk.md)
  Determine if a vnode is a block device special file.
- [vnode_ischr](1562401-vnode_ischr.md)
  Determine if a vnode is a character device special file.
- [vnode_isdir](1562276-vnode_isdir.md)
  Determine if a vnode is a directory.
- [vnode_isdirty](1562357-vnode_isdirty.md)
- [vnode_isfastdevicecandidate](1562391-vnode_isfastdevicecandidate.md)
- [vnode_isfifo](1562153-vnode_isfifo.md)
  Determine if a vnode is a named pipe.
- [vnode_isinuse](1562179-vnode_isinuse.md)
  Determine if the number of persistent (usecount) references on a vnode is greater than a given count.
- [vnode_islnk](1562202-vnode_islnk.md)
  Determine if a vnode is a symbolic link.
- [vnode_ismount](1562400-vnode_ismount.md)
  Determine if there is currently a mount occurring which will cover this vnode.
- [vnode_ismountedon](1562452-vnode_ismountedon.md)
  Determine if a vnode is a block device on which a filesystem has been mounted.
- [vnode_isnamedstream](1562161-vnode_isnamedstream.md)
  Determine if a vnode is a named stream.
- [vnode_isnocache](1562192-vnode_isnocache.md)
  Check if a vnode is set to not have its data cached in memory (i.e. we write-through to disk and always read from disk).
- [vnode_isnoreadahead](1562307-vnode_isnoreadahead.md)
  Check if a vnode is set to not have data speculatively read in in hopes of future cache hits.
- [vnode_isonexternalstorage](3175002-vnode_isonexternalstorage.md)
- [vnode_israge](1562229-vnode_israge.md)
  Check if a vnode is marked for rapid aging
- [vnode_isrecycled](1562214-vnode_isrecycled.md)
  Check if a vnode is dead or in the process of being killed (recycled).
- [vnode_isreg](1562441-vnode_isreg.md)
  Determine if a vnode is a regular file.
- [vnode_isswap](1562252-vnode_isswap.md)
  Determine if a vnode is being used as a swap file.
- [vnode_issystem](1562350-vnode_issystem.md)
  Determine if a vnode is marked as a System vnode.
- [vnode_isvroot](1562236-vnode_isvroot.md)
  Determine if a vnode is the root of its filesystem.
- [vnode_iterate](1562464-vnode_iterate.md)
  Perform an operation on (almost) all vnodes from a given mountpoint.
- [vnode_lookup](1562245-vnode_lookup.md)
  Convert a path into a vnode.
- [vnode_mount](1562358-vnode_mount.md)
  Get the mount structure for the filesystem that a vnode belongs to.
- [vnode_mountedhere](1562327-vnode_mountedhere.md)
  Returns a pointer to a mount placed on top of a vnode, should it exist.
- [vnode_needssnapshots](1562160-vnode_needssnapshots.md)
  Check if a vnode needs snapshots events (regardless of its ctime status)
- [vnode_notify](1562393-vnode_notify.md)
- [vnode_open](1562149-vnode_open.md)
  Open a file identified by a path--roughly speaking an in-kernel open(2).
- [vnode_put](1562280-vnode_put.md)
  Decrement the iocount on a vnode.
- [vnode_putname](1562445-vnode_putname.md)
  Release a reference on a name from the VFS cache.
- [vnode_recycle](1562237-vnode_recycle.md)
  Cause a vnode to be reclaimed and prepared for reuse.
- [vnode_ref](1562240-vnode_ref.md)
  Increment the usecount on a vnode.
- [vnode_rele](1562121-vnode_rele.md)
  Decrement the usecount on a vnode.
- [vnode_setattr](1562455-vnode_setattr.md)
  Set vnode attributes.
- [vnode_setautocandidate](1562116-vnode_setautocandidate.md)
- [vnode_setdirty](1562289-vnode_setdirty.md)
- [vnode_setfastdevicecandidate](1562221-vnode_setfastdevicecandidate.md)
- [vnode_setmountedon](1562370-vnode_setmountedon.md)
  Set flags indicating that a block device vnode has been mounted as a filesystem.
- [vnode_setmultipath](1562201-vnode_setmultipath.md)
  Mark a vnode as being reachable by multiple paths, i.e. as a hard link.
- [vnode_setnocache](1562318-vnode_setnocache.md)
  Set a vnode to not have its data cached in memory (i.e. we write-through to disk and always read from disk).
- [vnode_setnoreadahead](1562123-vnode_setnoreadahead.md)
  Set a vnode to not have data speculatively read in in hopes of hitting in cache.
- [vnode_settag](1562288-vnode_settag.md)
  Set a vnode filesystem-specific "tag."
- [vnode_specrdev](1562443-vnode_specrdev.md)
  Return the device id of the device associated with a special file.
- [vnode_startwrite](1562369-vnode_startwrite.md)
- [vnode_tag](1562337-vnode_tag.md)
  Get the vnode filesystem-specific "tag."
- [vnode_uncache_credentials](1562109-vnode_uncache_credentials.md)
  Clear out cached credentials on a vnode.
- [vnode_update_identity](1562361-vnode_update_identity.md)
  Update vnode data associated with the vfs cache.
- [vnode_vfs64bitready](1562169-vnode_vfs64bitready.md)
  Determine if the filesystem to which a vnode belongs is marked as ready to interact with 64-bit user processes.
- [vnode_vfsisrdonly](1562081-vnode_vfsisrdonly.md)
  Determine if the filesystem to which a vnode belongs is mounted read-only.
- [vnode_vfsmaxsymlen](1562159-vnode_vfsmaxsymlen.md)
  Determine the maximum length of a symbolic link for the filesystem on which a vnode resides.
- [vnode_vfsname](1562467-vnode_vfsname.md)
  Get the name of the filesystem to which a vnode belongs.
- [vnode_vfstypenum](1562295-vnode_vfstypenum.md)
  Get the "type number" of the filesystem to which a vnode belongs.
- [vnode_vid](1562119-vnode_vid.md)
  Return a vnode's vid (generation number), which is constant from creation until reclaim.
- [vnode_vtype](1562175-vnode_vtype.md)
  Return a vnode's type.
- [vnode_waitforwrites](1562434-vnode_waitforwrites.md)
  Wait for the number of pending writes on a vnode to drop below a target.
- [vnode_writedone](1562375-vnode_writedone.md)
  Decrement the count of pending writes on a vnode .
- [vnode_attr](vnode_attr.md)
- [vnode_fsparam](vnode_fsparam.md)
- [vnode_t](vnode_t.md)
- [vnodeopv_desc](vnodeopv_desc.md)
- [vnodeopv_entry_desc](vnodeopv_entry_desc.md)
- [vnop_access_args](vnop_access_args.md)
  Call down to a filesystem to close a file.
- [vnop_advlock_args](vnop_advlock_args.md)
  Query a filesystem for path properties.
- [vnop_allocate_args](vnop_allocate_args.md)
  Aquire or release and advisory lock on a vnode.
- [vnop_blktooff_args](vnop_blktooff_args.md)
  List extended attribute keys.
- [vnop_blockmap_args](vnop_blockmap_args.md)
  Call down to a filesystem to convert a file offset to a logical block number.
- [vnop_bwrite_args](vnop_bwrite_args.md)
- [vnop_clonefile_args](vnop_clonefile_args.md)
- [vnop_close_args](vnop_close_args.md)
  Call down to a filesystem to open a file.
- [vnop_copyfile_args](vnop_copyfile_args.md)
  Write data from a mapped file back to disk.
- [vnop_create_args](vnop_create_args.md)
  Call down to a filesystem to look for a directory entry by name.
- [vnop_exchange_args](vnop_exchange_args.md)
  Call down to a filesystem or device to check if a file is ready for I/O and request later notification if it is not currently ready.
- [vnop_fsync_args](vnop_fsync_args.md)
  Inform a filesystem that a file is no longer mapped.
- [vnop_generic_args](vnop_generic_args.md)
- [vnop_getattr_args](vnop_getattr_args.md)
  Call down to a filesystem to see if a kauth-style operation is permitted.
- [vnop_getattrlistbulk_args](vnop_getattrlistbulk_args.md)
- [vnop_getxattr_args](vnop_getxattr_args.md)
  Write data from a mapped file back to disk.
- [vnop_inactive_args](vnop_inactive_args.md)
  Call down to a filesystem to get the pathname represented by a symbolic link.
- [vnop_ioctl_args](vnop_ioctl_args.md)
- [vnop_kqfilt_add_args](vnop_kqfilt_add_args.md)
- [vnop_kqfilt_remove_args](vnop_kqfilt_remove_args.md)
- [vnop_link_args](vnop_link_args.md)
  Call down to a filesystem to delete a file.
- [vnop_listxattr_args](vnop_listxattr_args.md)
  Remove extended file attributes.
- [vnop_lookup_args](vnop_lookup_args.md)
- [vnop_mkdir_args](vnop_mkdir_args.md)
  Call down to a filesystem to rename a file.
- [vnop_mknod_args](vnop_mknod_args.md)
  Call down to a filesystem to create a whiteout.
- [vnop_mmap_args](vnop_mmap_args.md)
  Call down to a filesystem to invalidate all open file descriptors for a vnode.
- [vnop_mmap_check_args](vnop_mmap_check_args.md)
- [vnop_mnomap_args](vnop_mnomap_args.md)
  Notify a filesystem that a file is being mmap-ed.
- [vnop_offtoblk_args](vnop_offtoblk_args.md)
  Call down to a filesystem to convert a logical block number to a file offset.
- [vnop_open_args](vnop_open_args.md)
  Call down to a filesystem to create a special file.
- [vnop_pagein_args](vnop_pagein_args.md)
  Pre-allocate space for a file.
- [vnop_pageout_args](vnop_pageout_args.md)
  Pull file data into memory.
- [vnop_pathconf_args](vnop_pathconf_args.md)
  Release filesystem-internal resources for a vnode.
- [vnop_read_args](vnop_read_args.md)
  Call down to a filesystem to set vnode attributes.
- [vnop_readdir_args](vnop_readdir_args.md)
  Call down to a filesystem to create a symbolic link.
- [vnop_readdirattr_args](vnop_readdirattr_args.md)
  Call down to a filesystem to enumerate directory entries.
- [vnop_readlink_args](vnop_readlink_args.md)
  Call down to get file attributes for many files in a directory at once.
- [vnop_reclaim_args](vnop_reclaim_args.md)
  Notify a filesystem that the last usecount (persistent reference) on a vnode has been dropped.
- [vnop_remove_args](vnop_remove_args.md)
- [vnop_removexattr_args](vnop_removexattr_args.md)
- [vnop_rename_args](vnop_rename_args.md)
  Call down to a filesystem to create a hardlink to a file.
- [vnop_renamex_args](vnop_renamex_args.md)
- [vnop_revoke_args](vnop_revoke_args.md)
  Call down to a filesystem to atomically exchange the data of two files.
- [vnop_rmdir_args](vnop_rmdir_args.md)
  Call down to a filesystem to create a directory.
- [vnop_searchfs_args](vnop_searchfs_args.md)
  Write data from a mapped file back to disk.
- [vnop_select_args](vnop_select_args.md)
- [vnop_setattr_args](vnop_setattr_args.md)
  Call down to a filesystem to get vnode attributes.
- [vnop_setlabel_args](vnop_setlabel_args.md)
- [vnop_setxattr_args](vnop_setxattr_args.md)
- [vnop_strategy_args](vnop_strategy_args.md)
  Call down to a filesystem to get information about the on-disk layout of a file region.
- [vnop_symlink_args](vnop_symlink_args.md)
  Call down to a filesystem to delete a directory.
- [vnop_whiteout_args](vnop_whiteout_args.md)
  Call down to a filesystem to create a regular file (VREG).
- [vnop_write_args](vnop_write_args.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562210-vnode_removefsref)*