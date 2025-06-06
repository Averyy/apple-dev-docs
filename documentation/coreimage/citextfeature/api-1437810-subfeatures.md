# subFeatures

**Framework**: Core Image  
**Kind**: instp

An array containing additional features detected within the feature.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var subFeatures: [Any]? { get }
```

#### Discussion

A text detector can identify both a major region that is likely to contain text as well as the areas within that region that likely to contain individual text features. Such features might be single characters, groups of closely-packed characters, or entire words.

Core Image populates this array only if you enable the [`CIDetectorReturnSubFeatures`](cidetectorreturnsubfeatures.md) option when retrieving features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citextfeature/1437810-subfeatures)*