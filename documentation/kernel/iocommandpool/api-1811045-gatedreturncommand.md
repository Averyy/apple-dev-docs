# gatedReturnCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn gatedReturnCommand(
 IOCommand *vCommand);
```

#### Return Value

Always returns kIOReturnSuccess if the vCommand argument is valid.

#### Overview

The gatedReturnCommand method is used to serialize the return of a command to the pool behind a command gate, runAction-ed by returnCommand.

## Parameters

- `vCommand`: A pointer to the IOCommand object to be returned to the pool.

## See Also

### Miscellaneous
- [commandPool](./api-1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](./api-1811028-gatedgetcommand.md)
- [getCommand](./api-1811062-getcommand.md)
- [init](./api-1811075-init.md)
  Should never be used, obsolete. See initWithWorkLoop.
- [initWithWorkLoop](./api-1811086-initwithworkloop.md)
  Primary initializer for an IOCommandPool object.
- [returnCommand](./api-1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](./api-1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](./api-1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811045-gatedreturncommand)*