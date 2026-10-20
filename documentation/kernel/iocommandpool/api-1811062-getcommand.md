# getCommand

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOCommand *getCommand(
 bool blockForCommand = true);
```

#### Return Value

If the caller passes true in blockForCommand, getCommand guarantees that the result will be a pointer to an IOCommand object from the pool. If the caller passes false, s/he is responsible for checking whether a non-NULL pointer was returned.

#### Overview

The getCommand method is used to get a pointer to an object of type IOCommand from the pool.

## Parameters

- `blockForCommand`: If the caller would like to have its thread slept until a command is available, it should pass true, else false.

## See Also

### Miscellaneous
- [commandPool](./api-1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](./api-1811028-gatedgetcommand.md)
- [gatedReturnCommand](./api-1811045-gatedreturncommand.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811062-getcommand)*