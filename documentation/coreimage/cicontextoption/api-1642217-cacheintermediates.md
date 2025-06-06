# cacheIntermediates

**Framework**: Core Image  
**Kind**: structdata

An option for whether the context caches the contents of any intermediate pixel buffers it uses during rendering.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let cacheIntermediates: CIContextOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object containing a Boolean value. If this value is [`false`](https://developer.apple.com/documentation/swift/false), the context empties such buffers during and after renders. The default value is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/1642217-cacheintermediates)*