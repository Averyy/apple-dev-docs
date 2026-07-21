# GetUID

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<OSString> GetUID();
```

#### Return Value

Returns an OSSharedPtr to an OSString

#### Discussion

Get the unique identifier of the clock device

Getting the value will be synchronized using the work queue created by the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getuid)*