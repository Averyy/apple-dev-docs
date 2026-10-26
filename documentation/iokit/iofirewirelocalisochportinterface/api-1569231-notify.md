# Notify

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
IOReturn (*Notify)(IOFireWireLibLocalIsochPortRef self, IOFWDCLNotificationType notificationType, void **inDCLList, UInt32 numDCLs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalisochportinterface/1569231-notify)*