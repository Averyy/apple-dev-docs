# PMPaperCreateCustom(_:_:_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a custom paper object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPaperCreateCustom(_ printer: PMPrinter?, _ id: CFString?, _ name: CFString?, _ width: Double, _ height: Double, _ margins: UnsafePointer<PMPaperMargins>, _ paperP: UnsafeMutablePointer<PMPaper?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function creates a custom paper object appropriate for the specified printer. Custom papers are treated differently than built-in papers by the printing system. To obtain one of the available built-in papers for a given printer, you can use the function [`PMPrinterGetPaperList(_:_:)`](1460088-pmprintergetpaperlist.md).

## Parameters

- `printer`: A printer for which the specified paper size is appropriate.
- `id`: A unique identifier for this custom paper. For example, you could create a UUID string and use it as the unique identifier.
- `name`: The name to display to the user for this custom paper.
- `width`: The width of the paper, in points.
- `height`: The height of the paper, in points.
- `margins`: A pointer to a   structure that specifies the unprintable margins of the paper, in points. The four values in the structure specify the top, left, bottom, and right imageable area margins of the paper.
- `paperP`: A pointer to your   variable. On return, the variable refers to a new custom paper object. You are responsible for releasing the paper object with the function  .

## See Also

- [func PMPaperIsCustom(PMPaper) -> Bool](1459526-pmpaperiscustom.md)
  Returns a Boolean value indicating whether a specified paper is a custom paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459322-pmpapercreatecustom)*