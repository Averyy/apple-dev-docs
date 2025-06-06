# highQualityDownsample

**Framework**: Core Image  
**Kind**: structdata

An option controlling the quality of image downsampling operations performed by the context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let highQualityDownsample: CIContextOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Boolean value. A value of [`true`](https://developer.apple.com/documentation/swift/true) (the default in macOS) results in higher image quality and lower performance. In iOS and tvOS, the default value is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/1437699-highqualitydownsample)*