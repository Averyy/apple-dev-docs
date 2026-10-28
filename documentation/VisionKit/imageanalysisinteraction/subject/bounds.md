# bounds

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

A rectangle that identifies the extremities of a subject within an image in relation to the interaction view’s bounds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var bounds: CGRect { get }
```

## Discussion

This property will always return `CGRect.zero` if the interaction isn’t added to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subject/bounds)*