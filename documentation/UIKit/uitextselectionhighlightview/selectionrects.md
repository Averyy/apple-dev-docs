# selectionRects

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The rectangles to draw with the selection highlight.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var selectionRects: [UITextSelectionRect] { get set }
```

```objc
@property (nonatomic, strong) NSArray<UITextSelectionRect *> * selectionRects;
```

## Discussion

Use this property to get the rectangles to draw in a custom highlight view. The rectangles are in the coordinate space of the view that adopts this protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionhighlightview/selectionrects)*