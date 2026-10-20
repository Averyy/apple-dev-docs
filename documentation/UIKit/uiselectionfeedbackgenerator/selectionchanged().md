# selectionChanged()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Triggers selection feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func selectionChanged()
```

```objc
- (void) selectionChanged;
```

#### Discussion

This method tells the generator that the user has changed a selection. In response, the generator may play the appropriate haptics. Don’t use this feedback when the user makes or confirms a selection; use it only when the selection changes.

For information on setting up a feedback generator, see the [`UIFeedbackGenerator`](../uifeedbackgenerator.md) class.

## See Also

### Related Documentation
- [func prepare()](../uifeedbackgenerator/prepare%28%29.md)
  Prepares the generator to trigger feedback.
### Reporting selection changes
- [func selectionChanged(at: CGPoint)](./selectionchanged%28at%29.md)
  Triggers selection feedback at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiselectionfeedbackgenerator/selectionchanged())*