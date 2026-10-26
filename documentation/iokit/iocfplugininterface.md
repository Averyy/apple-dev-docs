# IOCFPlugInInterfaceStruct

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias IOCFPlugInInterface = IOCFPlugInInterfaceStruct
```

```swift
struct IOCFPlugInInterfaceStruct
```

```c
typedef struct IOCFPlugInInterfaceStruct {
    ...
} IOCFPlugInInterface;
```

## Topics

### Initializers
- [init()](./iocfplugininterfacestruct/api-1514869-init.md)
- [init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!, Release: ((UnsafeMutableRawPointer?) -> ULONG)!, version: UInt16, revision: UInt16, Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!, Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!, Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!)](./iocfplugininterfacestruct/api-1792000-init.md)
### Instance Properties
- [var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!](./iocfplugininterfacestruct/api-1412440-addref.md)
- [var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!](./iocfplugininterfacestruct/api-1412435-probe.md)
- [var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!](./iocfplugininterfacestruct/api-1412423-queryinterface.md)
- [var Release: ((UnsafeMutableRawPointer?) -> ULONG)!](./iocfplugininterfacestruct/api-1412422-release.md)
- [var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!](./iocfplugininterfacestruct/api-1412433-start.md)
- [var Stop: ((UnsafeMutableRawPointer?) -> IOReturn)!](./iocfplugininterfacestruct/api-1412438-stop.md)
- [var revision: UInt16](./iocfplugininterfacestruct/api-1412427-revision.md)
- [var version: UInt16](./iocfplugininterfacestruct/api-1412436-version.md)
- [AddRef](./iocfplugininterface/api-1412440-addref.md)
- [Probe](./iocfplugininterface/api-1412435-probe.md)
- [QueryInterface](./iocfplugininterface/api-1412423-queryinterface.md)
- [Release](./iocfplugininterface/api-1412422-release.md)
- [Start](./iocfplugininterface/api-1412433-start.md)
- [Stop](./iocfplugininterface/api-1412438-stop.md)
- [revision](./iocfplugininterface/api-1412427-revision.md)
- [version](./iocfplugininterface/api-1412436-version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocfplugininterface)*