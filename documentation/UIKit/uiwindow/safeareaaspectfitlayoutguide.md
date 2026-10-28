# safeAreaAspectFitLayoutGuide

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A layout guide for placing content of a particular aspect ratio.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var safeAreaAspectFitLayoutGuide: any UILayoutGuide & UILayoutGuideAspectFitting { get }
```

```objc
@property (nonatomic, strong, readonly) UILayoutGuide<UILayoutGuideAspectFitting> * safeAreaAspectFitLayoutGuide;
```

## Discussion

This layout guide provides a centered region in the window where you can place media content of a particular aspect ratio (width over height) to avoid obscuring the content.

> ❗ **Important**:  Use this layout guide for full-screen content. Avoid adding constraints to the guide through deeply nested view hierarchies.

## See Also

### Working with layout guides
- [protocol UILayoutGuideAspectFitting](../uilayoutguideaspectfitting.md)
  The interface for a layout guide that supports a particular aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/safeareaaspectfitlayoutguide)*