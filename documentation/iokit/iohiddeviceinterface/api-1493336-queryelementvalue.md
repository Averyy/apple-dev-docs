# queryElementValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the current value of an element.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*queryElementValue)(void *self, IOHIDElementCookie elementCookie, IOHIDEventStruct *valueEvent, uint32_t timeoutMS, IOHIDElementCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

## Return Value

Returns an IOReturn code.

## Discussion

This call is most useful for feature type elements. This method will poll the device for the current element value.

## Parameters

- `elementCookie`: The element of interest.
- `valueEvent`: The event that will be filled. If a long value is present, it is up to the caller to deallocate it.
- `timeoutMS`: UNSUPPORTED.
- `callback`: UNSUPPORTED.
- `callbackTarget`: UNSUPPORTED.
- `callbackRefcon`: UNSUPPORTED.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493336-queryelementvalue)*