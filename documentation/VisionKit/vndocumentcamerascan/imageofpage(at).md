# imageOfPage(at:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Requests the image of a page at a specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func imageOfPage(at index: Int) -> UIImage
```

```objc
- (UIImage *) imageOfPageAtIndex:(NSUInteger) index;
```

#### Return Value

The image of the page at the specified index. If `index` is out of bounds, the framework throws an exception.

## Parameters

- `index`: The index of the image in the scanned document you’d like to return. Page 1 is at index 0.

## See Also

### Reading the scanned document
- [var title: String](./title.md)
  The title of the scanned document.
- [var pageCount: Int](./pagecount.md)
  The number of pages in the scanned document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcamerascan/imageofpage(at:))*