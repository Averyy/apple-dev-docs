# clear

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Clears element transaction values for an IOHIDDeviceTransactionInterface.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*clear)(void *self, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

#### Discussion

In regards to kIOHIDTransactionDirectionTypeOutput direction, default element values will be preserved.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395709-clear)*