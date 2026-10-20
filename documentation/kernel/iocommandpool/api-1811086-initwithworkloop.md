# initWithWorkLoop

**Framework**: Kernel  
**Kind**: instm

Primary initializer for an IOCommandPool object.

## Declaration

```cpp
virtual bool initWithWorkLoop(
 IOWorkLoop *inWorkLoop);
```

#### Return Value

Returns true if command pool was successfully initialized.

#### Overview

Primary initializer for an IOCommandPool. Should probably use IOCommandPool::withWorkLoop() as it is easier to use.

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
- [returnCommand](./api-1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](./api-1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](./api-1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811086-initwithworkloop)*