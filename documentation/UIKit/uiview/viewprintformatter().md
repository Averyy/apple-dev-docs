# viewPrintFormatter()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a print formatter for the receiving view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
func viewPrintFormatter() -> UIViewPrintFormatter
```

```objc
- (UIViewPrintFormatter *) viewPrintFormatter;
```

#### Return Value

A [`UIViewPrintFormatter`](../uiviewprintformatter.md) object or `nil` if the object could not be created. If it is successfully created, the returned object is automatically associated with this view.

#### Discussion

When initiating a print job, you can call this method to obtain an appropriate view print formatter object for your view. You can use the formatter object to configure the page layout options for your view during printing. Each time you call this method, you get a unique view print formatter object.

For more information about how to use print formatters to configure the printing behavior of your view, see [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

## See Also

### Formatting printed view content
- [func draw(CGRect, for: UIViewPrintFormatter)](./draw%28_,for%29.md)
  Implemented to draw the view’s content for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/viewprintformatter())*