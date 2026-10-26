# os_security_config_get

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
extern os_security_config_t os_security_config_get();
```

#### Return Value

An os_security_config_t value representing the active security flags. This function is not expected to fail for the current process.

#### Discussion

Retrieves the security configuration bitmask for the current process.

This function inspects the value passed by the kernel to the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_security_config_get)*