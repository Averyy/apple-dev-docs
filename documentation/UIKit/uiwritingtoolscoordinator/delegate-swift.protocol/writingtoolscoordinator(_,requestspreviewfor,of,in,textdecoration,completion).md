# writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, requestsPreviewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, of range: NSRange, in context: UIWritingToolsCoordinator.Context, textDecoration: UIWritingToolsCoordinator.TextDecoration, completion: @escaping @Sendable (UITargetedPreview?) -> Void)
```

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, previewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, range: NSRange, context: UIWritingToolsCoordinator.Context, textDecoration: UIWritingToolsCoordinator.TextDecoration) async -> UITargetedPreview?
```

```objc
- (void) writingToolsCoordinator:(UIWritingToolsCoordinator *) writingToolsCoordinator requestsPreviewForTextAnimation:(UIWritingToolsCoordinatorTextAnimation) textAnimation ofRange:(NSRange) range inContext:(UIWritingToolsCoordinatorContext *) context textDecoration:(UIWritingToolsCoordinatorTextDecoration) textDecoration completion:(void (^)(UITargetedPreview *)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:textdecoration:completion:))*