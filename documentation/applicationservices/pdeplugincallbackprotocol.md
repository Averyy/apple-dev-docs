# PDEPlugInCallbackProtocol

**Framework**: Application Services  
**Kind**: intf  
**Role**: Protocol

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol PDEPlugInCallbackProtocol
```

```objc
@protocol PDEPlugInCallbackProtocol
```

## Topics

### Instance Methods
- [func pageFormat() -> PMPageFormat?](./pdeplugincallbackprotocol/api-3930837-pageformat.md)
- [func pmPrinter() -> PMPrinter](./pdeplugincallbackprotocol/api-3930838-pmprinter.md)
- [func ppdFile() -> UnsafeMutablePointer<ppd_file_s>?](./pdeplugincallbackprotocol/api-3930839-ppdfile.md)
- [func printSession() -> PMPrintSession?](./pdeplugincallbackprotocol/api-3930840-printsession.md)
- [func printSettings() -> PMPrintSettings?](./pdeplugincallbackprotocol/api-3930841-printsettings.md)
- [func willChangePPDOptionKeyValue(String, ppdChoice: String) -> Bool](./pdeplugincallbackprotocol/api-3930842-willchangeppdoptionkeyvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pdeplugincallbackprotocol)*