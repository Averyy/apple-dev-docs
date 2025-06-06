# init(reuseIdentifier:)

**Framework**: UIKit  
**Kind**: init

Initializes a header-footer view with the specified reuse identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(reuseIdentifier: String?)
```

#### Return Value

An initialized [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md) object or `nil` if the object could not be created.

#### Discussion

Once set, you can’t change the reuse identifier for the returned view object.

## Parameters

- `reuseIdentifier`: A string used to identify the header or footer view if it’s to be reused by multiple sections. Pass   if the view isn’t to be reused. You should use the same reuse identifier for all header or footer views of the same form.

## See Also

- [init?(coder: NSCoder)](uitableviewheaderfooterview/init(coder:).md)
  Creates a header-footer view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/init(reuseidentifier:))*