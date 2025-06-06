# rectForRow(at:)

**Framework**: UIKit  
**Kind**: method

Returns the drawing area for a row that an index path identifies.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func rectForRow(at indexPath: IndexPath) -> CGRect
```

#### Return Value

A rectangle defining the area in which the table view draws the row or [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) if `indexPath` is invalid.

## Parameters

- `indexPath`: An index path object that identifies a row by its index and its section index.

## See Also

- [func rect(forSection: Int) -> CGRect](uitableview/rect(forsection:).md)
  Returns the drawing area for a specified section of the table view.
- [func rectForFooter(inSection: Int) -> CGRect](uitableview/rectforfooter(insection:).md)
  Returns the drawing area for the footer of the specified section.
- [func rectForHeader(inSection: Int) -> CGRect](uitableview/rectforheader(insection:).md)
  Returns the drawing area for the header of the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/rectforrow(at:))*