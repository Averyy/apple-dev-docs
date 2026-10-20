# cluster_pagein_ext

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.9+

## Declaration

```c
int cluster_pagein_ext(vnode_t, upl_t, upl_offset_t, off_t, int, off_t, int, int (*)(buf_t, void *), void *);
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1463709-cluster_pagein_ext)*