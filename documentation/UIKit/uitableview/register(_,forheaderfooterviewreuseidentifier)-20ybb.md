# register(_:forHeaderFooterViewReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers a class to use in creating new table header or footer views.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func register(_ aClass: AnyClass?, forHeaderFooterViewReuseIdentifier identifier: String)
```

```objc
- (void) registerClass:(Class) aClass forHeaderFooterViewReuseIdentifier:(NSString *) identifier;
```

## Discussion

Before dequeueing any header or footer views, call this method or the [`register(_:forHeaderFooterViewReuseIdentifier:)`](./register%28_,forheaderfooterviewreuseidentifier%29-1rgvc.md) method to tell the table view how to create new instances of your views. If a view of the specified type isn’t currently in a reuse queue, the table view uses the provided information to create a one automatically.

If you previously registered a class or nib file with the same reuse identifier, the class you specify in the `aClass` parameter replaces the old entry. You may specify `nil` for `aClass` if you want to unregister the class from the specified reuse identifier.

## Parameters

- `aClass`: The class of the header or footer view that you want to register. You must specify either [`UITableViewHeaderFooterView`](../uitableviewheaderfooterview.md) or a subclass of it.
- `identifier`: The reuse identifier for the header or footer view. This parameter must not be `nil` and must not be an empty string.

## See Also

### Recycling section headers and footers
- [func register(UINib?, forHeaderFooterViewReuseIdentifier: String)](./register%28_,forheaderfooterviewreuseidentifier%29-1rgvc.md)
  Registers a nib object that contains a header or footer with the table view under a specified identifier.
- [func dequeueReusableHeaderFooterView(withIdentifier: String) -> UITableViewHeaderFooterView?](./dequeuereusableheaderfooterview%28withidentifier%29.md)
  Returns a reusable header or footer view after locating it by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb)*