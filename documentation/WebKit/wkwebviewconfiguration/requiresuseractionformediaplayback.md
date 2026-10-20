# requiresUserActionForMediaPlayback

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether HTML5 videos require the user to start playing them (`true`) or whether the videos play automatically (`false`).

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`mediaTypesRequiringUserActionForPlayback`](./mediatypesrequiringuseractionforplayback.md) instead.

## Declaration

```swift
var requiresUserActionForMediaPlayback: Bool { get set }
```

```objc
@property (nonatomic) BOOL requiresUserActionForMediaPlayback;
```

## See Also

### Deprecated
- [var mediaPlaybackAllowsAirPlay: Bool](./mediaplaybackallowsairplay.md)
  Deprecated property.
- [var mediaPlaybackRequiresUserAction: Bool](./mediaplaybackrequiresuseraction.md)
  Deprecated property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/requiresuseractionformediaplayback)*