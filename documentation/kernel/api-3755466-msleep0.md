# msleep0

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
int msleep0(void *chan, lck_mtx_t *mtx, int pri, const char *wmesg, int timo, int (*continuation)(int));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3755466-msleep0)*