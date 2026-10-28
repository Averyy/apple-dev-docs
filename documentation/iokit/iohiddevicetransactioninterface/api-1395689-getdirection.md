# getDirection

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the direction for this IOHIDDeviceTransactionInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*getDirection)(void *self, IOHIDTransactionDirectionType *pDirection);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Discussion

Direction constants are declared in IOHIDTransactionDirectionType.

## Parameters

- `self`: Pointer to the IOHIDDeviceTransactionInterface.
- `pDirection`: Pointer to a IOHIDTransactionDirectionType to obtain transaction direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetransactioninterface/1395689-getdirection)*