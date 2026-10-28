# image

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

This array defines the cursor color values and transparency. The array is two dimensional and its first index is the cursor frame and the second index is the cursor pixel. A value of 0 means the pixel is transparent. 

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
unsigned short image[4][256];
```

## Discussion

Non-zero values are stored with the red, green, blue, and alpha values encoded with the following masks:

| red mask | 0xF000 |
| --- | --- |
| blue mask | 0x0F00 |
| green mask | 0x00F0 |
| alpha mask | 0x000F |

Note that only 4 bits are allocated for each color component.

## See Also

### Fields
- [save](./api-1589144-save.md)
  This array stores the color values of the region underneath the cursor in its last drawn position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/bm34cursor/1589181-image)*