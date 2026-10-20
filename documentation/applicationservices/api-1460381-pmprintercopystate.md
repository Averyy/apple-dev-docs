# PMPrinterCopyState(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.6+

## Declaration

```swift
func PMPrinterCopyState(_ printer: PMPrinter, _ stateDict: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus
```

```c
OSStatus PMPrinterCopyState(PMPrinter printer, CFDictionaryRef  _Nullable *stateDict);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460381-pmprintercopystate)*