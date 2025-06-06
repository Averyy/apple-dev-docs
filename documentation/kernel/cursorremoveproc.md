# CursorRemoveProc

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef void (*CursorRemoveProc)(IOFramebuffer *inst, void *shmem, volatile unsigned char *vramPtr, unsigned int vramRow, int width, int height);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/cursorremoveproc)*