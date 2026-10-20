# IOCreatePlugInInterfaceForService(_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func IOCreatePlugInInterfaceForService(_ service: io_service_t, _ pluginType: CFUUID!, _ interfaceType: CFUUID!, _ theInterface: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<IOCFPlugInInterface>?>?>!, _ theScore: UnsafeMutablePointer<Int32>!) -> kern_return_t
```

```c
kern_return_t IOCreatePlugInInterfaceForService(io_service_t service, CFUUIDRef pluginType, CFUUIDRef interfaceType, IOCFPlugInInterface ***theInterface, SInt32 *theScore);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1412429-iocreateplugininterfaceforservic)*