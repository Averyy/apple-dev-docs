# title

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The text to display for the item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

## Discussion

This string contains the item’s content and is displayed when the item is selected. Titles are used for pickers configured to display a list. They are not shown for stack and image sequence styles.

## See Also

### Setting the Picker Item’s Content
- [var contentImage: WKImage?](./contentimage.md)
  The image to display for the item.
- [var accessoryImage: WKImage?](./accessoryimage.md)
  A small image to display next to the title string.
- [var caption: String?](./caption.md)
  A caption for the item’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem/title)*