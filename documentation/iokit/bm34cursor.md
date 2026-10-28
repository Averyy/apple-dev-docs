# bm34Cursor

**Framework**: IOKit  
**Kind**: tag

Cursor image for 15-bit cursor.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
struct bm34Cursor {
    ...
};
```

## Discussion

This structure stores 16 pixel x 16 pixel cursors to be used with 15-bit color depth. This structure is only defined if IOFB_ARBITRARY_SIZE_CURSOR is not defined.

## Topics

### Fields
- [image](./bm34cursor/api-1589181-image.md)
  This array defines the cursor color values and transparency. The array is two dimensional and its first index is the cursor frame and the second index is the cursor pixel. A value of 0 means the pixel is transparent. 
- [save](./bm34cursor/api-1589144-save.md)
  This array stores the color values of the region underneath the cursor in its last drawn position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/bm34cursor)*