# GetUID

**Framework**: VideoDriverKit  
**Kind**: method

Gets the unique identifier of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<OSString> GetUID();
```

#### Return Value

The unique identifier.

#### Discussion

The object’s work queue synchronizes access to the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getuid)*