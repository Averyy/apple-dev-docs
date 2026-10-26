# hasElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Checks whether an element has been added to the queue.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
Boolean (*hasElement)(void *self, IOHIDElementCookie elementCookie);
```

#### Return Value

Returns a Boolean value.

#### Discussion

Will return true if present, otherwise will return false.

## Parameters

- `elementCookie`: The element of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493401-haselement)*