# contentImage

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The image to display for the item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var contentImage: WKImage? { get set }
```

```objc
@property (nonatomic, copy, nullable) WKImage * contentImage;
```

## Discussion

This image contains the item’s content and is displayed when the item is selected. The content image supported for all picker styles.

## See Also

### Setting the Picker Item’s Content
- [var title: String?](./title.md)
  The text to display for the item.
- [var accessoryImage: WKImage?](./accessoryimage.md)
  A small image to display next to the title string.
- [var caption: String?](./caption.md)
  A caption for the item’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage)*