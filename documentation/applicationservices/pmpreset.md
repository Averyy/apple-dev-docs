# PMPreset

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

An opaque type that stores information about a named preset available for a print job.

**Availability**:
- macOS 10.3+

## Declaration

```swift
typealias PMPreset = OpaquePointer
```

```c
typedef struct OpaquePMPreset *PMPreset;
```

## Discussion

Your application uses a preset object to identify a named preset in the Print dialog. You typically obtain an instance of this type using the function [`PMPrinterCopyPresets(_:_:)`](./api-1459117-pmprintercopypresets.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pmpreset)*