# wrapMode

**Framework**: USD

An option that determines the flow of the text.

#### Overview

The default value is `flowing`.

##### Wrap Modes

- **`singleLine`**: Displays text in a single line.
- **`hardBreaks`**: Breaks the text only at the text string’s line breaks.
- **`flowing`**: Breaks the text as needed to fit within the bounding box.

##### Declaration

```other
token wrapMode = "flowing" (
    allowedTokens = ["singleLine", "hardBreaks", "flowing"]
)
```

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
- [horizontalAlignment](horizontalalignment.md)
  An option that controls the text’s horizontal placement within its bounding box.
- [verticalAlignment](verticalalignment.md)
  An option that controls the text’s vertical placement within its bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/wrapmode)*