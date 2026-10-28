# OS_SECURITY_CONFIG_TPRO

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

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
OS_SECURITY_CONFIG_TPRO
```

## Discussion

Supported security configurations that a process/task can have. This is a bitmask type, allowing multiple configurations to be active.

No security config flags set.

Indicates that the Hardened Heap configuration is enabled for the process/task. This implies security-critical settings for the system memory allocator.

Indicates that Trusted Path Read-Only (TPRO) is enabled for the process/task.

Indicates that Memory Tagging Extension (MTE) is enabled for the process/task.

Indicates Script Restrictions are enabled for the process/task.

Indicates that the Guard Objects configuration is enabled for the process/task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_security_config_t/os_security_config_tpro)*