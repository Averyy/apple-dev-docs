# OS_SYNC_WAIT_ON_ADDRESS_SHARED

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

Flag to indicate an address is in a shared memory region, allowing for a futex wake from another process.

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
OS_SYNC_WAIT_ON_ADDRESS_SHARED
```

#### Discussion

Use this flag when you pass an address allocated in shared memory to any futex wait function. Shared memory can be used for waits and wakes within a single process, but incur a performance hit.

> ❗ **Important**: When using this flag with a futex wait, use the [`OS_SYNC_WAKE_BY_ADDRESS_SHARED`](../os_sync_wake_by_address_flags_t/os_sync_wake_by_address_shared.md) flag for any futex wake on the address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_sync_wait_on_address_flags_t/os_sync_wait_on_address_shared)*