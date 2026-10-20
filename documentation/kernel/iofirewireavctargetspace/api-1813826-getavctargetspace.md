# getAVCTargetSpace

**Framework**: Kernel  
**Kind**: instm

returns the IOFireWireAVCTargetSpace object for the given FireWire bus

## Declaration

```c
static IOFireWireAVCTargetSpace *getAVCTargetSpace(
 IOFireWireController *bus);
```

## Parameters

- `bus`: The FireWire bus

## See Also

### Miscellaneous
- [init](./api-1813830-init.md)
  initializes the IOFireWireAVCTargetSpace object
- [publishAVCUnitDirectory](./api-1813834-publishavcunitdirectory.md)
  Creates a local AVC Unit directory if it doesn't already exist


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavctargetspace/1813826-getavctargetspace)*