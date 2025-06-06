# nop_getattr

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
int nop_getattr(struct vnop_getattr_args *ap);
```

## See Also

- [nop_access](1523716-nop_access.md)
- [nop_advlock](1523779-nop_advlock.md)
- [nop_allocate](1523773-nop_allocate.md)
- [nop_blktooff](1523748-nop_blktooff.md)
- [nop_blockmap](1523729-nop_blockmap.md)
- [nop_bwrite](1523755-nop_bwrite.md)
- [nop_close](1523718-nop_close.md)
- [nop_copyfile](1523720-nop_copyfile.md)
- [nop_create](1523722-nop_create.md)
- [nop_exchange](1523694-nop_exchange.md)
- [nop_fsync](1523723-nop_fsync.md)
- [nop_inactive](1523711-nop_inactive.md)
- [nop_ioctl](1523715-nop_ioctl.md)
- [nop_link](1523693-nop_link.md)
- [nop_mkdir](1523677-nop_mkdir.md)
- [nop_mknod](1523731-nop_mknod.md)
- [nop_mmap](1523753-nop_mmap.md)
- [nop_offtoblk](1523783-nop_offtoblk.md)
- [nop_open](1523733-nop_open.md)
- [nop_pagein](1523686-nop_pagein.md)
- [nop_pageout](1523770-nop_pageout.md)
- [nop_pathconf](1523727-nop_pathconf.md)
- [nop_read](1523765-nop_read.md)
- [nop_readdir](1523710-nop_readdir.md)
- [nop_readdirattr](1523717-nop_readdirattr.md)
- [nop_readlink](1523774-nop_readlink.md)
- [nop_reclaim](1523708-nop_reclaim.md)
- [nop_remove](1523713-nop_remove.md)
- [nop_rename](1523741-nop_rename.md)
- [nop_revoke](1523764-nop_revoke.md)
- [nop_rmdir](1523767-nop_rmdir.md)
- [nop_searchfs](1523744-nop_searchfs.md)
- [nop_select](1523738-nop_select.md)
- [nop_setattr](1523719-nop_setattr.md)
- [nop_strategy](1523746-nop_strategy.md)
- [nop_symlink](1523696-nop_symlink.md)
- [nop_whiteout](1523682-nop_whiteout.md)
- [nop_write](1523695-nop_write.md)
- [err_access](1523742-err_access.md)
- [err_advlock](1523766-err_advlock.md)
- [err_allocate](1523740-err_allocate.md)
- [err_blktooff](1523777-err_blktooff.md)
- [err_blockmap](1523771-err_blockmap.md)
- [err_bwrite](1523737-err_bwrite.md)
- [err_close](1523768-err_close.md)
- [err_copyfile](1523763-err_copyfile.md)
- [err_create](1523690-err_create.md)
- [err_exchange](1523683-err_exchange.md)
- [err_fsync](1523761-err_fsync.md)
- [err_getattr](1523757-err_getattr.md)
- [err_inactive](1523681-err_inactive.md)
- [err_ioctl](1523684-err_ioctl.md)
- [err_link](1523732-err_link.md)
- [err_mkdir](1523751-err_mkdir.md)
- [err_mknod](1523750-err_mknod.md)
- [err_mmap](1523704-err_mmap.md)
- [err_offtoblk](1523781-err_offtoblk.md)
- [err_open](1523735-err_open.md)
- [err_pagein](1523688-err_pagein.md)
- [err_pageout](1523700-err_pageout.md)
- [err_pathconf](1523679-err_pathconf.md)
- [err_read](1523775-err_read.md)
- [err_readdir](1523691-err_readdir.md)
- [err_readdirattr](1523705-err_readdirattr.md)
- [err_readlink](1523739-err_readlink.md)
- [err_reclaim](1523726-err_reclaim.md)
- [err_remove](1523769-err_remove.md)
- [err_rename](1523706-err_rename.md)
- [err_revoke](1523736-err_revoke.md)
- [err_rmdir](1523772-err_rmdir.md)
- [err_searchfs](1523702-err_searchfs.md)
- [err_select](1523714-err_select.md)
- [err_setattr](1523786-err_setattr.md)
- [err_strategy](1523730-err_strategy.md)
- [err_symlink](1523759-err_symlink.md)
- [err_whiteout](1523785-err_whiteout.md)
- [err_write](1523725-err_write.md)
- [advisory_read](1463716-advisory_read.md)
- [advisory_read_ext](1463707-advisory_read_ext.md)
- [VNOP_BWRITE](1585961-vnop_bwrite.md)
  Write a buffer to backing store.
- [VNOP_FSYNC](1586212-vnop_fsync.md)
  Call down to a filesystem to synchronize a file with on-disk state.
- [VNOP_GETXATTR](1586289-vnop_getxattr.md)
  Get extended file attributes.
- [VNOP_IOCTL](1586258-vnop_ioctl.md)
  Call down to a filesystem or device driver to execute various control operations on or request data about a file.
- [VNOP_READ](1586326-vnop_read.md)
  Call down to a filesystem to read file data.
- [VNOP_SETXATTR](1586200-vnop_setxattr.md)
  Set extended file attributes.
- [VNOP_STRATEGY](1586257-vnop_strategy.md)
  Initiate I/O on a file (both read and write).
- [VNOP_WRITE](1586129-vnop_write.md)
  Call down to the filesystem to write file data.
- [cache_enter](1562285-cache_enter.md)
  Add a (name,vnode) entry to the VFS namecache.
- [cache_lookup](1562195-cache_lookup.md)
  Check for a filename in a directory using the VFS name cache.
- [cache_purge](1562225-cache_purge.md)
  Remove all data relating to a vnode from the namecache.
- [cache_purge_negatives](1562456-cache_purge_negatives.md)
  Remove all negative cache entries which are children of a given vnode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523698-nop_getattr)*