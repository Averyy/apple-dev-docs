# OSSerializerCallback

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef bool (*OSSerializerCallback)(void *target, void *ref, OSSerialize *serializer);
```

## See Also

- [OSActionAbortedHandler](osactionabortedhandler.md)
- [OSActionCancelHandler](osactioncancelhandler.md)
- [OSDispatchMethod](osdispatchmethod.md)
- [OSKextRequestResourceCallback](oskextrequestresourcecallback.md)
  Invoked to provide results for a kext resource request.
- [OSObjectApplierFunction](osobjectapplierfunction.md)
- [OSSerializerBlock](osserializerblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osserializercallback)*