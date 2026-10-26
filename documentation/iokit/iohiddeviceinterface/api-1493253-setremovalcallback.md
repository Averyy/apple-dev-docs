# setRemovalCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets callback to be used when device is removed.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*setRemovalCallback)(void *self, IOHIDCallbackFunction removalCallback, void *removalTarget, void *removalRefcon);
```

#### Return Value

Returns an IOReturn code.

## Parameters

- `removalCallback`: Called when the device is removed.
- `removalTarget`: Passed to the callback.
- `removalRefcon`: Passed to the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493253-setremovalcallback)*