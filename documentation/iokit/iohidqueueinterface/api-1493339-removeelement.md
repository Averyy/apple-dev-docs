# removeElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Removes an element from the queue.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*removeElement)(void *self, IOHIDElementCookie elementCookie);
```

## Return Value

Returns an IOReturn code.

## Discussion

If the element has not been added to queue, an error will be returned.

## Parameters

- `elementCookie`: The element of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493339-removeelement)*