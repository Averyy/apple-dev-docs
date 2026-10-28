# cancelTextAnimations(identifiers:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
func cancelTextAnimations(identifiers: [UUID])
```

```objc
- (void) cancelTextAnimationsWithIdentifiers:(NSArray<NSUUID *> *) identifiers;
```

## Discussion

The UUIDs passed in should be those returned when starting the animations. To cancel all ahimations, use [`stopWritingTools()`](./stopwritingtools%28%29.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/canceltextanimations(identifiers:))*