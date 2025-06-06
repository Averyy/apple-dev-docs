# setEditing(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets whether the view controller shows an editable view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func setEditing(_ editing: Bool, animated: Bool)
```

#### Discussion

Subclasses that use an edit-done button must override this method to change their view to an editable state if [`isEditing`](uiviewcontroller/isediting.md) is [`true`](https://developer.apple.com/documentation/swift/true) and a non-editable state if it is [`false`](https://developer.apple.com/documentation/swift/false). This method should invoke super’s implementation before updating its view.

## Parameters

- `editing`: If   and one of the custom views of the   property is set to the value returned by the   method, the associated navigation controller displays a Done button; otherwise, an Edit button.
- `animated`: If  , animates the transition; otherwise, does not.

## See Also

- [var isEditing: Bool](uiviewcontroller/isediting.md)
  A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [var editButtonItem: UIBarButtonItem](uiviewcontroller/editbuttonitem.md)
  Returns a bar button item that toggles its title and associated state between Edit and Done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setediting(_:animated:))*