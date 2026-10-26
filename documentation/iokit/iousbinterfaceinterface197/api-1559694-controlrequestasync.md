# ControlRequestAsync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*ControlRequestAsync)(void *self, UInt8 pipeRef, IOUSBDevRequest *req, IOAsyncCallback1 callback, void *refCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface197/1559694-controlrequestasync)*