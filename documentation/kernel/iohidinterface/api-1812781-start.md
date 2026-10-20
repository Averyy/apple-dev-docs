# start

**Framework**: Kernel  
**Kind**: instm

Start up the driver using the given provider.

## Declaration

```cpp
virtual bool start(
 IOService *provider );
```

#### Return Value

True on success, or false otherwise.

#### Overview

IOHIDInterface will allocate resources. Before returning true to indicate success, registerService() is called to trigger client matching.

## Parameters

- `provider`: The provider that the driver was matched to, and selected to run with.

## See Also

### Miscellaneous
- [free](./api-1812725-free.md)
  Free the IOHIDInterface object.
- [init](./api-1812739-init.md)
  Initialize an IOHIDInterface object.
- [matchPropertyTable](./api-1812756-matchpropertytable.md)
  Called by the provider during a match


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidinterface/1812781-start)*