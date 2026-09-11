# GetWorkQueue

**Framework**: VideoDriverKit  
**Kind**: method

Gets the work queue created by the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<IODispatchQueue> GetWorkQueue();
```

#### Return Value

An OSSharedPtr to an IODispatchQueue on success

#### Discussion

The work queue is used to synchronize access to the driver’s state. Setters and Getters for the driver will be done on the work queue.

## See Also

- [GetClassID](iouservideodriver/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideodriver/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
- [GetName](iouservideodriver/getname.md)
  Gets the name of the driver.
- [SetName](iouservideodriver/setname.md)
  Sets the name of the video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getworkqueue)*