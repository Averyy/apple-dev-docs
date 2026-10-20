# backtrace

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.12+

## Declaration

```c
unsigned int backtrace(uintptr_t *bt, unsigned int btlen, struct backtrace_control *ctl, backtrace_info_t *info_out);
```

## See Also

### Backtrace
- [backtrace_user](./api-2202280-backtrace_user.md)
- [OSReportWithBacktrace](./api-1593374-osreportwithbacktrace.md)
- [OSBacktrace](./api-1593371-osbacktrace.md)
- [OSPrintBacktrace](./api-1593373-osprintbacktrace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1644760-backtrace)*