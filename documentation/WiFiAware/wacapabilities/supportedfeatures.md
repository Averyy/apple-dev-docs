# supportedFeatures

**Framework**: Wi-Fi Aware  
**Kind**: property

A property that returns a set of supported features, or an empty set if the current platform doesn’t support Wi-Fi Aware.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static var supportedFeatures: Set<WACapabilities.Feature> { get }
```

#### Discussion

If the host device doesn’t support Wi-Fi Aware, the system returns an empty set. If a feature is present in the set, it’s supported, which you can test by using the code below:

```swift
let isSupported = WACapabilities.supportedFeatures.contains(feature)
```

## See Also

- [WACapabilities.Feature](wacapabilities/feature.md)
  Features that your app’s current host device can support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wacapabilities/supportedfeatures)*