# UISplitArrangement

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

An arrangement that places the primary and secondary views side by side along one or more axes.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct UISplitArrangement
```

#### Overview

A split arrangement view keeps its primary and secondary views in separate spaces: next to each other horizontally when someone is holding the device in landscape orientation, or stacked vertically when someone is holding the device in portrait orientation.. Here’s how the split arrangement positions the primary and secondary views:

- In landscape orientation, the arrangement view places the primary view in the leading position and the secondary view in the trailing position.
- In portrait orientation, the arrangement view places the primary view in the top position and the secondary view in the bottom position.
- When someone is holding a closed iPhone Duo in a horizontal orientation, the split arrangement only shows the primary view.

Create a split arrangement by specifying a primary and secondary view controller, and call the [`updateArrangement(_:animated:)`](./uiarrangementviewcontroller/updatearrangement%28_,animated%29.md) method with [`split`](./uiarrangementviewcontroller/arrangement/split.md):

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.split)
```

##### Adjust a split arrangement’s layout sizing

By default, a split arrangement controller sizes the primary and secondary views equally when a display has one region. Influence how the arrangement view computes the sizes for each view by setting the split arrangement’s properties for each placement to use an automatic size, a fixed layout size, a fractional layout size, or an intrinsic content size.

First create a `UISplitArrangement` instance and view properties instance to configure the preferred size:

```swift
var splitArrangement = UISplitArrangement.split
var primaryViewProperties = splitArrangement.defaultViewProperties
```

Next, create a [`UISplitArrangement.DimensionRange`](./uisplitarrangement-swift.struct/dimensionrange.md) instance, and configure the [`minimum`](./uisplitarrangement-swift.struct/dimensionrange/minimum.md), [`preferred`](./uisplitarrangement-swift.struct/dimensionrange/preferred.md), or [`maximum`](./uisplitarrangement-swift.struct/dimensionrange/maximum.md) properties with [`UISplitArrangement.Dimension`](./uisplitarrangement-swift.struct/dimension.md) options to describe how to size the view. The following example sets a preferred fractional layout size with an absolute minimum:

```swift
var primaryDimensionRange = UISplitArrangement.DimensionRange()
primaryDimensionRange.minimum = .absolute(250.0)
primaryDimensionRange.preferred = .fractional(0.3)
```

Then, set the `width` or `height` property on the view properties instance to the configured [`UISplitArrangement.DimensionRange`](./uisplitarrangement-swift.struct/dimensionrange.md), set the view properties on the split arrangement for the view’s placement , and update the arrangement view controller to use the split arrangement by calling the [`updateArrangement(_:animated:)`](./uiarrangementviewcontroller/updatearrangement%28_,animated%29.md) method:

```swift
 primaryViewProperties.width = primaryDimensionRange
 
 splitArrangement.setViewProperties(primaryViewProperties, for: .primary)
 updateArrangement(splitArrangement)
```

##### Limit a split arrangement by orientation

You can limit which axes your split arrangement view controller supports by specifying the axes for the arrangement. The following example shows an arrangement that only splits vertically:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.split.axes(.vertical))
```

Use [`axes(_:)`](./uisplitarrangement-swift.struct/axes%28_%29.md)  to set the axes for a split arrangement. For axes that you don’t include, the arrangement view only displays the primary view.

## Topics

### Creating a split arrangement
- [init()](./uisplitarrangement-swift.struct/init%28%29.md)
  Creates a split arrangement.
### Configuring the arrangement
- [func axes(UIAxis) -> UISplitArrangement](./uisplitarrangement-swift.struct/axes%28_%29.md)
  Sets the axes that the arrangement supports to the axes you provide.
- [UISplitArrangement.Dimension](./uisplitarrangement-swift.struct/dimension.md)
  A dimension for a view within a split arrangement.
- [UISplitArrangement.DimensionRange](./uisplitarrangement-swift.struct/dimensionrange.md)
  A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [UIArrangementViewController.Arrangement](./uiarrangementviewcontroller/arrangement.md)

## See Also

### Configuring the arrangement
- [struct UIOverlayArrangement](./uioverlayarrangement-swift.struct.md)
  An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [UIArrangementViewController.Arrangement](./uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [func updateArrangement<A>(A, animated: Bool)](./uiarrangementviewcontroller/updatearrangement%28_,animated%29.md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-swift.struct)*