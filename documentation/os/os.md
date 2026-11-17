# os

**Framework**: os  
**Kind**: module  
**Role**: Framework

Coordinate the scheduling and synchronization of your app’s tasks, and log information to the console to diagnose issues.

**Availability**:
- iOS 8.0+
- iPadOS
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Topics

### Logs
- [Logging](./logging.md)
  Capture telemetry from your app for debugging and performance analysis using the unified logging system.
### Task Management
- [Synchronization](./synchronization.md)
  Access low-level synchronization mechanisms to control state across threads.
- [Workgroups](./workgroups.md)
  Schedule one or more threads to run at regular intervals and before specific deadlines.
### Deprecated
- [Deprecated Symbols](./deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Reference
- [os Constants](./os-constants.md)
- [os Macros](./os-macros.md)
- [os Data Types](./os-data-types.md)
### Variables
- [var OS_LOG_STRING_SECTION: String](./os_log_string_section.md)
### Memory
- [os_proc_available_memory](./os_proc_available_memory.md)
  Determines the amount of memory available to the current app.
- [os_block_t](./os_block_t.md)
  A block that takes no arguments and returns no value.
- [os_function_t](./os_function_t.md)
  A pointer to a function.
- [os_release](./os_release-c.func.md)
- [os_retain](./os_retain-c.func.md)
### Structures
- [os_unfair_recursive_lock_s](./os_unfair_recursive_lock_s.md)
### Functions
- [os_lockdown_mode_enabled](./os_lockdown_mode_enabled.md)
- [os_security_config_get](./os_security_config_get.md)
- [os_security_config_get_for_proc](./os_security_config_get_for_proc.md)
- [os_security_config_get_for_task](./os_security_config_get_for_task.md)
- [os_unfair_recursive_lock_assert_not_owned_by_self](./os_unfair_recursive_lock_assert_not_owned_by_self.md)
- [os_unfair_recursive_lock_assert_owned_by_self](./os_unfair_recursive_lock_assert_owned_by_self.md)
- [os_unfair_recursive_lock_lock](./os_unfair_recursive_lock_lock.md)
- [os_unfair_recursive_lock_lock_with_flags](./os_unfair_recursive_lock_lock_with_flags.md)
- [os_unfair_recursive_lock_trylock](./os_unfair_recursive_lock_trylock.md)
- [os_unfair_recursive_lock_unlock](./os_unfair_recursive_lock_unlock.md)
### Macros
- [API_OBSOLETED](./api_obsoleted.md)
- [API_OBSOLETED_BEGIN](./api_obsoleted_begin.md)
- [API_OBSOLETED_END](./api_obsoleted_end.md)
- [API_OBSOLETED_WITH_REPLACEMENT](./api_obsoleted_with_replacement.md)
- [API_OBSOLETED_WITH_REPLACEMENT_BEGIN](./api_obsoleted_with_replacement_begin.md)
- [API_OBSOLETED_WITH_REPLACEMENT_END](./api_obsoleted_with_replacement_end.md)
- [LOG_SWIFT_NAME](./log_swift_name.md)
- [LOG_SWIFT_NEWTYPE](./log_swift_newtype.md)
- [OS_RECURSIVE_LOCK_API_VERSION](./os_recursive_lock_api_version.md)
- [OS_RECURSIVE_LOCK_SUPPORTS_AT_LEAST](./os_recursive_lock_supports_at_least.md)
- [OS_UNFAIR_RECURSIVE_LOCK_INIT](./os_unfair_recursive_lock_init.md)
- [OS_UNFAIR_RECURSIVE_LOCK_NO_BACKDEPLOY](./os_unfair_recursive_lock_no_backdeploy.md)
- [OS_WORKGROUP_ENUM_API_DEPRECATED_WITH_REPLACEMENT](./os_workgroup_enum_api_deprecated_with_replacement.md)
### Type Aliases
- [os_unfair_recursive_lock](./os_unfair_recursive_lock.md)
- [os_unfair_recursive_lock_t](./os_unfair_recursive_lock_t.md)
### Enumerations
- [os_security_config_t](./os_security_config_t.md)
- [os_unfair_recursive_lock_flags_t](./os_unfair_recursive_lock_flags_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os)*