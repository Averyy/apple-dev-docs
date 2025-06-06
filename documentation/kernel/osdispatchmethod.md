# OSDispatchMethod

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.15+

## Declaration

```swift
typedef kern_return_t (*OSDispatchMethod)(OSMetaClassBase *self, const IORPC rpc);
```

## See Also

- [OSActionAbortedHandler](osactionabortedhandler.md)
- [OSActionCancelHandler](osactioncancelhandler.md)
- [OSKextRequestResourceCallback](oskextrequestresourcecallback.md)
  Invoked to provide results for a kext resource request.
- [OSObjectApplierFunction](osobjectapplierfunction.md)
- [OSSerializerBlock](osserializerblock.md)
- [OSSerializerCallback](osserializercallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdispatchmethod)*