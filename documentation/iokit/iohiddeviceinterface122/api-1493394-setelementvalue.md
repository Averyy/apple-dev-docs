# setElementValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
IOReturn (*setElementValue)(void *self, IOHIDElementCookie elementCookie, IOHIDEventStruct *valueEvent, uint32_t timeoutMS, IOHIDElementCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface122/1493394-setelementvalue)*