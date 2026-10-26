# UISplitArrangement

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An arrangement that places the primary and secondary views side by side along one or more axes.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@interface UISplitArrangement : UIArrangement
```

#### Overview

A split arrangement view keeps its primary and secondary views in separate spaces: next to each other horizontally when someone is holding the device in landscape orientation, or stacked vertically when someone is holding the device in portrait orientation. Here’s how the split arrangement positions the primary and secondary views:

- In landscape orientation, the arrangement view places the primary view in the leading position and the secondary view in the trailing position.
- In portrait orientation, the arrangement view places the primary view in the top position and the secondary view in the bottom position.
- When someone is holding a closed iPhone Duo in a horizontal orientation, the split arrangement only shows the primary view.

Create a split arrangement by specifying a primary and secondary view controller, and call the [`updateArrangement:`](./uiarrangementviewcontroller/updatearrangement_.md) method with [`splitArrangement`](./uisplitarrangement-c.class/splitarrangement.md):

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UISplitArrangement *arrangement = [UISplitArrangement splitArrangement];
[self.arrangementVC updateArrangement:arrangement];
```

##### Adjust a split arrangement’s layout sizing

By default, a split arrangement view controller sizes the primary and secondary views equally when a display has one region. Influence how the arrangement view computes the sizes for each view by setting the split arrangement’s view properties for each placement to use an automatic size, a fixed layout size, a fractional layout size, or an intrinsic content size.

First create a [`UISplitArrangement`](./uisplitarrangement-c.class.md) instance and a [`UISplitArrangementViewProperties`](./uisplitarrangementviewproperties.md) instance to configure the preferred size:

```objc
UISplitArrangement *splitArrangement = [UISplitArrangement splitArrangement];
UISplitArrangementViewProperties *primaryViewProperties = [splitArrangement.defaultViewProperties copy];
```

Next, create a [`UISplitArrangementDimensionRange`](./uisplitarrangementdimensionrange.md) instance, and configure the [`minimum`](./uisplitarrangementdimensionrange/minimum.md), [`preferred`](./uisplitarrangementdimensionrange/preferred.md), or [`maximum`](./uisplitarrangementdimensionrange/maximum.md) properties with [`UISplitArrangementDimension`](./uisplitarrangementdimension.md) options to describe how to size the view. The following example sets a preferred fractional layout size with an absolute minimum:

```objc
UISplitArrangementDimensionRange *primaryDimensionRange = [[UISplitArrangementDimensionRange alloc] init];
primaryDimensionRange.minimum = [UISplitArrangementDimension absoluteDimension:250.0];
primaryDimensionRange.preferred = [UISplitArrangementDimension fractionalDimension:0.3];
```

Then, set the `width` or `height` property on the view properties instance to the configured [`UISplitArrangementDimensionRange`](./uisplitarrangementdimensionrange.md), set the view properties on the split arrangement for the view’s placement, and update the arrangement view controller to use the split arrangement by calling the [`updateArrangement:animated:`](./uiarrangementviewcontroller/updatearrangement_animated_.md) method:

```objc
primaryViewProperties.width = primaryDimensionRange;

[splitArrangement setViewProperties:primaryViewProperties forPlacement:UIArrangementViewControllerViewPlacementPrimary];
[arrangementVC updateArrangement:splitArrangement];
```

##### Limit a split arrangement by orientation

You can limit which axes your split arrangement view controller supports by specifying the axes for the arrangement. The following example shows an arrangement that only splits vertically:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UISplitArrangement *arrangement = [UISplitArrangement splitArrangement];
arrangement.axes = UIAxisVertical;
[self.arrangementVC updateArrangement:arrangement];
```

Use [`axes`](./uisplitarrangement-c.class/axes.md) to set the axes for a split arrangement. For axes that you don’t include, the arrangement view only displays the primary view.

## Topics

### Creating a split arrangement
- [+ splitArrangement](./uisplitarrangement-c.class/splitarrangement.md)
  Returns a split arrangement.
### Configuring the arrangement
- [axes](./uisplitarrangement-c.class/axes.md)
  The axes of the arrangement.
- [defaultViewProperties](./uisplitarrangement-c.class/defaultviewproperties.md)
  Returns the default properties for a view in the split arrangement.
- [- setViewProperties:forPlacement:](./uisplitarrangement-c.class/setviewproperties_forplacement_.md)
  Sets the view properties in the split arrangement for a specific placement.
- [UISplitArrangementViewProperties](./uisplitarrangementviewproperties.md)
  Properties you use to customize how a split arrangement presents a view.

## Relationships

### Inherits From
- [UIArrangement](./uiarrangement.md)

## See Also

### Configuring the arrangement
- [UIOverlayArrangement](./uioverlayarrangement-c.class.md)
  An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [UIArrangement](./uiarrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [- updateArrangement:](./uiarrangementviewcontroller/updatearrangement_.md)
  Updates the arrangement of the view controller.
- [- updateArrangement:animated:](./uiarrangementviewcontroller/updatearrangement_animated_.md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangement-c.class)*