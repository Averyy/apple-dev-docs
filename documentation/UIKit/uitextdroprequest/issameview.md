# isSameView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the drag and the drop are within the same text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isSameView: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSameView) BOOL sameView;
```

## See Also

### Getting information about the text drop request
- [var dropPosition: UITextPosition](./dropposition.md)
  The text position corresponding to the location of a drop session.
- [var suggestedProposal: UITextDropProposal](./suggestedproposal.md)
  The text drop proposal offered by the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdroprequest/issameview)*