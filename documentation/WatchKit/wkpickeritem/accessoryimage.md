# accessoryImage

**Framework**: WatchKit  
**Kind**: property

A small image to display next to the title string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var accessoryImage: WKImage? { get set }
```

#### Discussion

The dimensions of an accessory image are 13 points wide by 13 points high. Larger images are scaled and centered to fit the available space. Smaller images are centered but not scaled.

## See Also

- [var contentImage: WKImage?](wkpickeritem/contentimage.md)
  The image to display for the item.
- [var title: String?](wkpickeritem/title.md)
  The text to display for the item.
- [var caption: String?](wkpickeritem/caption.md)
  A caption for the item’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem/accessoryimage)*