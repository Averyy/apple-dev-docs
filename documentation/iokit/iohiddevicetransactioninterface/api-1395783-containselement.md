# containsElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Checks whether an element has been added to this IOHIDDeviceTransactionInterface instance.

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

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `element`: IOHIDElementRef referencing the element to be be found in the transaction.
- `pValue`: Pointer to a Boolean to return whether or not the element was found in the transaction.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395783-containselement)*