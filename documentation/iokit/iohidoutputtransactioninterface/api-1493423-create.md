# create

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates the current transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*create)(void *self);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

This method will free any memory that has been allocated for this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493423-create)*