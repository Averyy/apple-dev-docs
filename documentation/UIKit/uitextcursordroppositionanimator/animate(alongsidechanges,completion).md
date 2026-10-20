# animate(alongsideChanges:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Optionally, provide an animation block or completion block to run alongside cursor appearance or position update animations.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func animate(alongsideChanges animation: (() -> Void)?, completion: (() -> Void)? = nil)
```

```swift
func animate(alongsideChanges animation: (() -> Void)?) async
```

```objc
- (void) animateAlongsideChanges:(void (^)()) animation completion:(void (^)()) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursordroppositionanimator/animate(alongsidechanges:completion:))*