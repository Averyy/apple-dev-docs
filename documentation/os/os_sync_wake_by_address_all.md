# os_sync_wake_by_address_all

**Framework**: os  
**Kind**: func  
**Role**: Function

An atomic operation that wakes all threads blocked on a futex wait, used to implement higher-level synchronization primitives.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```c
extern int os_sync_wake_by_address_all(void *addr, size_t size, os_sync_wake_by_address_flags_t flags);
```

#### Return Value

Returns 0 on success, and -1 on error with `errno` set.

#### Discussion

This function wakes all threads waiting on `addr`. There’s no guarantee on the order threads wake.

Pass consistent values across wait and wake APIs for `addr`, `size`, and `flags`. See [`os_sync_wake_by_address_flags_t`](./os_sync_wake_by_address_flags_t.md) for details.

> ❗ **Important**: Use this function only for implementing synchronization primitives that don’t have a sense of ownership, such as condition variables or semaphores. In particular, this function doesn’t provide priority inversion avoidance. For locking APIs, use existing OS primitives, such as `pthread` threads or [Unfair Locking](./synchronization.md#Unfair-Locking) APIs. For synchronization and threading managed by the OS, use a higher-level API, such as [Dispatch](../Dispatch/Dispatch.md).

##### Error Codes

When this function returns `-1`, the global variable `errno` contains one of these values, indicating the corresponding error.

| Error code | Description |
| --- | --- |
| `EINVAL` | Invalid flags or size.![](https://developer.apple.com/tutorials/images/com.apple.os/spacer.png)The `addr` passed is NULL.![](https://developer.apple.com/tutorials/images/com.apple.os/spacer.png)The operation associated with the existing kernel state at `addr` is inconsistent with other function arguments. |
| `ENOENT` | There are no compare-and-wait operations on `addr`. |
| `EDOM` | The `addr` is in use for non-compare-and-wait synchronization. |

## Parameters

- `addr`: The user-space address waited on to wake. This address must be aligned to `size`.
- `size`: The size of the wait value, in bytes. Values can be 4 or 8 bytes, where 4-byte values use the lower bytes of `value`.
- `flags`: Flags for the operation.

## See Also

### Futex Conditional Wait Primitives
- [os_sync_wait_on_address](./os_sync_wait_on_address.md)
  An atomic compare-and-wait operation, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_deadline](./os_sync_wait_on_address_with_deadline.md)
  An atomic compare-and-wait operation with a deadline, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_timeout](./os_sync_wait_on_address_with_timeout.md)
  An atomic compare-and-wait operation with a timeout, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_flags_t](./os_sync_wait_on_address_flags_t.md)
  Flags to control futex wait behavior.
- [os_sync_wake_by_address_any](./os_sync_wake_by_address_any.md)
  An atomic operation that wakes one thread blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_flags_t](./os_sync_wake_by_address_flags_t.md)
  Flags to control futex wake behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_sync_wake_by_address_all)*