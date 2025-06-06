# UIScrollView.ContentInsetAdjustmentBehavior.automatic

**Framework**: UIKit  
**Kind**: case

Automatically adjust the scroll view insets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

#### Discussion

Content is always adjusted vertically when the scroll view is the content view of a view controller that is currently displayed by a navigation or tab bar controller. If the scroll view is horizontally scrollable, the horizontal content offset is also adjusted when there are nonzero safe area insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentinsetadjustmentbehavior-swift.enum/automatic)*