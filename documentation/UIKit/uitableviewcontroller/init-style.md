# init(style:)

**Framework**: UIKit  
**Kind**: init

Initializes a table view controller to manage a table view of a given style.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(style: UITableView.Style)
```

#### Return Value

An initialized [`UITableViewController`](uitableviewcontroller.md) object.

#### Discussion

If you use the standard `init` method to initialize a [`UITableViewController`](uitableviewcontroller.md) object, a table view in the plain style is created.

## Parameters

- `style`: A constant that specifies the style of table view that the controller object is to manage (  or  ).

## See Also

- [init(nibName: String?, bundle: Bundle?)](uitableviewcontroller/init(nibname:bundle:).md)
  Creates a table view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uitableviewcontroller/init(coder:).md)
  Creates a table view controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcontroller/init(style:))*