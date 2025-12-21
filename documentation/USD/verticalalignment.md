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

##### Vertical Alignments for Multiline Text

For multiline text, each line of text bases its vertical alignment on the text’s bounding box.

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