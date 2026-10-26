# OS_SYNC_WAIT_ON_ADDRESS_NONE

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

Default behavior for futex functions that block a thread.

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
OS_SYNC_WAIT_ON_ADDRESS_NONE
```

#### Discussion

Use this flag when you pass an address only accessed in the calling process’s memory space. This flag enables kernel optimizations that can’t be used on shared memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_sync_wait_on_address_flags_t/os_sync_wait_on_address_none)*