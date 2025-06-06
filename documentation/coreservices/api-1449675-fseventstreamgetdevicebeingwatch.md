# FSEventStreamGetDeviceBeingWatched(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamGetDeviceBeingWatched(_ streamRef: ConstFSEventStreamRef) -> dev_t
```

#### Return_value

The dev_t for a device-relative stream, otherwise 0.

#### Discussion

Fetches the dev_t supplied when the stream was created via FSEventStreamCreateRelativeToDevice(), otherwise 0.

## Parameters

- `streamRef`: A valid stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449675-fseventstreamgetdevicebeingwatch)*