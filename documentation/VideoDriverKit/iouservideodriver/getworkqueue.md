# GetWorkQueue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IODispatchQueue> GetWorkQueue();
```

#### Return Value

Returns an OSSharedPtr to an IODispatchQueue on success

#### Discussion

Gets the work queue created by the IOUserVideoObject in an OSSharedPtr.

The work queue is used to synchronize access to the driver’s state.  Setters and Getters for the driver will be done on the work queue.

## See Also

- [GetClassID](iouservideodriver/getclassid.md)
- [GetBaseClassID](iouservideodriver/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
- [GetName](iouservideodriver/getname.md)
- [SetName](iouservideodriver/setname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getworkqueue)*