# identifier

**Framework**: Vision  
**Kind**: property

Classification label identifying the type of observation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

An example classification could be a string like `cat` or `hotdog`.  The model used for the classification defines the domain of strings that may result.  Usually, these strings are unlocalized technical labels not meant for direct presentation to the end user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassificationobservation/identifier)*