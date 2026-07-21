# GetStartingChannel

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetStartingChannel();
```

#### Return Value

Returns a uint32_t that represents the starting channel of the stream.

#### Discussion

Get the starting channel of the IOUserVideoStream. Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetStartingChannel](iouservideostream/setstartingchannel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getstartingchannel)*