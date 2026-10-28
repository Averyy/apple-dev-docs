# UIView.ReservedRegion

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A region within a view’s coordinate space that another entity reserves.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct ReservedRegion
```

## Overview

A reserved region indicates an area within a view’s coordinate space that an entity, such as the device hardware, reserves. Arrange your view’s content to account for this region. Each region describes a frame, margins, active state, and an identifier. For example, a camera or the Dynamic Island can cover part of the display, and the hinge of iPhone Duo divides the display into two halves.

There are two categories of reserved regions, which you specify with a [`UIView.ReservedRegion.Kind`](./reservedregion/kind-swift.struct.md) value:

- **[`occlusion`](./reservedregion/kind-swift.struct/occlusion.md)**: An area where an element, such as the Dynamic Island, a camera, or window controls, covers content. Place content outside this area.
- **[`division`](./reservedregion/kind-swift.struct/division.md)**: An area where content splits into separate regions, such as at the fold of a hinge. Arrange your content into separate sections on each side of this area.

## Get the reserved regions that intersect your view

Parts of the display aren’t available for your content. For example, a camera or the Dynamic Island covers part of your view, and the fold of iPhone Duo splits it in two. The system describes each of these areas as a reserved region.

Framework-provided views, such as split view controllers and sheets, adjust for reserved regions for you. If you build a custom view that places its own content, find out where the reserved regions are and arrange your content around them.

To get the reserved regions, call [`reservedRegions(kind:options:)`](./reservedregions%28kind,options%29.md) on your view. Use the `kind` parameter to choose which regions you want: `.occlusion` for areas that cover your content, such as a camera, and `.division` for areas that split it, such as the fold. By default, the method returns only active regions that currently affect your view. The following example gets the regions that cover part of the view:

```swift
let regions = reservedRegions(kind: .occlusion)
```

The method returns only the regions that overlap your view, including a partial overlap. For example, if a camera region overlaps with a corner of your view, its frame can start at negative coordinates or extend past the view’s size. Regions elsewhere on the screen don’t appear in the results.

Each region has a [`frame`](./reservedregion/frame.md), a rectangle that describes where the region is within your view. The frame uses your view’s own coordinates, not the screen’s, and the values are in points. The frame already includes the region’s [`margins`](./reservedregion/margins.md), which is extra space around the reserved area that keeps interactive content clear of it, so you don’t need to add the margins yourself.

## Keep content visible around occlusion regions

An occlusion region covers part of your view; people can’t see content that you place there. Use the [`frame`](./reservedregion/frame.md) of each occlusion region to update the constants of your Auto Layout constraints to move your content out of the way.

The following example keeps a button bar, a custom row of buttons along the top of the view, clear of a region at the top. It checks only the regions that overlap the area the bar reserves, because an occlusion region can be anywhere in the view. It then moves the bar down, below the lowest of those regions:

```swift
class ControlsView: UIView {
    let buttonBar = UIView()
    private let barHeight: CGFloat = 60
    private var topConstraint: NSLayoutConstraint!

    override init(frame: CGRect) {
        super.init(frame: frame)
        buttonBar.translatesAutoresizingMaskIntoConstraints = false
        addSubview(buttonBar)
        topConstraint = buttonBar.topAnchor.constraint(equalTo: topAnchor)
        NSLayoutConstraint.activate([
            topConstraint,
            buttonBar.heightAnchor.constraint(equalToConstant: barHeight),
            buttonBar.leadingAnchor.constraint(equalTo: leadingAnchor),
            buttonBar.trailingAnchor.constraint(equalTo: trailingAnchor)
        ])
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func updateConstraints() {
        let regions = reservedRegions(kind: .occlusion)
        let barFrame = CGRect(x: 0, y: 0, width: bounds.width, height: barHeight)
        topConstraint.constant = regions
            .filter { $0.frame.intersects(barFrame) }
            .map(\.frame.maxY)
            .max() ?? 0
        super.updateConstraints()
    }
}
```

UIKit tracks the regions you read in `updateConstraints()` and runs it again when they change, so the constraint stays current as regions become active or inactive.

## Split your content at a division

A division region is an area that splits your view into separate parts, such as the fold of iPhone Duo. A division is active only when the device is partially open or closed. When iPhone Duo is fully open, the division is inactive, and [`reservedRegions(kind:options:)`](./reservedregions%28kind,options%29.md) returns no division regions.

When a division is active, content that crosses it is hard to read and use, so keep each view entirely on one side of the division. Because a division can run in either direction, the sides depend on how someone folds the device. When you partially fold iPhone Duo like a book, the fold runs vertically, so your content sits side by side. When you partially fold it like a laptop, the fold runs horizontally, so your content rests above and below the fold.

To find which direction the fold runs, compare the width and height of the division’s frame. Then constrain each of your views to its side of the frame in the same way as in the previous example, and leave the space the division reserves empty. If your content is two related views that sit side by side or one above the other, use [`UIArrangementViewController`](../uiarrangementviewcontroller.md) instead of reading the division yourself. For more information, see “Choose where to check for regions,” below.

As someone opens or closes the device, your layout changes with the division. When you adjust your layout for the fold, move only what’s necessary to keep elements visible and easy to tap. Controls that disappear or shift dramatically are harder to find and track. Favor small adjustments over rearrangement. If your layout is a grid, use an even number of columns so your content divides cleanly at the fold.

## Choose where to check for regions

Most apps don’t need to check for reserved regions. Framework-provided views, such as split view controllers, tab bars, alerts, context menus, and sheets, already adjust for the fold and the camera, so the content you place in them stays clear of those areas. Use those views when you can.

Scrolling containers, such as table views, collection views, and scroll views, don’t split their content around a division by default. When the device is partially open, a row or item can run across the fold. If that makes your content harder to read or use, check for division regions and arrange the content yourself.

If your custom view arranges two related views around the fold, use [`UIArrangementViewController`](../uiarrangementviewcontroller.md) instead of reading regions yourself. A split arrangement places the two views side by side or one above the other, and keeps them on separate sides of the fold. An overlay arrangement layers one view over the other, and moves them to separate sides of the fold when the device is partially open. Place an arrangement view outside scroll views, collection views, and other containers that could make part of your view inaccessible.

Check for reserved regions yourself in custom views where controls or other important content might end up in the fold or near the camera. For example, check in a custom overlay, a floating control, or a view that positions its content with explicit frames or constraints. Check in the view that positions the content, so the frames you read use the same coordinates as the content you place.

## Include inactive regions

A reserved region can become active or inactive as conditions change. An active region currently affects your view. An inactive region doesn’t. For example, the fold of iPhone Duo becomes active when the device is partially open, and inactive again when it’s fully open. The inner camera is active only while the camera is in use, and the outer camera is always active.

By default, [`reservedRegions(kind:options:)`](./reservedregions%28kind,options%29.md) returns only the active regions. To also get the inactive regions, pass [`includeInactive`](./reservedregion/queryoptions/includeinactive.md) for the `options` parameter:

```swift
let regions = reservedRegions(kind: .occlusion, options: .includeInactive)
```

Check the [`isActive`](./reservedregion/isactive.md) property of each region to find out whether it currently affects your view. An inactive region still has a frame, so you can leave room for it. This keeps your layout from jumping when the region becomes active, such as when someone folds the device or starts using the inner camera.

For more information about preparing your app for a device with a folding display, see [Preparing your app for iPhone Duo](../../TechnologyOverviews/preparing-your-app-for-iphone-duo.md). For design guidance, see Human Interface Guidelines > [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

## Topics

### Getting region details
- [let frame: CGRect](./reservedregion/frame.md)
  The rectangle that describes the region within your view.
- [let isActive: Bool](./reservedregion/isactive.md)
  A Boolean value that indicates whether the region is active.
- [let kind: UIView.ReservedRegion.Kind](./reservedregion/kind-swift.property.md)
  The kind of the region.
- [UIView.ReservedRegion.Kind](./reservedregion/kind-swift.struct.md)
  A kind of reserved region.
- [let margins: UIEdgeInsets](./reservedregion/margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.
### Querying reserved regions
- [UIView.ReservedRegion.QueryOptions](./reservedregion/queryoptions.md)
  Options for querying reserved regions.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Reserved regions
- [func reservedRegions(kind: UIView.ReservedRegion.Kind, options: UIView.ReservedRegion.QueryOptions) -> [UIView.ReservedRegion]](./reservedregions%28kind,options%29.md)
  Returns the reserved regions of a kind that overlap the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion)*