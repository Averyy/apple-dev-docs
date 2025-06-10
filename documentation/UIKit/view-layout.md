# View layout

**Framework**: UIKit

Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.

#### Overview

When you design your app’s interface, you position views and other interface elements in your app’s windows and size them appropriately. However, the size and position of those views may need to change at runtime for a variety of reasons:

- The user can resize the window containing your views.
- Variations in the screen sizes of iOS devices (including differences between portrait and landscape orientations) require different layouts for each device and orientation.
- Apps on iPad must adapt to cover different amounts of screen space, ranging from a third of the screen to the entire screen.
- Language changes might require size changes for labels and other text-based views.
- Dynamic Type allows changes to the size of the text, which affects the size of the view.

[`UIStackView`](uistackview.md) objects adjust the position of their contained views automatically when interface dimensions change. Alternatively, Auto Layout constraints let you specify the rules that determine the size and position of the views in your interface.

## Topics

### Essentials
- [class UIStackView](uistackview.md)
  A streamlined interface for laying out a collection of views in either a column or a row.
### Localization
- [Autosizing Views for Localization in iOS](../xcode/autosizing_views_for_localization_in_ios.md)
  Add auto layout constraints to your app to achieve localizable views.
### Constraints
- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [class NSLayoutConstraint](nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
- [protocol UILayoutSupport](uilayoutsupport.md)
  A set of methods that provide layout support and access to layout anchors.
### Layout guides
- [class UILayoutGuide](uilayoutguide.md)
  A rectangular area that can interact with Auto Layout.
- [class NSLayoutDimension](nslayoutdimension.md)
  A factory class for creating size-based layout constraint objects using a fluent API.
### Anchors
- [class NSLayoutAnchor](nslayoutanchor.md)
  A factory class for creating layout constraint objects using a fluent API.
- [class NSLayoutXAxisAnchor](nslayoutxaxisanchor.md)
  A factory class for creating horizontal layout constraint objects using a fluent API.
- [class NSLayoutYAxisAnchor](nslayoutyaxisanchor.md)
  A factory class for creating vertical layout constraint objects using a fluent API.
- [var NSLAYOUTANCHOR_H: Int32](nslayoutanchor_h.md)

## See Also

- [Views and controls](views-and-controls.md)
  Present your content onscreen and define the interactions allowed with that content.
- [View controllers](view-controllers.md)
  Manage your interface using view controllers and facilitate navigation around your app’s content.
- [Appearance customization](appearance-customization.md)
  Apply Liquid Glass to views, support Dark Mode in your app, customize the appearance of bars, and use appearance proxies to modify your UI.
- [Animation and haptics](animation-and-haptics.md)
  Provide feedback to users using view-based animations and haptics.
- [Windows and screens](windows-and-screens.md)
  Provide a container for your view hierarchies and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/view-layout)*