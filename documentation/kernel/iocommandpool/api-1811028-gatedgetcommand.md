# gatedGetCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn gatedGetCommand(
 IOCommand **vCommand,
 boolvBlock);
```

#### Return Value

Returns kIOReturnNoResources if no command is available and the client doesn't wish to block until one does become available. kIOReturnSuccess if the vCommand argument is valid.

#### Overview

The gatedGetCommand method is used to serialize the extraction of a command from the pool behind a command gate, runAction-ed by getCommand.

## Parameters

- `vCommand`: A pointer to a pointer to an IOCommand object where the returned command will be stored.
- `vBlock`: A bool that indicates whether to block the request until a command becomes available.

## See Also

### Miscellaneous
- [commandPool](./api-1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedReturnCommand](./api-1811045-gatedreturncommand.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811028-gatedgetcommand)*