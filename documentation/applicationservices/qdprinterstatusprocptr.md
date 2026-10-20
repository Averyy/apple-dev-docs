# QDPrinterStatusProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDPrinterStatusProcPtr = (PrinterStatusOpcode, CGrafPtr?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*QDPrinterStatusProcPtr)(PrinterStatusOpcode opcode, CGrafPtr currentPort, void *printerStatus);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdprinterstatusprocptr)*