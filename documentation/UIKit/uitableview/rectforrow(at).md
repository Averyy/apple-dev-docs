# rectForRow(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the drawing area for a row that an index path identifies.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func rectForRow(at indexPath: IndexPath) -> CGRect
```

```objc
- (CGRect) rectForRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

A rectangle defining the area in which the table view draws the row or [`CGRectZero`](../../CoreGraphics/cgrectzero.md) if `indexPath` is invalid.

## Parameters

- `indexPath`: An index path object that identifies a row by its index and its section index.

## See Also

### Getting the drawing areas for the table
- [func rect(forSection: Int) -> CGRect](./rect%28forsection%29.md)
  Returns the drawing area for a specified section of the table view.
- [func rectForFooter(inSection: Int) -> CGRect](./rectforfooter%28insection%29.md)
  Returns the drawing area for the footer of the specified section.
- [func rectForHeader(inSection: Int) -> CGRect](./rectforheader%28insection%29.md)
  Returns the drawing area for the header of the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/rectforrow(at:))*