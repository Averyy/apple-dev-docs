# isEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the view controller currently allows the user to edit the view contents.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isEditing: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the view controller currently allows editing; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

If the view is editable and the associated navigation controller contains an edit-done button, then a Done button is displayed; otherwise, an Edit button is displayed. Clicking either button toggles the state of this property. Add an edit-done button by setting the custom left or right view of the navigation item to the value returned by the [`editButtonItem`](uiviewcontroller/editbuttonitem.md) method. Set the [`isEditing`](uiviewcontroller/isediting.md) property to the initial state of your view. Use the [`setEditing(_:animated:)`](uiviewcontroller/setediting(_:animated:).md) method as an action method to animate the transition of this state if the view is already displayed.

## See Also

- [func setEditing(Bool, animated: Bool)](uiviewcontroller/setediting(_:animated:).md)
  Sets whether the view controller shows an editable view.
- [var editButtonItem: UIBarButtonItem](uiviewcontroller/editbuttonitem.md)
  Returns a bar button item that toggles its title and associated state between Edit and Done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/isediting)*