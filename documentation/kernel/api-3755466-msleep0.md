# msleep0

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 12.0+

## Declaration

```c
int msleep0(void *chan, lck_mtx_t *mtx, int pri, const char *wmesg, int timo, int (*continuation)(int));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3755466-msleep0)*