# IOCFPlugInInterfaceStruct

**Framework**: IOKit  
**Kind**: tdef

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct IOCFPlugInInterfaceStruct
```

## Topics

### Initializers
- [init()](iocfplugininterfacestruct/1514869-init.md)
- [init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, version: UInt16, revision: UInt16, Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!)](iocfplugininterfacestruct/1792000-init.md)
### Instance Properties
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](iocfplugininterfacestruct/1412440-addref.md)
- [var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!](iocfplugininterfacestruct/1412435-probe.md)
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](iocfplugininterfacestruct/1412423-queryinterface.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](iocfplugininterfacestruct/1412422-release.md)
- [var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!](iocfplugininterfacestruct/1412433-start.md)
- [var Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!](iocfplugininterfacestruct/1412438-stop.md)
- [var revision: UInt16](iocfplugininterfacestruct/1412427-revision.md)
- [var version: UInt16](iocfplugininterfacestruct/1412436-version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocfplugininterfacestruct)*