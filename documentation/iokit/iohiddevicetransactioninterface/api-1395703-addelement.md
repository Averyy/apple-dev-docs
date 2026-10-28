# addElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Adds an element to this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*addElement)(void *self, IOHIDElementRef element, IOOptionBits options);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `element`: IOHIDElementRef referencing the element to be added to the transaction.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395703-addelement)*