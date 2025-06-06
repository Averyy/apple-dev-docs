# rect(forSection:)

**Framework**: UIKit  
**Kind**: method

Returns the drawing area for a specified section of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func rect(forSection section: Int) -> CGRect
```

#### Return Value

A rectangle defining the area in which the table view draws the section.

## Parameters

- `section`: An index number identifying a section of the table view. Plain-style table views always have a section index of zero.

## See Also

- [func rectForRow(at: IndexPath) -> CGRect](uitableview/rectforrow(at:).md)
  Returns the drawing area for a row that an index path identifies.
- [func rectForFooter(inSection: Int) -> CGRect](uitableview/rectforfooter(insection:).md)
  Returns the drawing area for the footer of the specified section.
- [func rectForHeader(inSection: Int) -> CGRect](uitableview/rectforheader(insection:).md)
  Returns the drawing area for the header of the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/rect(forsection:))*