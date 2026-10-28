# draw(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Implemented to draw the view’s content for printing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)
```

```objc
- (void) drawRect:(CGRect) rect forViewPrintFormatter:(UIViewPrintFormatter *) formatter;
```

## Discussion

You implement this method if you want a view’s printed content to appear differently than its displayed content. If you add a view print formatter to a print job but do not implement this method, the view’s [`draw(_:)`](./draw%28_%29.md) method is called to provide the content for printing.

For more information about how to implement a custom drawing routine for printed content, see [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

## Parameters

- `rect`: A rectangle that defines the area for drawing printable content.
- `formatter`: An instance of [`UIViewPrintFormatter`](../uiviewprintformatter.md) obtained by calling the [`viewPrintFormatter()`](./viewprintformatter%28%29.md) method.

## See Also

### Formatting printed view content
- [func viewPrintFormatter() -> UIViewPrintFormatter](./viewprintformatter%28%29.md)
  Returns a print formatter for the receiving view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/draw(_:for:))*