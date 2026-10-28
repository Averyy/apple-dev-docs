# dispose

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Disposes of the current transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*dispose)(void *self);
```

## Return Value

Returns an IOReturn code.

## Discussion

The transaction will have to be recreated, in order to perform any operations on the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493382-dispose)*