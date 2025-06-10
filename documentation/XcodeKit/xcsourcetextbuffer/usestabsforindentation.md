# usesTabsForIndentation

**Framework**: XcodeKit  
**Kind**: property

A Boolean value that indicates whether tabs are used for indentation.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var usesTabsForIndentation: Bool { get }
```

#### Discussion

The `usesTabsForIndentation` property determines whether tab characters are used to indent text instead of space characters when possible. When the indentation width isn’t a multiple of the tab width, space characters are used to pad the indentation to the appropriate width.

For example, consider an `XCSourceTextBuffer` instance that has a tab width of eight, an indentation width of four, and the `usesTabsForIndentation` property set to `true`. The first indentation level is represented by four space characters, the second by a tab character, the third by a tab followed by four space characters, the fourth by two tab characters, and so on.

![A diagram showing four lines of source code, with each line indented once more than the last.](https://docs-assets.developer.apple.com/published/7e231364d72effa78c6e7cff391335c2/media-2902679%402x.png)

## See Also

- [var indentationWidth: Int](xcsourcetextbuffer/indentationwidth.md)
  The number of space characters used for indentation of the text in the buffer.
- [var tabWidth: Int](xcsourcetextbuffer/tabwidth.md)
  The number of space characters represented by a tab character in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextbuffer/usestabsforindentation)*