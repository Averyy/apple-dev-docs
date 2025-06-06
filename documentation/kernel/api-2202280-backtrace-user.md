# backtrace_user

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.12+

## Declaration

```swift
unsigned int backtrace_user(uintptr_t *bt, unsigned int btlen, const struct backtrace_control *ctl, struct backtrace_user_info *info_out);
```

## See Also

- [backtrace](1644760-backtrace.md)
- [OSReportWithBacktrace](1593374-osreportwithbacktrace.md)
- [OSBacktrace](1593371-osbacktrace.md)
- [OSPrintBacktrace](1593373-osprintbacktrace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/2202280-backtrace_user)*