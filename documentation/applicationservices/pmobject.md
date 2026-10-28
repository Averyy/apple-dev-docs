# PMObject

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

The base type for all the opaque types used in Core Printing.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias PMObject = UnsafeRawPointer
```

```c
typedef const void *PMObject;
```

## Discussion

`PMObject` is the base type for opaque types such as `PMPrintSession`, `PMPageFormat`, `PMPrintSettings`, `PMPrinter`, `PMPaper`, `PMPreset`, and `PMServer`. `PMObject` is used in functions such as [`PMRetain(_:)`](./api-1460190-pmretain.md) and [`PMRelease(_:)`](./api-1461402-pmrelease.md) that operate on any opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pmobject)*