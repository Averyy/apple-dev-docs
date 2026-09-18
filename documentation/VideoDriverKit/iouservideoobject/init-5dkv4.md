# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_video_driver);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoObject.

Always pass in the IOUserVideoDriver.  init() will always return false;

## Parameters

- `in_video_driver`: The IOUserVideoDriver that owns this object.

## See Also

- [init](iouservideoobject/init-853a8.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/init-5dkv4)*