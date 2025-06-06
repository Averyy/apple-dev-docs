# backtrace

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.12+

## Declaration

```swift
unsigned int backtrace(uintptr_t *bt, unsigned int btlen, struct backtrace_control *ctl, backtrace_info_t *info_out);
```

## See Also

- [backtrace_user](2202280-backtrace_user.md)
- [OSReportWithBacktrace](1593374-osreportwithbacktrace.md)
- [OSBacktrace](1593371-osbacktrace.md)
- [OSPrintBacktrace](1593373-osprintbacktrace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644760-backtrace)*