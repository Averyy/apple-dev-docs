# init

**Framework**: VideoDriverKit  
**Kind**: method

Initializes a video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_video_driver);
```

#### Return Value

True on success.

#### Discussion

Always pass in the `IOUserVideoDriver`; calling `init()` always returns false.

## Parameters

- `in_video_driver`: The IOUserVideoDriver that owns this object.

## See Also

- [init](iouservideoobject/init-853a8.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/init-5dkv4)*