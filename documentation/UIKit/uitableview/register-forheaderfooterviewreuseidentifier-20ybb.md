# register(_:forHeaderFooterViewReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a class to use in creating new table header or footer views.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func register(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String)
```

#### Discussion

Before dequeueing any header or footer views, call this method or the [`register(_:forHeaderFooterViewReuseIdentifier:)`](uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc.md) method to tell the table view how to create new instances of your views. If a view of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a one automatically.

If you previously registered a class or nib file with the same reuse identifier, the class you specify in the `aClass` parameter replaces the old entry. You may specify `nil` for `aClass` if you want to unregister the class from the specified reuse identifier.

## Parameters

- `aClass`: The class of the header or footer view that you want to register. You must specify either   or a subclass of it.
- `identifier`: The reuse identifier for the header or footer view. This parameter must not be   and must not be an empty string.

## See Also

- [func register(UINib?, forHeaderFooterViewReuseIdentifier: String)](uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc.md)
  Registers a nib object that contains a header or footer with the table view under a specified identifier.
- [func dequeueReusableHeaderFooterView(withIdentifier: String) -> UITableViewHeaderFooterView?](uitableview/dequeuereusableheaderfooterview(withidentifier:).md)
  Returns a reusable header or footer view after locating it by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb)*