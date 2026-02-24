# verticalAlignment

**Framework**: USD

An option that controls the text’s vertical placement within its bounding rectangle.

#### Overview

The runtime handles each option of this property differently depending on whether the text displays with line breaks. For more information, see [`wrapMode`](wrapmode.md).

##### Declaration

```other
token verticalAlignment = "center" (
    allowedTokens = ["top", "middle", "lowerMiddle", "baseline", "bottom"]
)
```

##### Vertical Alignments for Single Line Text

For a single line of text, the vertical alignment is relative to font features.

- **`top`**: Aligns the line of text vertically with the ascender.
- **`middle`**: Aligns the line of text vertically with the center of capital letters.
- **`lowerMiddle`**: Aligns the line of text vertically with the center of lowercase letters.
- **`baseline`**: Aligns the line of text vertically with the baseline.
- **`bottom`**: Aligns the line of text vertically with a descender.

##### Vertical Alignments for Multiline Text

For multiline text, each line of text bases its vertical alignment on the text’s bounding box.

- **`top`**: Aligns each line of text vertically with the top.
- **`middle, lowerMiddle`**: Aligns each line of text in the center with equal space above and below the line of text.
- **`baseline, bottom`**: Aligns each line of text vertically with the bottom.

## See Also

- [content](content.md)
  The characters that the text displays.
- [font](font.md)
  An array of font names.
- [pointSize](pointsize.md)
  The size of the text’s font.
- [width](width.md)
  The width of the text’s bounding box.
- [height](height.md)
  The height of the text’s bounding box.
- [depth](depth.md)
  A value that defines the depth, in scene units, of the text’s extrusion.
- [wrapMode](wrapmode.md)
  An option that determines the flow of the text.
- [horizontalAlignment](horizontalalignment.md)
  An option that controls the text’s horizontal placement within its bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/verticalalignment)*