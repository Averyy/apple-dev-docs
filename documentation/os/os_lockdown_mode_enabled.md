# os_lockdown_mode_enabled

**Framework**: os  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```c
extern bool os_lockdown_mode_enabled();
```

#### Return Value

True if Lockdown Mode is enabled; false if Lockdown Mode is disabled or not supported on the platform.

#### Discussion

Returns a cached value indicating whether Lockdown Mode is currently enabled on the system.

On platforms that support Lockdown Mode, the calling process must have the com.apple.developer.lockdown-mode.state entitlement. Without it, this function aborts the process.

This function will abort the process if an unexpected error occurs while querying the Lockdown Mode state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_lockdown_mode_enabled)*