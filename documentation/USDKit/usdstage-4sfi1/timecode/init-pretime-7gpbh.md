# init(preTime:)

**Framework**: USDKit  
**Kind**: init

The instant directly before the given time value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(preTime instant: Double)
```

#### Discussion

If a time-varying value is discontinuous at `instant`, pre-time refers to the value’s limit approaching from the left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/timecode/init(pretime:)-7gpbh)*