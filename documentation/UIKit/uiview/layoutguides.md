# layoutGuides

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The array of layout guide objects owned by this view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var layoutGuides: [UILayoutGuide] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof UILayoutGuide *> * layoutGuides;
```

## See Also

### Working with layout guides
- [func addLayoutGuide(UILayoutGuide)](./addlayoutguide%28_%29.md)
  Adds the specified layout guide to the view.
- [var layoutMarginsGuide: UILayoutGuide](./layoutmarginsguide.md)
  A layout guide representing the view’s margins.
- [var readableContentGuide: UILayoutGuide](./readablecontentguide.md)
  A layout guide representing an area with a readable width within the view.
- [func removeLayoutGuide(UILayoutGuide)](./removelayoutguide%28_%29.md)
  Removes the specified layout guide from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutguides)*