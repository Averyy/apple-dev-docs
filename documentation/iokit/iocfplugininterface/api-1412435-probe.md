# Probe

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var Probe: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t, UnsafeMutablePointer<Int32>?) -> IOReturn)!
```

```c
IOReturn (*Probe)(void *thisPointer, CFDictionaryRef propertyTable, io_service_t service, SInt32 *order);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocfplugininterface/1412435-probe)*