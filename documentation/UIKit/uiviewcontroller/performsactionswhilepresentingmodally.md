# performsActionsWhilePresentingModally

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view controller performs menu-related actions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var performsActionsWhilePresentingModally: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL performsActionsWhilePresentingModally;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which causes the view controller to handle actions passed along the responder chain by modally presented view controllers. If the app includes the `UIViewControllerPerformsActionsWhilePresentingModally` key in its `Info.plist` file, the default value matches the value of that key instead.

A presenting view controller might not want to handle actions in one of its modally presented child view controllers. Overriding this property and returning [`false`](../../Swift/false.md) causes UIKit to ignore this view controller when searching for a target to handle actions.

## See Also

### Accessing the available key commands
- [func addKeyCommand(UIKeyCommand)](./addkeycommand%28_%29.md)
  Associates the specified keyboard shortcut with the view controller.
- [func removeKeyCommand(UIKeyCommand)](./removekeycommand%28_%29.md)
  Removes the key command from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/performsactionswhilepresentingmodally)*