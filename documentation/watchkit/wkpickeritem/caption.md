# caption

**Framework**: WatchKit  
**Kind**: property

A caption for the item’s content.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var caption: String? { get set }
```

#### Discussion

When the picker’s focus style includes a caption, the picker gets the text for that caption from this property. Captions are a way to identify the meaning of the item’s content. You can also assign the same caption to all of the items in a picker to identify the purpose of the picker itself.

## See Also

- [var contentImage: WKImage?](contentimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage))
  The image to display for the item.
- [var title: String?](title.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/title))
  The text to display for the item.
- [var accessoryImage: WKImage?](accessoryimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/accessoryimage))
  A small image to display next to the title string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem/caption)*