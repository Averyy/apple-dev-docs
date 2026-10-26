# addElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Adds an element to the transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*addElement)(void *self, IOHIDElementCookie elementCookie);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

If the element has already been added to transaction, an error will be returned.

## Parameters

- `elementCookie`: The element of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493297-addelement)*