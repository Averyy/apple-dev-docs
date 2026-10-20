# withWorkLoop(IOService *, IOWorkLoop *, UInt32)

**Framework**: Kernel  
**Kind**: instm

Should never be used, obsolete. See IOCommandPool::withWorkLoop.

## Declaration

```c
static IOCommandPool *commandPool(
 IOService *inOwner, 
 IOWorkLoop *inWorkLoop, 
 UInt32 inSize = kIOCommandPoolDefaultSize);
```

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
- [withWorkLoop(IOWorkLoop *)](./api-1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool/1811120-withworkloop)*