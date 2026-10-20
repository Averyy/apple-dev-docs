# backtrace_user

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.12+

## Declaration

```c
unsigned int backtrace_user(uintptr_t *bt, unsigned int btlen, const struct backtrace_control *ctl, struct backtrace_user_info *info_out);
```

## See Also

### Backtrace
- [backtrace](./api-1644760-backtrace.md)
- [OSReportWithBacktrace](./api-1593374-osreportwithbacktrace.md)
- [OSBacktrace](./api-1593371-osbacktrace.md)
- [OSPrintBacktrace](./api-1593373-osprintbacktrace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/2202280-backtrace_user)*