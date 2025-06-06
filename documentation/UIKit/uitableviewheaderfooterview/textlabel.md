# textLabel

**Framework**: UIKit  
**Kind**: property

A primary text label for the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textLabel: UILabel? { get }
```

#### Discussion

Accessing the value in this property causes the view to create a default label for displaying a detail text string. If you are managing the content of the view yourself by adding subviews to the [`contentView`](uitableviewheaderfooterview/contentview.md) property, you should not access this property.

The label sizes to fit the content view area in the best way possible according to the size of the string. Its size also adjusts depending on whether there is a detail text label present.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](uitableviewheaderfooterview/contentconfiguration-6b4eg.md) resets this property to `nil`.

## See Also

- [var detailTextLabel: UILabel?](uitableviewheaderfooterview/detailtextlabel.md)
  A detail text label for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/textlabel)*