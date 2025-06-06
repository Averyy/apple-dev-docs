# contentView

**Framework**: UIKit  
**Kind**: property

The content view of the header or footer.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentView: UIView { get }
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Discussion

To create your header or footer content, you add subviews to the view in this property. Your custom subviews represent the main content of your header or footer. Be sure to configure all subviews.

## See Also

- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewheaderfooterview/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewheaderfooterview/contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the view automatically updates its content configuration when its state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/contentview)*