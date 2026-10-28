# effectiveUserInterfaceLayoutDirection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The user interface layout direction appropriate for arranging the immediate content of the view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var effectiveUserInterfaceLayoutDirection: UIUserInterfaceLayoutDirection { get }
```

```objc
@property (nonatomic, readonly) UIUserInterfaceLayoutDirection effectiveUserInterfaceLayoutDirection;
```

## Discussion

When a view’s immediate content is being arranged or drawn, you should always consult the value of this property. In addition, note that you can’t assume that the value propagates through the view’s subtree.

## See Also

### Adjusting the user interface
- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](./overrideuserinterfacestyle.md)
  The user interface style adopted by the view and all of its subviews.
- [var semanticContentAttribute: UISemanticContentAttribute](./semanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection](./userinterfacelayoutdirection%28for%29.md)
  Returns the user interface direction for the given semantic content attribute.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute, relativeTo: UIUserInterfaceLayoutDirection) -> UIUserInterfaceLayoutDirection](./userinterfacelayoutdirection%28for,relativeto%29.md)
  Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/effectiveuserinterfacelayoutdirection)*