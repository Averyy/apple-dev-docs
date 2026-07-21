# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_acquirable, OSString *in_box_uid);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoBox.

Always pass in the IOUserVideoDriver and arguments.  init() will always return false;

## Parameters

- `in_is_acquirable`: Bool value
- `in_box_uid`: An OSString pointer for the box unique identifier

## See Also

- [Create](iouservideobox/create.md)
- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/init)*