# editButtonItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns a bar button item that toggles its title and associated state between Edit and Done.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var editButtonItem: UIBarButtonItem { get }
```

```objc
@property (nonatomic, readonly) UIBarButtonItem * editButtonItem;
```

## Discussion

If one of the custom views of the [`navigationItem`](./navigationitem.md) property is set to the returned object, the associated navigation bar displays an Edit button if [`isEditing`](./isediting.md) is [`false`](../../Swift/false.md) and a Done button if [`isEditing`](./isediting.md) is [`true`](../../Swift/true.md). The default button action invokes the [`setEditing(_:animated:)`](./setediting%28_,animated%29.md) method.

## See Also

### Adding editing behaviors to your view controller
- [var isEditing: Bool](./isediting.md)
  A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [func setEditing(Bool, animated: Bool)](./setediting%28_,animated%29.md)
  Sets whether the view controller shows an editable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/editbuttonitem)*