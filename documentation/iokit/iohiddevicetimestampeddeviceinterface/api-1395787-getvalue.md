# getValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.10+

## Declaration

```c
IOReturn (*getValue)(void *self, IOHIDElementRef element, IOHIDValueRef *pValue, uint32_t timeout, IOHIDValueCallback callback, void *context, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetimestampeddeviceinterface/1395787-getvalue)*