# getElementValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the most recent value of an element.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*getElementValue)(void *self, IOHIDElementCookie elementCookie, IOHIDEventStruct *valueEvent);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

This call is most useful for interrupt driven elements, such as input type elements. Since feature type element values need to be polled from the device, it is recommended to use the queryElementValue method to obtain the current value. The timestamp field in the event details the last time the element value was altered.

## Parameters

- `elementCookie`: The element of interest.
- `valueEvent`: The event that will be filled. If a long value is present, it is up to the caller to deallocate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493342-getelementvalue)*