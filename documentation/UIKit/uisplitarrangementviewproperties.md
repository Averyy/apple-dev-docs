# UISplitArrangementViewProperties

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Properties you use to customize how a split arrangement presents a view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@interface UISplitArrangementViewProperties : NSObject
```

## Overview

By default, a split arrangement sizes the primary and secondary views equally when a display has one region. Influence how the arrangement view computes the sizes for each view by setting the split arrangement’s view properties for each placement to use an automatic size, a fixed layout size, a fractional layout size, or an intrinsic content size.

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

## Topics

### Creating view properties
- [- init](./uisplitarrangementviewproperties/init.md)
  Creates a set of split arrangement view properties.
### Configuring the view
- [width](./uisplitarrangementviewproperties/width.md)
  The width dimension range for the view.
- [height](./uisplitarrangementviewproperties/height.md)
  The height dimension range for the view.
- [UISplitArrangementDimensionRange](./uisplitarrangementdimensionrange.md)
  A range of dimensions defining the minimum, preferred, and maximum size for a view within a split arrangement.
- [layoutPriority](./uisplitarrangementviewproperties/layoutpriority.md)
  The layout priority of the view within the split arrangement.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Configuring the arrangement
- [axes](./uisplitarrangement-c.class/axes.md)
  The axes of the arrangement.
- [defaultViewProperties](./uisplitarrangement-c.class/defaultviewproperties.md)
  Returns the default properties for a view in the split arrangement.
- [- setViewProperties:forPlacement:](./uisplitarrangement-c.class/setviewproperties_forplacement_.md)
  Sets the view properties in the split arrangement for a specific placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitarrangementviewproperties)*