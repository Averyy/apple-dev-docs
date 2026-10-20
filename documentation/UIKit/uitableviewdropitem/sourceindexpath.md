# sourceIndexPath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The index path of the item in the table view, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var sourceIndexPath: IndexPath? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSIndexPath * sourceIndexPath;
```

#### Discussion

If the item originated from the table view, this property contains the item’s original index path.

## See Also

### Getting the item information
- [var previewSize: CGSize](./previewsize.md)
  The size of the drag item’s preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropitem/sourceindexpath)*