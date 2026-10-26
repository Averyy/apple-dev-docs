# os_security_config_t

**Framework**: os  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef enum { ... } os_security_config_t;
```

#### Overview

Supported security configurations that a process/task can have. This is a bitmask type, allowing multiple configurations to be active.

No security config flags set.

Indicates that the Hardened Heap configuration is enabled for the process/task. This implies security-critical settings for the system memory allocator.

Indicates that Trusted Path Read-Only (TPRO) is enabled for the process/task.

Indicates that Memory Tagging Extension (MTE) is enabled for the process/task.

Indicates Script Restrictions are enabled for the process/task.

Indicates that the Guard Objects configuration is enabled for the process/task.

## Topics

### Enumeration Cases
- [OS_SECURITY_CONFIG_GUARD_OBJECTS](./os_security_config_t/os_security_config_guard_objects.md)
- [OS_SECURITY_CONFIG_HARDENED_HEAP](./os_security_config_t/os_security_config_hardened_heap.md)
- [OS_SECURITY_CONFIG_MTE](./os_security_config_t/os_security_config_mte.md)
- [OS_SECURITY_CONFIG_NONE](./os_security_config_t/os_security_config_none.md)
- [OS_SECURITY_CONFIG_SCRIPT_RESTRICTIONS](./os_security_config_t/os_security_config_script_restrictions.md)
- [OS_SECURITY_CONFIG_TPRO](./os_security_config_t/os_security_config_tpro.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_security_config_t)*