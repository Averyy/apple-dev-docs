# world(with:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class func world(with configuration: WKContentWorldConfiguration) -> WKContentWorld
```

#### Discussion

Creates a world with the given WKContentWorldConfiguration

Unlike all other worlds, worlds created with this factory method cannot be retrieved later. Clients therefore need to take care to reference them for as long as they are needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/world(with:))*