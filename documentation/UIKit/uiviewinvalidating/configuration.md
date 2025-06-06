# configuration

**Framework**: UIKit  
**Kind**: property

A change that invalidates a view’s configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
static var configuration: UIView.Invalidations.Configuration { get }
```

#### Discussion

Use this invalidation type to call [`setNeedsUpdateConfiguration()`](uibutton/setneedsupdateconfiguration().md) when a change in property value should cause the containing view to update the configuration.

> **Note**:  You only use this invalidation type on [`UIView`](uiview.md) subclasses that support a configuration pattern, using [`setNeedsUpdateConfiguration()`](uibutton/setneedsupdateconfiguration().md) and [`updateConfiguration()`](uibutton/updateconfiguration().md) pattern. For example, use this type on [`UIButton`](uibutton.md), [`UICollectionViewCell`](uicollectionviewcell.md), [`UITableViewCell`](uitableviewcell.md), or [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md). This type has no effect on [`UIView`](uiview.md) subclasses that don’t use a configuration pattern.

 You only use this invalidation type on [`UIView`](uiview.md) subclasses that support a configuration pattern, using [`setNeedsUpdateConfiguration()`](uibutton/setneedsupdateconfiguration().md) and [`updateConfiguration()`](uibutton/updateconfiguration().md) pattern. For example, use this type on [`UIButton`](uibutton.md), [`UICollectionViewCell`](uicollectionviewcell.md), [`UITableViewCell`](uitableviewcell.md), or [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md). This type has no effect on [`UIView`](uiview.md) subclasses that don’t use a configuration pattern.

## See Also

- [static var constraints: UIView.Invalidations.Constraints](uiviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: UIView.Invalidations.Display](uiviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize](uiviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: UIView.Invalidations.Layout](uiviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/configuration)*