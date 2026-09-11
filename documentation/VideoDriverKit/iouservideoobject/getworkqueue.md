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

The work queue is used to synchronize access to the object’s state. Setters and Getters for the object will be done on the work queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/getworkqueue)*