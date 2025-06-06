# viewPrintFormatter()

**Framework**: UIKit  
**Kind**: method

Returns a print formatter for the receiving view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func viewPrintFormatter() -> UIViewPrintFormatter
```

#### Return Value

A [`UIViewPrintFormatter`](uiviewprintformatter.md) object or `nil` if the object could not be created. If it is successfully created, the returned object is automatically associated with this view.

#### Discussion

When initiating a print job, you can call this method to obtain an appropriate view print formatter object for your view. You can use the formatter object to configure the page layout options for your view during printing. Each time you call this method, you get a unique view print formatter object.

For more information about how to use print formatters to configure the printing behavior of your view, see [`Drawing and Printing Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

## See Also

- [func draw(CGRect, for: UIViewPrintFormatter)](uiview/draw(_:for:).md)
  Implemented to draw the view’s content for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/viewprintformatter())*