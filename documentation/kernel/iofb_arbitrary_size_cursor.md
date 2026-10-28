# IOFB_ARBITRARY_SIZE_CURSOR

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.6+

## Declaration

```c
#define IOFB_ARBITRARY_SIZE_CURSOR
```

## Discussion

When IOFB_ARBITRARY_SIZE_CURSOR is not defined, the maximum cursor size is assumed to be CURSORWIDTH x CURSORHEIGHT and this header file will define a number of structures for storing cursor images accordingly. A non-kernel task may define IOFB_ARBITRARY_SIZE_CURSOR and use cursors up to the size specified when IOFBCreateSharedCursor() was called. In this case appropriate structures for storing cursor images must be defined elsewhere. In the kernel, IOFB_ARBITRARY_SIZE_CURSOR is always defined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofb_arbitrary_size_cursor)*