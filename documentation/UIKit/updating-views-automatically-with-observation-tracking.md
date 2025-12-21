# Updating views automatically with observation tracking

**Framework**: UIKit

Use Swift Observation and UIKit’s automatic tracking to update your views in response to model data updates.

#### Overview

Traditionally, when your app’s model data changes, you need to update your views with the new data. Depending on what you update, you may also need to manually call methods like [`setNeedsLayout()`](uiview/setneedslayout().md) or [`setNeedsDisplay()`](uiview/setneedsdisplay().md) to refresh your view layouts. This approach requires you to remember when and where to invalidate views, creating opportunities for bugs and outdated displays.

Swift [`Observation`](https://developer.apple.com/documentation/Observation) provides the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) macro to mark your models for automatic change tracking. When you combine `Observable` models with UIKit, the system automatically watches for property changes and updates your views. You don’t need to manually invalidate anything — UIKit handles it for you.

UIKit provides methods and closures in several objects where [`Automatic observation tracking`](automatic-observation-tracking.md) happens. In a view subclass, [`updateProperties()`](uiview/updateproperties().md) and [`layoutSubviews()`](uiview/layoutsubviews().md) are examples of two methods where your updates receive automatic observation tracking. The `updateProperties` method runs before layout and is ideal for configuring properties like text, colors, and visibility. The `layoutSubviews` method handles geometry and positioning. Both methods automatically track any `Observable` properties you read, and UIKit updates your views when those properties change.

> **Note**: In iOS 18, the system doesn’t enable automatic observation tracking by default. To enable it, add the [`UIObservationTrackingEnabled`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIObservationTrackingEnabled) key to your app’s information property list and set the key’s value to [`true`](https://developer.apple.com/documentation/Swift/true).

##### Update View Properties Automatically

The [`updateProperties()`](uiviewcontroller/updateproperties().md) method automatically tracks `Observable` properties and updates views when they change. For example, to show a message list with a status label that displays unread message information, start by creating an `Observable` model with the properties your view needs:

```swift
@Observable
class MessageModel {
    var showStatus: Bool
    var statusText: String
}
```

Then, use these properties in your view controller’s `updateProperties()` method:

```swift
override func updateProperties() {
    super.updateProperties()
    statusLabel.alpha = model.showStatus ? 1.0 : 0.0
    statusLabel.text = model.statusText
}
```

When the view first appears, UIKit runs `updateProperties()` and tracks that you read `showStatus` and `statusText`. If either property changes later, UIKit automatically runs `updateProperties()` again to update the label.

You can also automatically track changes in a custom view using [`updateProperties()`](uiview/updateproperties().md).

> **Note**: To get automatic observation tracking in iOS 18, use [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md).

##### Configure Collection View and Table View Cells Automatically

Collection view and table view cells also support automatic observation tracking through their configuration update handler. For example, to show a list where each cell displays information from an `Observable` model, start by creating an `Observable` model for your list items:

```swift
@Observable
class ListItemModel {
    var icon: UIImage?
    var title: String
    var subtitle: String
}
```

Then, in your cell provider, set up the configuration update handler to use the model:

```swift
cell.configurationUpdateHandler = { cell, state in
    var config = UIListContentConfiguration.cell()
    config.image = model.icon
    config.text = model.title
    config.secondaryText = model.subtitle
    cell.contentConfiguration = config
}
```

UIKit automatically tracks the `Observable` model properties you use in the handler. When any of these properties change while the cell is visible, UIKit runs the handler again to update the cell. This pattern is especially useful for lists in your app where model data changes frequently.

##### Separate Property Updates From Layout

Use `updateProperties()` for configuring content and styling, such as putting text in labels and adjusting colors based on data. Reserve `layoutSubviews()` for geometry calculations, such as setting a frame for a view when using Auto Layout constraints doesn’t work for your situation. This separation improves performance by avoiding unnecessary layout passes.

The following example shows a badge view that updates its count without triggering layout:

```swift
override func updateProperties() {
    super.updateProperties()
    badgeItem.badge = "\(model.count)"
}
```

By using `updateProperties()` instead of `layoutSubviews()`, you avoid re-running layout code when the badge count changes. The view only updates the badge text, not its size or position. Moving your code that doesn’t affect layout into `updateProperties()` is especially important for views that update frequently.

If you need to manually trigger property updates, call [`setNeedsUpdateProperties()`](uiviewcontroller/setneedsupdateproperties().md) on your view controller or [`setNeedsUpdateProperties()`](uiview/setneedsupdateproperties().md) on your view. This method tells UIKit to call `updateProperties()` during the next update pass.

##### Optimize the Uikit Update Pass

UIKit performs updates in a specific order to help your views display correctly. Place your code in the right method to keep your user interface up-to-date and avoid performance issues.

The update pass follows these steps:

1. The trait collection updates with the current environment values.
2. UIKit runs `updateProperties()` if necessary, where you configure properties and styling.
3. UIKit runs `layoutSubviews()` if necessary, where you calculate geometry and positioning.
4. The display pass renders draw methods to create the visual output.
5. The system presents the rendered frame on screen.

If any step causes other views to need updates, UIKit repeats the process until all views are current.

Because `updateProperties()` runs after the trait collection updates, your app can safely read trait values there. `updateProperties()` runs before `layoutSubviews()`, so your app can invalidate layout if needed, and the layout pass runs immediately afterward. UIKit may skip calling either `updateProperties()` or `layoutSubviews()` during an update pass when there are no pending changes to update.

## See Also

- [Automatic observation tracking](automatic-observation-tracking.md)
  Simplify updating views when data changes by making updates in methods that support automatic observation tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/updating-views-automatically-with-observation-tracking)*