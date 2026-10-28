# setEditing(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the view controller shows an editable view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func setEditing(_ editing: Bool, animated: Bool)
```

```objc
- (void) setEditing:(BOOL) editing animated:(BOOL) animated;
```

## Discussion

Subclasses that use an edit-done button must override this method to change their view to an editable state if [`isEditing`](./isediting.md) is [`true`](../../Swift/true.md) and a non-editable state if it is [`false`](../../Swift/false.md). This method should invoke super’s implementation before updating its view.

## Parameters

- `editing`: If [`true`](../../Swift/true.md), the view controller should display an editable view; otherwise, [`false`](../../Swift/false.md).

  If [`true`](../../Swift/true.md) and one of the custom views of the [`navigationItem`](./navigationitem.md) property is set to the value returned by the [`editButtonItem`](./editbuttonitem.md) method, the associated navigation controller displays a Done button; otherwise, an Edit button.
- `animated`: If [`true`](../../Swift/true.md), animates the transition; otherwise, does not.

## See Also

### Adding editing behaviors to your view controller
- [var isEditing: Bool](./isediting.md)
  A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [var editButtonItem: UIBarButtonItem](./editbuttonitem.md)
  Returns a bar button item that toggles its title and associated state between Edit and Done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setediting(_:animated:))*