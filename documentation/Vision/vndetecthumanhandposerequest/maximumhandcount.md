# maximumHandCount

**Framework**: Vision  
**Kind**: property

The maximum number of hands to detect in an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var maximumHandCount: Int { get set }
```

#### Discussion

The request orders detected hands by relative size, with only the largest ones having key points determined.

The default value is 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/maximumhandcount)*