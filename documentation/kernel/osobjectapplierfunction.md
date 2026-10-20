# OSObjectApplierFunction

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef void (*OSObjectApplierFunction)(OSObject *object, void *context);
```

## See Also

### Callback Methods
- [OSActionAbortedHandler](./osactionabortedhandler.md)
- [OSActionCancelHandler](./osactioncancelhandler.md)
- [OSDispatchMethod](./osdispatchmethod.md)
- [OSKextRequestResourceCallback](./oskextrequestresourcecallback.md)
  Invoked to provide results for a kext resource request.
- [OSSerializerBlock](./osserializerblock.md)
- [OSSerializerCallback](./osserializercallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobjectapplierfunction)*