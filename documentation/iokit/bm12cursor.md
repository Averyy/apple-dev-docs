# bm12Cursor

**Framework**: IOKit  
**Kind**: tag

Cursor image for 1-bit cursor.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
struct bm12Cursor {
    ...
};
```

#### Discussion

This structure stores 16 pixel x 16 pixel cursors to be used with 1-bit color depth. This structure is only defined if IOFB_ARBITRARY_SIZE_CURSOR is not defined.

## Topics

### Fields
- [image](./bm12cursor/api-1589178-image.md)
  This array contains the cursor images.
- [mask](./bm12cursor/api-1589177-mask.md)
  This array contains the cursor mask.
- [save](./bm12cursor/api-1589193-save.md)
  This array stores the pixel values of the region underneath the cursor in its last drawn position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/bm12cursor)*