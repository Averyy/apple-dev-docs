# Debugging

**Framework**: Kernel

Debug your kernel extensions using the kernel debugger, assertions, exceptions, backtraces, and logging.

## Topics

### Kernel Debugging
- [Debugger](1575299-debugger.md)
  Enter the kernel debugger.
- [kdbg_get_cpu](3197813-kdbg_get_cpu.md)
- [kdbg_get_timestamp](3197814-kdbg_get_timestamp.md)
- [kdbg_set_cpu](3197815-kdbg_set_cpu.md)
- [kdbg_set_timestamp](3197816-kdbg_set_timestamp.md)
- [kdbg_set_timestamp_and_cpu](3197817-kdbg_set_timestamp_and_cpu.md)
- [kdebug_commpage_state](3242840-kdebug_commpage_state.md)
- [kdebug_debugid_enabled](3242841-kdebug_debugid_enabled.md)
- [kdebug_debugid_explicitly_enabled](3242842-kdebug_debugid_explicitly_enable.md)
- [kdebug_using_continuous_time](3242843-kdebug_using_continuous_time.md)
- [kernel_debug](1568810-kernel_debug.md)
- [kernel_debug1](1568762-kernel_debug1.md)
- [kernel_debug_enter](3242844-kernel_debug_enter.md)
- [kernel_debug_filtered](2123006-kernel_debug_filtered.md)
- [kernel_debug_flags](2977320-kernel_debug_flags.md)
- [kernel_debug_register_callback](3242845-kernel_debug_register_callback.md)
### kdp
- [kdp_register_callout](1526280-kdp_register_callout.md)
- [kdp_register_send_receive](1399355-kdp_register_send_receive.md)
- [kdp_unregister_send_receive](1399359-kdp_unregister_send_receive.md)
### Assertions
- [Assert](1574809-assert.md)
- [assert_wait](1524384-assert_wait.md)
- [assert_wait_deadline](1524378-assert_wait_deadline.md)
- [assert_wait_deadline_with_leeway](1524380-assert_wait_deadline_with_leeway.md)
- [assert_wait_timeout](1524367-assert_wait_timeout.md)
- [assert_wait_timeout_with_leeway](1524381-assert_wait_timeout_with_leeway.md)
### Backtrace
- [backtrace](1644760-backtrace.md)
- [backtrace_user](2202280-backtrace_user.md)
- [OSReportWithBacktrace](1593374-osreportwithbacktrace.md)
- [OSBacktrace](1593371-osbacktrace.md)
- [OSPrintBacktrace](1593373-osprintbacktrace.md)
### Exceptions
- [catch_exception_raise](1537287-catch_exception_raise.md)
- [catch_exception_raise_state](1537255-catch_exception_raise_state.md)
- [catch_exception_raise_state_identity](1537251-catch_exception_raise_state_iden.md)
- [catch_mach_exception_raise](1559883-catch_mach_exception_raise.md)
- [catch_mach_exception_raise_state](1559877-catch_mach_exception_raise_state.md)
- [catch_mach_exception_raise_state_identity](1559863-catch_mach_exception_raise_state.md)
### Logging
- [OS_os_log](os_os_log.md)
- [IOLog](1575337-iolog.md)
  Log a message to console in text mode, and /var/log/system.log.
- [IOLogv](1575323-iologv.md)
  Log a message to console in text mode, and /var/log/system.log.
- [os_log_create](1643798-os_log_create.md)
  Creates a custom log object, to be passed to logging functions for sending messages to the logging system.
- [os_log_debug_enabled](1643808-os_log_debug_enabled.md)
  Returns a Boolean value indicating whether debug-level logging is enabled for a specified log object.
- [os_log_info_enabled](1643817-os_log_info_enabled.md)
  Returns a Boolean value indicating whether info-level logging is enabled for a specified log object.
### Helpers
- [OSPrintMemory](1543117-osprintmemory.md)
- [IOFindNameForValue](1575325-iofindnameforvalue.md)
- [IOFindValueForName](1575321-iofindvalueforname.md)

## See Also

- [AppleDSP](appledsp.md)
  Perform digital signal processing on data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/debugging)*