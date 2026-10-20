# lck_rw_alloc_init

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
lck_rw_t * lck_rw_alloc_init(lck_grp_t *grp, lck_attr_t *attr);
```

## See Also

### locks
- [lck_attr_alloc_init](./api-1575529-lck_attr_alloc_init.md)
- [lck_attr_cleardebug](./api-1575538-lck_attr_cleardebug.md)
- [lck_attr_free](./api-1575499-lck_attr_free.md)
- [lck_attr_setdebug](./api-1575551-lck_attr_setdebug.md)
- [lck_attr_setdefault](./api-1575541-lck_attr_setdefault.md)
- [lck_grp_alloc_init](./api-1575515-lck_grp_alloc_init.md)
- [lck_grp_attr_alloc_init](./api-1575518-lck_grp_attr_alloc_init.md)
- [lck_grp_attr_free](./api-1575492-lck_grp_attr_free.md)
- [lck_grp_attr_setdefault](./api-1575540-lck_grp_attr_setdefault.md)
- [lck_grp_attr_setstat](./api-1575490-lck_grp_attr_setstat.md)
- [lck_grp_free](./api-1575524-lck_grp_free.md)
- [lck_mtx_alloc_init](./api-1575516-lck_mtx_alloc_init.md)
- [lck_mtx_assert](./api-1575514-lck_mtx_assert.md)
- [lck_mtx_destroy](./api-1575534-lck_mtx_destroy.md)
- [lck_mtx_free](./api-1575493-lck_mtx_free.md)
- [lck_mtx_init](./api-1575548-lck_mtx_init.md)
- [lck_mtx_lock](./api-1575544-lck_mtx_lock.md)
- [lck_mtx_sleep](./api-1575546-lck_mtx_sleep.md)
- [lck_mtx_sleep_deadline](./api-1575501-lck_mtx_sleep_deadline.md)
- [lck_mtx_unlock](./api-1575506-lck_mtx_unlock.md)
- [lck_rw_destroy](./api-1575502-lck_rw_destroy.md)
- [lck_rw_free](./api-1575547-lck_rw_free.md)
- [lck_rw_init](./api-1575530-lck_rw_init.md)
- [lck_rw_lock](./api-1575537-lck_rw_lock.md)
- [lck_rw_lock_exclusive](./api-1575510-lck_rw_lock_exclusive.md)
- [lck_rw_lock_exclusive_to_shared](./api-1575536-lck_rw_lock_exclusive_to_shared.md)
- [lck_rw_lock_shared](./api-1575517-lck_rw_lock_shared.md)
- [lck_rw_lock_shared_to_exclusive](./api-1575507-lck_rw_lock_shared_to_exclusive.md)
- [lck_rw_sleep](./api-1575504-lck_rw_sleep.md)
- [lck_rw_sleep_deadline](./api-1575512-lck_rw_sleep_deadline.md)
- [lck_rw_try_lock](./api-1575528-lck_rw_try_lock.md)
- [lck_rw_unlock](./api-1575549-lck_rw_unlock.md)
- [lck_rw_unlock_exclusive](./api-1575542-lck_rw_unlock_exclusive.md)
- [lck_rw_unlock_shared](./api-1575496-lck_rw_unlock_shared.md)
- [lck_spin_alloc_init](./api-1575508-lck_spin_alloc_init.md)
- [lck_spin_destroy](./api-1575489-lck_spin_destroy.md)
- [lck_spin_free](./api-1575491-lck_spin_free.md)
- [lck_spin_init](./api-1575543-lck_spin_init.md)
- [lck_spin_lock](./api-1575532-lck_spin_lock.md)
- [lck_spin_lock_grp](./api-3112641-lck_spin_lock_grp.md)
- [lck_spin_sleep](./api-1575509-lck_spin_sleep.md)
- [lck_spin_sleep_deadline](./api-1575526-lck_spin_sleep_deadline.md)
- [lck_spin_sleep_grp](./api-3112642-lck_spin_sleep_grp.md)
- [lck_spin_unlock](./api-1575523-lck_spin_unlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575521-lck_rw_alloc_init)*