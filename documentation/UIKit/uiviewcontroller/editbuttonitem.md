# editButtonItem

**Framework**: UIKit  
**Kind**: property

Returns a bar button item that toggles its title and associated state between Edit and Done.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var editButtonItem: UIBarButtonItem { get }
```

#### Discussion

If one of the custom views of the [`navigationItem`](uiviewcontroller/navigationitem.md) property is set to the returned object, the associated navigation bar displays an Edit button if [`isEditing`](uiviewcontroller/isediting.md) is [`false`](https://developer.apple.com/documentation/Swift/false) and a Done button if [`isEditing`](uiviewcontroller/isediting.md) is [`true`](https://developer.apple.com/documentation/Swift/true). The default button action invokes the [`setEditing(_:animated:)`](uiviewcontroller/setediting(_:animated:).md) method.

## See Also

- [var isEditing: Bool](uiviewcontroller/isediting.md)
  A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [func setEditing(Bool, animated: Bool)](uiviewcontroller/setediting(_:animated:).md)
  Sets whether the view controller shows an editable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/editbuttonitem)*