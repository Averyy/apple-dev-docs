# withWorkLoop(IOWorkLoop *)

**Framework**: Kernel  
**Kind**: instm

Primary factory method for the IOCommandPool class

## Declaration

```c
static IOCommandPool *withWorkLoop(
 IOWorkLoop *inWorkLoop);
```

#### Return Value

Returns a pointer to an instance of IOCommandPool if successful, otherwise NULL.

#### Overview

The withWorkLoop method is what is known as a factory method. It creates a new instance of an IOCommandPool and returns a pointer to that object.

## Parameters

- `inWorkLoop`: The workloop that this command pool should synchronize with.

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
- [returnCommand](./api-1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](./api-1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811136-withworkloop)*