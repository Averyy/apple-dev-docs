# register(_:forHeaderFooterViewReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a nib object that contains a header or footer with the table view under a specified identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func register(_ nib: UINib?, forHeaderFooterViewReuseIdentifier identifier: String)
```

#### Discussion

Before dequeueing any header or footer views, call this method or the [`register(_:forHeaderFooterViewReuseIdentifier:)`](uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb.md) method to tell the table view how to create new instances of your views. If a view of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a new one automatically.

If you previously registered a class or nib file with the same reuse identifier, the nib you specify in the `nib` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the nib from the specified reuse identifier.

## Parameters

- `nib`: A nib object that specifies the nib file to use to create the header or footer view. This parameter can’t be  .
- `identifier`: The reuse identifier for the header or footer view. This parameter must not be   and must not be an empty string.

## See Also

- [func register(AnyClass?, forHeaderFooterViewReuseIdentifier: String)](uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb.md)
  Registers a class to use in creating new table header or footer views.
- [func dequeueReusableHeaderFooterView(withIdentifier: String) -> UITableViewHeaderFooterView?](uitableview/dequeuereusableheaderfooterview(withidentifier:).md)
  Returns a reusable header or footer view after locating it by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc)*