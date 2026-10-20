# pageCount

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The number of pages in the scanned document.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var pageCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger pageCount;
```

## See Also

### Reading the scanned document
- [var title: String](./title.md)
  The title of the scanned document.
- [func imageOfPage(at: Int) -> UIImage](./imageofpage%28at%29.md)
  Requests the image of a page at a specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcamerascan/pagecount)*