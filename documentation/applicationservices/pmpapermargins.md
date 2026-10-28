# PMPaperMargins

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

A data structure that specifies the unprintable area of a paper object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
typealias PMPaperMargins = PMRect
```

```c
typedef PMRect PMPaperMargins;
```

## Discussion

Your application specifies paper margins when calling the function [`PMPaperCreateCustom(_:_:_:_:_:_:_:)`](./api-1459322-pmpapercreatecustom.md) to create a custom paper type. You can obtain a paper’s margins with the function [`PMPaperGetMargins(_:_:)`](./api-1461994-pmpapergetmargins.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pmpapermargins)*