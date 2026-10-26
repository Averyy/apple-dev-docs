# os_security_config_get_for_proc

**Framework**: os  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
extern int os_security_config_get_for_proc(pid_t pid, os_security_config_t *config);
```

#### Return Value

Returns 0 on success, in which case `*config` is populated, or -1 on failure.

#### Discussion

Retrieves the security configuration bitmask for a target process, identified by its PID.

This function queries the kernel for the set of security properties active for the specified process.

## Parameters

- `pid`: The process identifier (pid_t) of the target process.
- `config`: A pointer to an os_security_config_t variable where the resulting security configuration will be stored if the function succeeds. This parameter must not be NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_security_config_get_for_proc)*