# GetWorkQueue

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the work queue created by the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<IODispatchQueue> GetWorkQueue();
```

## Return Value

An OSSharedPtr to an IODispatchQueue on success

## Discussion

The work queue is used to synchronize access to the driver’s state. Setters and Getters for the driver will be done on the work queue.

## See Also

### Getting information about the class
- [GetClassID](./getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](./getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](../videodriverkit-page/iouservideoclassid.md)
  Video class identifiers of an video object.
- [GetName](./getname.md)
  Gets the name of the driver.
- [SetName](./setname.md)
  Sets the name of the video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/getworkqueue)*