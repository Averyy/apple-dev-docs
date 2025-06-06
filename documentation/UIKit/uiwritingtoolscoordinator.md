# UIWritingToolsCoordinator

**Framework**: UIKit  
**Kind**: class

An object that manages interactions between Writing Tools and your custom text view.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class UIWritingToolsCoordinator
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Overview

Add a `UIWritingToolsCoordinator` object to a custom view when you want to add Writing Tools support to that view. The coordinator manages interactions between your view and the Writing Tools UI and back-end capabilities. When creating a coordinator, you supply a delegate object to respond to requests from the system and provide needed information. Your delegate delivers your view’s text to Writing Tools, incorporates suggested changes back into your text storage, and supports the animations that Writing Tools creates to show the state of an operation.

Create the `UIWritingToolsCoordinator` object when setting up your UI, and initialize it with a custom object that adopts the [`UIWritingToolsCoordinator.Delegate`](uiwritingtoolscoordinator/delegate-swift.protocol.md) protocol. Add the coordinator to your view using the [`addInteraction(_:)`](uiview/addinteraction(_:).md) method. When a coordinator is present on a view, the system adds UI elements to initiate Writing Tools operations.

When defining the delegate, choose an object from your app that has access to your view and its text storage. You can adopt the [`UIWritingToolsCoordinator.Delegate`](uiwritingtoolscoordinator/delegate-swift.protocol.md) protocol in the view itself, or in another type that your view uses to manage content. During the interactions with Writing Tools, the delegate gets and sets the contents of the view’s text storage and supports Writing Tools behaviors.

> **Note**: You don’t need to create an `UIWritingToolsCoordinator`  object if you display text using a [`UITextView`](uitextview.md), [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView), [`Text`](https://developer.apple.com/documentation/SwiftUI/Text), [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField), or [`TextEditor`](https://developer.apple.com/documentation/SwiftUI/TextEditor) view. Those views already include the required support to handle Writing Tools interactions.

You don’t need to create an `UIWritingToolsCoordinator`  object if you display text using a [`UITextView`](uitextview.md), [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView), [`Text`](https://developer.apple.com/documentation/SwiftUI/Text), [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField), or [`TextEditor`](https://developer.apple.com/documentation/SwiftUI/TextEditor) view. Those views already include the required support to handle Writing Tools interactions.

## Topics

### Creating a coordinator object
- [init(delegate: (any UIWritingToolsCoordinator.Delegate)?)](uiwritingtoolscoordinator/init(delegate:).md)
  Creates a writing tools coordinator and assigns the specified delegate object to it.
### Checking the availability of Writing Tools
- [class var isWritingToolsAvailable: Bool](uiwritingtoolscoordinator/iswritingtoolsavailable.md)
  A Boolean value that indicates whether Writing Tools features are currently available.
### Managing Writing Tools interactions
- [var delegate: (any UIWritingToolsCoordinator.Delegate)?](uiwritingtoolscoordinator/delegate-swift.property.md)
  The object that handles Writing Tools interactions for your view.
- [UIWritingToolsCoordinator.Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
### Getting the host views for effects
- [var effectContainerView: UIView?](uiwritingtoolscoordinator/effectcontainerview.md)
  The view that Writing Tools uses to display visual effects during the text-rewriting process.
- [var decorationContainerView: UIView?](uiwritingtoolscoordinator/decorationcontainerview.md)
  The view that Writing Tools uses to display background decorations such as proofreading marks.
### Configuring the experience
- [var preferredBehavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/preferredbehavior.md)
  The level of Writing Tools support you want the system to provide for your view.
- [var behavior: UIWritingToolsBehavior](uiwritingtoolscoordinator/behavior.md)
  The actual level of Writing Tools support the system provides for your view.
- [var preferredResultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/preferredresultoptions.md)
  The type of content you allow Writing Tools to generate for your custom text view.
- [var resultOptions: UIWritingToolsResultOptions](uiwritingtoolscoordinator/resultoptions.md)
  The type of content the system generates for your custom text view.
### Reporting changes to Writing Tools
- [func updateRange(NSRange, with: NSAttributedString, reason: UIWritingToolsCoordinator.TextUpdateReason, forContextWithIdentifier: UUID)](uiwritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md)
  Informs the coordinator about changes your app made to the text in the specified context object.
- [func updateForReflowedTextInContextWithIdentifier(UUID)](uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:).md)
  Informs the coordinator that a change occurred to the view or its text that requires a layout update.
- [UIWritingToolsCoordinator.TextUpdateReason](uiwritingtoolscoordinator/textupdatereason.md)
  Constants that specify the reason you updated your view’s content outside of the Writing Tools workflow.
### Managing the current state
- [func stopWritingTools()](uiwritingtoolscoordinator/stopwritingtools.md)
  Stops the current Writing Tools operation and dismisses the system UI.
- [var state: UIWritingToolsCoordinator.State](uiwritingtoolscoordinator/state-swift.property.md)
  The current level of Writing Tools activity in your view.
- [UIWritingToolsCoordinator.State](uiwritingtoolscoordinator/state-swift.enum.md)
  The states that indicate the current activity, if any, Writing Tools is performing in your view.
### Getting the supporting types
- [UIWritingToolsCoordinator.ContextScope](uiwritingtoolscoordinator/contextscope.md)
  Options that indicate how much of your content Writing Tools requested.
- [UIWritingToolsCoordinator.TextReplacementReason](uiwritingtoolscoordinator/textreplacementreason.md)
  Options that indicate whether Writing Tools is animating changes to your view’s text.
- [UIWritingToolsCoordinator.TextAnimation](uiwritingtoolscoordinator/textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)
  Add Writing Tools support, including support for inline replacement animations, to your custom iOS views that contain text.
- [UIWritingToolsCoordinator.Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
- [UIWritingToolsCoordinator.Context](uiwritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.
- [UIWritingToolsCoordinator.AnimationParameters](uiwritingtoolscoordinator/animationparameters.md)
  An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator)*