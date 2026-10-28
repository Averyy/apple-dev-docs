# configuration

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A change that invalidates a view’s configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS
- Swift 5.1+

## Declaration

```swift
static var configuration: UIView.Invalidations.Configuration { get }
```

Available when `Self` is `UIView.Invalidations.Configuration`.

## Discussion

Use this invalidation type to call [`setNeedsUpdateConfiguration()`](../uibutton/setneedsupdateconfiguration%28%29.md) when a change in property value should cause the containing view to update the configuration.

> **Note**:  You only use this invalidation type on [`UIView`](../uiview.md) subclasses that support a configuration pattern, using [`setNeedsUpdateConfiguration()`](../uibutton/setneedsupdateconfiguration%28%29.md) and [`updateConfiguration()`](../uibutton/updateconfiguration%28%29.md) pattern. For example, use this type on [`UIButton`](../uibutton.md), [`UICollectionViewCell`](../uicollectionviewcell.md), [`UITableViewCell`](../uitableviewcell.md), or [`UITableViewHeaderFooterView`](../uitableviewheaderfooterview.md). This type has no effect on [`UIView`](../uiview.md) subclasses that don’t use a configuration pattern.

## See Also

### Specifying invalidation types
- [static var constraints: UIView.Invalidations.Constraints](./constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: UIView.Invalidations.Display](./display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: UIView.Invalidations.IntrinsicContentSize](./intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: UIView.Invalidations.Layout](./layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewinvalidating/configuration)*