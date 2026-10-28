# os_sync_wait_on_address_with_timeout

**Framework**: os  
**Kind**: func  
**Role**: Function

An atomic compare-and-wait operation with a timeout, used to implement higher-level synchronization primitives.

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
extern int os_sync_wait_on_address_with_timeout(void *addr, uint64_t value, size_t size, os_sync_wait_on_address_flags_t flags, os_clockid_t clockid, uint64_t timeout_ns);
```

## Return Value

If the calling thread is woken up by a call to [`os_sync_wake_by_address_all`](./os_sync_wake_by_address_all.md) or [`os_sync_wake_by_address_any`](./os_sync_wake_by_address_any.md), or the value at `addr` is different than expected, this function returns successfully and the return value indicates the number of outstanding waiters blocked on this address.

In the event of an error or a timeout, the function returns `-1` with `errno` set.

## Discussion

This function reads a value from `addr`, compares it to the expected `value`, and blocks the current thread for up to `timeout_ns` nanoseconds if the two are equal. This sequence of operations is atomic with respect to other concurrent operations performed on `addr` with [Futex Conditional Wait Primitives](./synchronization.md#Futex-Conditional-Wait-Primitives).

Pass consistent values across wait and wake APIs for `addr`, `size`, and `flags`. See [`os_sync_wait_on_address_flags_t`](./os_sync_wait_on_address_flags_t.md) for details.

> ❗ **Important**: Use this function only for implementing synchronization primitives that don’t have a sense of ownership, such as condition variables or semaphores. In particular, this function doesn’t provide priority inversion avoidance. For locking APIs, use existing OS primitives, such as `pthread` threads or [Unfair Locking](./synchronization.md#Unfair-Locking) APIs. For synchronization and threading managed by the OS, use a higher-level API, such as [Dispatch](../Dispatch/Dispatch.md).

### Error Codes

When this function returns `-1`, the global variable `errno` contains either an error code from [`os_sync_wait_on_address`](./os_sync_wait_on_address.md) or one of the following errors.

| Error code | Description |
| --- | --- |
| `EINVAL` | The function call used an invalid `clockid`.![](https://developer.apple.com/tutorials/images/com.apple.os/spacer.png)The function call used a timeout of `0`. |
| `ETIMEDOUT` | The calling thead wasn’t unblocked within `timeout_ns` nanoseconds. |

## Parameters

- `addr`: The user-space address to be used for atomic compare-and-wait. This address must be aligned to `size`.
- `value`: The value expected at `addr`.
- `size`: The size of `value`, in bytes. Values can be 4 or 8 bytes, where 4-byte values use the lower bytes of `value`.
- `flags`: Flags for the operation.
- `clockid`: Reserved for future expansion. Use [`OS_CLOCK_MACH_ABSOLUTE_TIME`](./os_clockid_t/os_clock_mach_absolute_time.md).
- `timeout_ns`: The timeout, in nanoseconds, at which the wait unblocks.

## See Also

### Futex Conditional Wait Primitives
- [os_sync_wait_on_address](./os_sync_wait_on_address.md)
  An atomic compare-and-wait operation, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_deadline](./os_sync_wait_on_address_with_deadline.md)
  An atomic compare-and-wait operation with a deadline, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_flags_t](./os_sync_wait_on_address_flags_t.md)
  Flags to control futex wait behavior.
- [os_sync_wake_by_address_all](./os_sync_wake_by_address_all.md)
  An atomic operation that wakes all threads blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_any](./os_sync_wake_by_address_any.md)
  An atomic operation that wakes one thread blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_flags_t](./os_sync_wake_by_address_flags_t.md)
  Flags to control futex wake behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_sync_wait_on_address_with_timeout)*