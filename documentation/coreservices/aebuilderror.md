# AEBuildError

**Framework**: Core Services  
**Kind**: struct

Defines a structure for storing additional error codeinformation for “AEBuild” routines.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AEBuildError
```

## Topics

### Initializers
- [init()](aebuilderror/1447428-init.md)
- [init(fError: AEBuildErrorCode, fErrorPos: UInt32)](aebuilderror/1449472-init.md)
### Instance Properties
- [var fError: AEBuildErrorCode](aebuilderror/1446581-ferror.md)
  The error code. See [`AEBuildErrorCode`](aebuilderrorcode.md) for alist of errors. 
- [var fErrorPos: UInt32](aebuilderror/1448861-ferrorpos.md)
  The character position where the parser detectedthe error. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aebuilderror)*