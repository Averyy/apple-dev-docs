# GetName

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<OSString> GetName();
```

#### Return Value

Returns an OSSharedPtr to an OSString

#### Discussion

Get the name of the IOUserVideoObject. Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetName](iouservideoobject/setname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/getname)*