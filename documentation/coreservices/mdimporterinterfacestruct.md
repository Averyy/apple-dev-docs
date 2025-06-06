# MDImporterInterfaceStruct

**Framework**: Core Services  
**Kind**: struct

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+
- Xcode 6.1+

## Declaration

```swift
struct MDImporterInterfaceStruct
```

## Topics

### Initializers
- [init()](mdimporterinterfacestruct/1443848-init.md)
- [init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!)](mdimporterinterfacestruct/1792094-init.md)
### Instance Properties
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](mdimporterinterfacestruct/1443912-addref.md)
- [var ImporterImportData: ((UnsafeMutableRawPointer?, CFMutableDictionary?, CFString?, CFString?) -> DarwinBoolean)!](mdimporterinterfacestruct/1444710-importerimportdata.md)
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](mdimporterinterfacestruct/1446572-queryinterface.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](mdimporterinterfacestruct/1441880-release.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdimporterinterfacestruct)*