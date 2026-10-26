# PMPaperIsCustom(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Returns a Boolean value indicating whether a specified paper is a custom paper.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPaperIsCustom(_ paper: PMPaper) -> Bool
```

```c
Boolean PMPaperIsCustom(PMPaper paper);
```

#### Return Value

If `true`, the specified paper is a custom paper; otherwise, `false`.

#### Discussion

You can create a custom paper with the function [`PMPaperCreateCustom(_:_:_:_:_:_:_:)`](./api-1459322-pmpapercreatecustom.md).

## Parameters

- `paper`: The paper you’re querying to determine whether it’s a custom paper.

## See Also

### Creating and Using Paper Objects
- [func PMPaperCreateCustom(PMPrinter?, CFString?, CFString?, Double, Double, UnsafePointer<PMPaperMargins>, UnsafeMutablePointer<PMPaper?>) -> OSStatus](./api-1459322-pmpapercreatecustom.md)
  Creates a custom paper object.
- [PMPaperCreate](./core_printing/api-1805531-pmpapercreate.md)
  Creates a paper object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459526-pmpaperiscustom)*