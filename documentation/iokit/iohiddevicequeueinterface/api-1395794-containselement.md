# containsElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Determines whether an element has been added to this IOHIDDeviceQueueInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*containsElement)(void *self, IOHIDElementRef element, Boolean *pValue, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Parameters

- `self`: Pointer to the IOHIDDeviceQueueInterface.
- `element`: IOHIDElementRef referencing the element to be be found in the queue.
- `pValue`: Pointer to a Boolean to return whether or not the element was found in the queue.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicequeueinterface/1395794-containselement)*