# init(configuration:)

**Framework**: WebKit  
**Kind**: init

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(configuration: WKContentWorld.Configuration)
```

#### Discussion

Creates a world with the given WKContentWorldConfiguration

Unlike all other worlds, worlds created with this factory method cannot be retrieved later. Clients therefore need to take care to reference them for as long as they are needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/init(configuration:))*