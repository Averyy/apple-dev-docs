# PMPrinter

**Framework**: Application Services  
**Kind**: tdef

An opaque type that represents a printer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias PMPrinter = OpaquePointer
```

#### Discussion

You typically obtain a printer object using the function [`PMSessionGetCurrentPrinter(_:_:)`](1458998-pmsessiongetcurrentprinter.md) or [`PMServerCreatePrinterList(_:_:)`](1459953-pmservercreateprinterlist.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pmprinter)*