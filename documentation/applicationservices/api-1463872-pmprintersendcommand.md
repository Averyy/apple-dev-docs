# PMPrinterSendCommand(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.6+

## Declaration

```swift
func PMPrinterSendCommand(_ printer: PMPrinter, _ commandString: CFString, _ jobTitle: CFString?, _ options: CFDictionary?) -> OSStatus
```

```c
OSStatus PMPrinterSendCommand(PMPrinter printer, CFStringRef commandString, CFStringRef jobTitle, CFDictionaryRef options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463872-pmprintersendcommand)*