# getElementDefault

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the default value of an element in a transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*getElementDefault)(void *self, IOHIDElementCookie elementCookie, IOHIDEventStruct *outValueEvent);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

An error will be returned if the element has not been added to the transaction.

## Parameters

- `elementCookie`: The element of interest.
- `outValueEvent`: The event that will be filled. If a long value is present, it is up to the caller to deallocate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493363-getelementdefault)*