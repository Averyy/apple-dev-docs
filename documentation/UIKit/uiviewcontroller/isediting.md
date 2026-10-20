# isEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view controller currently allows the user to edit the view contents.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isEditing: Bool { get set }
```

```objc
@property (nonatomic, getter=isEditing) BOOL editing;
```

#### Discussion

If [`true`](../../Swift/true.md), the view controller currently allows editing; otherwise, [`false`](../../Swift/false.md).

If the view is editable and the associated navigation controller contains an edit-done button, then a Done button is displayed; otherwise, an Edit button is displayed. Clicking either button toggles the state of this property. Add an edit-done button by setting the custom left or right view of the navigation item to the value returned by the [`editButtonItem`](./editbuttonitem.md) method. Set the [`isEditing`](./isediting.md) property to the initial state of your view. Use the [`setEditing(_:animated:)`](./setediting%28_,animated%29.md) method as an action method to animate the transition of this state if the view is already displayed.

## See Also

### Adding editing behaviors to your view controller
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Sets whether the view controller shows an editable view.
- [var editButtonItem: UIBarButtonItem](./editbuttonitem.md)
  Returns a bar button item that toggles its title and associated state between Edit and Done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/isediting)*