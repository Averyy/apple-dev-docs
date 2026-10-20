# MDExporterInterfaceStruct

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

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
- [init()](./mdexporterinterfacestruct/api-1446815-init.md)
- [init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](./mdexporterinterfacestruct/api-1792091-init.md)
### Instance Properties
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](./mdexporterinterfacestruct/api-1449918-addref.md)
- [var ImporterExportData: ((UnsafeMutableRawPointer?, CFDictionary?, CFString?, CFString?) -> DarwinBoolean)!](./mdexporterinterfacestruct/api-1446348-importerexportdata.md)
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](./mdexporterinterfacestruct/api-1450043-queryinterface.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](./mdexporterinterfacestruct/api-1448271-release.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdexporterinterfacestruct)*