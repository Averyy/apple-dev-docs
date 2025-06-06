# CursorBlitProc

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef void (*CursorBlitProc)(IOFramebuffer *inst, void *shmem, volatile unsigned char *vramPtr, unsigned int cursStart, unsigned int vramRow, unsigned int cursRow, int width, int height);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/cursorblitproc)*