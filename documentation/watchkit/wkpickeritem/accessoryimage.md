# accessoryImage

**Framework**: Watchkit  
**Kind**: property

A small image to display next to the title string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@NSCopying var accessoryImage: WKImage? { get set }
```

## Overview

The dimensions of an accessory image are 13 points wide by 13 points high. Larger images are scaled and centered to fit the available space. Smaller images are centered but not scaled.

## See Also

- [var contentImage: WKImage?](contentimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/contentimage))
- [var title: String?](title.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/title))
- [var caption: String?](caption.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem/caption))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpickeritem/accessoryimage)*