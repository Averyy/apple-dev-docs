# GetUID

**Framework**: VideoDriverKit  
**Kind**: method

Gets the unique identifier of the video box.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<OSString> GetUID();
```

#### Return Value

An OSString unique identifier in an OSSharedPtr object.

#### Discussion

The object’s work queue synchronizes access to the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/getuid)*