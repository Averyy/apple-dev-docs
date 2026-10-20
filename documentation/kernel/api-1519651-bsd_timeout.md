# bsd_timeout

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```c
void bsd_timeout(void (*)(void *), void *arg, struct timespec *ts);
```

## See Also

### General
- [bsd_untimeout](./api-1519608-bsd_untimeout.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1519651-bsd_timeout)*