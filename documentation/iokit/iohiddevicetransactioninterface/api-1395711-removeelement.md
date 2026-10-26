# removeElement

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Removes an element from this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*removeElement)(void *self, IOHIDElementRef element, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `element`: IOHIDElementRef referencing the element to be removed from the transaction.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395711-removeelement)*