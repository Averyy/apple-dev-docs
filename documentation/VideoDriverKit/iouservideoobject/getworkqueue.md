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

The work queue is used to synchronize access to the object’s state.  Setters and Getters for the object will be done on the work queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/getworkqueue)*