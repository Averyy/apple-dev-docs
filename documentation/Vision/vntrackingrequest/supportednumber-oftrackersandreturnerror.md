# supportedNumber(ofTrackersAndReturnError:)

**Framework**: Vision  
**Kind**: method

Returns the maximum number of simultaneous trackers for the request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func supportedNumber(ofTrackersAndReturnError error: NSErrorPointer) -> Int
```

#### Return Value

The maximum number of trackers given a combination; or `0` if such combination doesn’t exist.

## Parameters

- `error`: An error that contains the reason why a failure occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackingrequest/supportednumber(oftrackersandreturnerror:))*