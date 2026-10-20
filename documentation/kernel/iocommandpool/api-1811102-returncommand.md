# returnCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual void returnCommand(
 IOCommand *commmand);
```

#### Overview

The returnCommand method is used to place an object of type IOCommand into the pool, whether it be the first time, or the 1000th time.

## Parameters

- `commmand`: The command to place in the pool.

## See Also

### Miscellaneous
- [commandPool](./api-1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](./api-1811028-gatedgetcommand.md)
- [gatedReturnCommand](./api-1811045-gatedreturncommand.md)
- [getCommand](./api-1811062-getcommand.md)
- [init](./api-1811075-init.md)
  Should never be used, obsolete. See initWithWorkLoop.
- [initWithWorkLoop](./api-1811086-initwithworkloop.md)
  Primary initializer for an IOCommandPool object.
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](./api-1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](./api-1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811102-returncommand)*