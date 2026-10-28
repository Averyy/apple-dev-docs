# representedURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A URL of the file or resource represented in the window.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
var representedURL: URL? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSURL * representedURL;
```

## Discussion

The window shows a documentation icon in the title bar when this property isn’t `nil` and the URL has a non-empty path. If the URL represents a filename or other resource with a known icon, the window displays that icon as the document icon; otherwise, the window displays a default document icon.

When the windows displays a document icon, a pop-up menu is also available by Command-clicking the area containing the icon and title. The pop-up menu displays the path components of the URL.

If [`representedURL`](./representedurl.md) is `nil` or the URL path is empty, the document icon and pop-up menu aren’t available.

## See Also

### Configuring the title bar
- [var separatorStyle: UITitlebarSeparatorStyle](./separatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum UITitlebarSeparatorStyle](../uititlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var titleVisibility: UITitlebarTitleVisibility](./titlevisibility.md)
  A value that indicates the visibility of the title.
- [enum UITitlebarTitleVisibility](../uititlebartitlevisibility.md)
  States that determine visibility of the title in the title bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uititlebar/representedurl)*