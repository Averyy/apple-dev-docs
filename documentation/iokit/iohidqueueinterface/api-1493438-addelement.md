# addElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Adds an element to the queue.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*addElement)(void *self, IOHIDElementCookie elementCookie, uint32_t flags);
```

## Return Value

Returns an IOReturn code.

## Discussion

If the element has already been added to queue, an error will be returned.

## Parameters

- `elementCookie`: The element of interest.
- `flags`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493438-addelement)*