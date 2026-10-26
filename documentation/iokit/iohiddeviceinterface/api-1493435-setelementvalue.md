# setElementValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets an element value on the device.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*setElementValue)(void *self, IOHIDElementCookie elementCookie, IOHIDEventStruct *valueEvent, uint32_t timeoutMS, IOHIDElementCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

This call is most useful for feature type elements. It is recommended to use IOOutputTransaction for output type elements.

## Parameters

- `elementCookie`: The element of interest.
- `valueEvent`: The event that will be filled. If a long value is present, it will be copied.
- `timeoutMS`: UNSUPPORTED.
- `callback`: UNSUPPORTED.
- `callbackTarget`: UNSUPPORTED.
- `callbackRefcon`: UNSUPPORTED.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493435-setelementvalue)*