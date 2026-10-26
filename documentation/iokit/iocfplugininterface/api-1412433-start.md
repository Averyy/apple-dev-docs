# Start

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var Start: ((UnsafeMutableRawPointer?, CFDictionary?, io_service_t) -> IOReturn)!
```

```c
IOReturn (*Start)(void *thisPointer, CFDictionaryRef propertyTable, io_service_t service);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocfplugininterface/1412433-start)*