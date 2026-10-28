# commit

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Commits the transaction.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*commit)(void *self, uint32_t timeoutMS, IOHIDCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

## Return Value

Returns an IOReturn code.

## Discussion

Transaction element values, if set, will be sent to the device. Otherwise, the default element value will be used. If neither are set, that element will be omitted from the commit. After a transaction is committed, transaction element values will be cleared. Default values will be preserved.

## Parameters

- `timeoutMS`: UNSUPPORTED
- `callback`: UNSUPPORTED
- `callbackTarget`: UNSUPPORTED
- `callbackRefcon`: UNSUPPORTED


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493426-commit)*