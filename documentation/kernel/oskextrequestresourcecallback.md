# OSKextRequestResourceCallback

**Framework**: Kernel  
**Kind**: tdef

Invoked to provide results for a kext resource request.

**Availability**:
- macOS 10.6+

## Declaration

```swift
typedef void (*OSKextRequestResourceCallback)(OSKextRequestTag requestTag, OSReturn result, const void *resourceData, uint32_t resourceDataLength, void *context);
```

## Parameters

- `requestTag`: The tag of the request that the callback pertains to.
- `result`: The result of the request:   if the request was fulfilled;   if the request has timed out;   if the kext containing the callback address for the kext is being unloaded; or other values on error.
- `resourceData`: A pointer to the requested resource data. Owned by the system; the kext should make a copy if it needs to keep the data past the callback.
- `resourceDataLength`: The length of  .
- `context`: The context pointer originally passed to  .

## See Also

- [OSActionAbortedHandler](osactionabortedhandler.md)
- [OSActionCancelHandler](osactioncancelhandler.md)
- [OSDispatchMethod](osdispatchmethod.md)
- [OSObjectApplierFunction](osobjectapplierfunction.md)
- [OSSerializerBlock](osserializerblock.md)
- [OSSerializerCallback](osserializercallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oskextrequestresourcecallback)*