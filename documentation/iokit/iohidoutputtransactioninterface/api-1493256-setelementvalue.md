# setElementValue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the value of an element in a transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*setElementValue)(void *self, IOHIDElementCookie elementCookie, IOHIDEventStruct *valueEvent);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

An error will be returned if the element has not been added to the transaction.

## Parameters

- `elementCookie`: The element of interest.
- `valueEvent`: The event that will be filled. If a long value is present, it will be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493256-setelementvalue)*