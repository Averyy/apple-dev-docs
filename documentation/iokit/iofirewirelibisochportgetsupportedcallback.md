# IOFireWireLibIsochPortGetSupportedCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
typedef IOReturn (*IOFireWireLibIsochPortGetSupportedCallback)(IOFireWireLibIsochPortRef interface, IOFWSpeed *outMaxSpeed, UInt64 *outChanSupported);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibisochportgetsupportedcallback)*