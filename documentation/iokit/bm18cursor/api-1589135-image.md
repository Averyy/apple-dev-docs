# image

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

This array contains cursor color values, which are converted to displayed colors through the color table. The array is two dimensional and its first index is the cursor frame and the second index is the cursor pixel.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
unsigned char image[4][256];
```

## See Also

### Fields
- [mask](./api-1589194-mask.md)
  This array contains the cursor alpha mask. The array is two dimensional with the same indexing as the image. If an alpha mask pixel is 0 and the corresponding image pixel is set to white for the display, then this cursor pixel will invert pixels on the display.
- [save](./api-1589138-save.md)
  This array stores the color values of the region underneath the cursor in its last drawn position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/bm18cursor/1589135-image)*