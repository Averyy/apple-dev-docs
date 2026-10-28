# scrollingAndDecelerationMetric

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

A metric that records scroll-dragging and deceleration animations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class var scrollingAndDecelerationMetric: any XCTMetric { get }
```

```objc
@property (class, readonly) id<XCTMetric> scrollingAndDecelerationMetric;
```

## Discussion

In a compatible iPad or iPhone app running in visionOS, the system doesn’t report hitch- or animation-related metrics that occur during scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/scrollinganddecelerationmetric)*