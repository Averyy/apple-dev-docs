# MDExporterInterfaceStruct

**Framework**: Core Services  
**Kind**: struct

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+
- Xcode 6.1+

## Declaration

```swift
struct MDExporterInterfaceStruct
```

## Topics

### Initializers
- [init()](mdexporterinterfacestruct/1446815-init.md)
- [init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](mdexporterinterfacestruct/1792091-init.md)
### Instance Properties
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](mdexporterinterfacestruct/1449918-addref.md)
- [var ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!](mdexporterinterfacestruct/1446348-importerexportdata.md)
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](mdexporterinterfacestruct/1450043-queryinterface.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](mdexporterinterfacestruct/1448271-release.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct)*