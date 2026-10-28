# clear

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Clears the transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*clear)(void *self);
```

## Return Value

Returns an IOReturn code.

## Discussion

Transaction element values will cleared. Default values will be preserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493331-clear)*