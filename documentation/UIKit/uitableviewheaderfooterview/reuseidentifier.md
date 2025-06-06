# reuseIdentifier

**Framework**: UIKit  
**Kind**: property

A string used to identify a reusable header or footer.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var reuseIdentifier: String? { get }
```

#### Discussion

You assign a reuse identifier to a header or footer view at creation time. Once assigned, the table view uses that reuse identifier to gather your views when they’re scrolled offscreen and queue them for later reuse. You can retrieve header or footer views by passing the same reuse identifier to the [`dequeueReusableHeaderFooterView(withIdentifier:)`](uitableview/dequeuereusableheaderfooterview(withidentifier:).md) method of the table view.

## See Also

- [func prepareForReuse()](uitableviewheaderfooterview/prepareforreuse.md)
  Prepares a reusable header or footer view for reuse by the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/reuseidentifier)*