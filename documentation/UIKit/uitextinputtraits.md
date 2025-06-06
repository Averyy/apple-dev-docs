# UITextInputTraits

**Framework**: UIKit  
**Kind**: protocol

A set of methods that defines features for keyboard input to a text object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITextInputTraits : NSObjectProtocol
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Overview

For a custom text object to support keyboard input, it must adopt this protocol to interact properly with the text-input management system. The [`UITextField`](uitextfield.md) and [`UITextView`](uitextview.md) classes automatically support this protocol.

## Topics

### Configuring the keyboard appearance
- [var keyboardType: UIKeyboardType](uitextinputtraits/keyboardtype.md)
  The keyboard type for the text object.
- [enum UIKeyboardType](uikeyboardtype.md)
  Constants that specify the type of keyboard to display for a text-based view.
- [var keyboardAppearance: UIKeyboardAppearance](uitextinputtraits/keyboardappearance.md)
  The appearance style of the keyboard for the text object.
- [enum UIKeyboardAppearance](uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [var returnKeyType: UIReturnKeyType](uitextinputtraits/returnkeytype.md)
  The visible title of the Return key.
- [enum UIReturnKeyType](uireturnkeytype.md)
  Constants that specify the text string that displays in the Return key of a keyboard.
- [var textContentType: UITextContentType!](uitextinputtraits/textcontenttype.md)
  The semantic meaning for a text input area.
- [struct UITextContentType](uitextcontenttype.md)
  Constants that identify the semantic meaning for a text-entry area.
### Managing the keyboard behavior
- [var isSecureTextEntry: Bool](uitextinputtraits/issecuretextentry.md)
  A Boolean value that indicates whether a text object disables copying, and in some cases, prevents recording/broadcasting and also hides the text.
- [var enablesReturnKeyAutomatically: Bool](uitextinputtraits/enablesreturnkeyautomatically.md)
  A Boolean value that indicates whether the system automatically enables the Return key when the user enters text.
### Managing spelling and autocorrection
- [var autocapitalizationType: UITextAutocapitalizationType](uitextinputtraits/autocapitalizationtype.md)
  The autocapitalization style for the text object.
- [enum UITextAutocapitalizationType](uitextautocapitalizationtype.md)
  The autocapitalization behavior of a text-based view.
- [var autocorrectionType: UITextAutocorrectionType](uitextinputtraits/autocorrectiontype.md)
  The autocorrection style for the text object.
- [enum UITextAutocorrectionType](uitextautocorrectiontype.md)
  The autocorrection behavior of a text-based view.
- [var spellCheckingType: UITextSpellCheckingType](uitextinputtraits/spellcheckingtype.md)
  The spell-checking style for the text object.
- [enum UITextSpellCheckingType](uitextspellcheckingtype.md)
  The spell-checking behavior of a text-based view.
- [var inlinePredictionType: UITextInlinePredictionType](uitextinputtraits/inlinepredictiontype.md)
  The behavior of inline text predictions for a text-entry area.
- [enum UITextInlinePredictionType](uitextinlinepredictiontype.md)
  Constants that identify the behavior of inline text predictions for a text-entry area.
### Configuring the autoformatting behaviors
- [var smartQuotesType: UITextSmartQuotesType](uitextinputtraits/smartquotestype.md)
  The configuration state for smart quotes.
- [enum UITextSmartQuotesType](uitextsmartquotestype.md)
  Constants that indicate whether to enable or disable smart quotes.
- [var smartDashesType: UITextSmartDashesType](uitextinputtraits/smartdashestype.md)
  The configuration state for smart dashes.
- [enum UITextSmartDashesType](uitextsmartdashestype.md)
  Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [var smartInsertDeleteType: UITextSmartInsertDeleteType](uitextinputtraits/smartinsertdeletetype.md)
  The configuration state for the smart insertion and deletion of space characters.
- [enum UITextSmartInsertDeleteType](uitextsmartinsertdeletetype.md)
  Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.
### Configuring the writing tools experience
- [var writingToolsBehavior: UIWritingToolsBehavior](uitextinputtraits/writingtoolsbehavior.md)
  The writing tools experience to support in the current view.
- [enum UIWritingToolsBehavior](uiwritingtoolsbehavior.md)
  Constants that specify the writing tools experience for the underlying view.
### Configuring Smart Replies
- [var conversationContext: UIConversationContext?](uitextinputtraits/conversationcontext.md)
  A reference to a conversation, such as a mail or messaging thread.
### Configuring Password AutoFill
- [Password AutoFill](../Security/password-autofill.md)
  Streamline your app’s login and onboarding procedures.
- [class UITextInputPasswordRules](uitextinputpasswordrules.md)
  A class that represents password rules for a text input field.
### Configuring math expression completion
- [var mathExpressionCompletionType: UITextMathExpressionCompletionType](uitextinputtraits/mathexpressioncompletiontype.md)
- [enum UITextMathExpressionCompletionType](uitextmathexpressioncompletiontype.md)
### Instance Properties
- [var allowedWritingToolsResultOptions: UIWritingToolsResultOptions](uitextinputtraits/allowedwritingtoolsresultoptions.md)
- [var passwordRules: UITextInputPasswordRules?](uitextinputtraits/passwordrules.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIKeyInput](uikeyinput.md)
- [UITextDocumentProxy](uitextdocumentproxy.md)
- [UITextDraggable](uitextdraggable.md)
- [UITextDroppable](uitextdroppable.md)
- [UITextInput](uitextinput.md)
### Conforming Types
- [UISearchBar](uisearchbar.md)
- [UISearchTextField](uisearchtextfield.md)
- [UITextField](uitextfield.md)
- [UITextView](uitextview.md)

## See Also

- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [class UITextInputContext](uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputMode](uitextinputmode.md)
  The current text input mode.
- [class UITextInputAssistantItem](uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [class UIDictationPhrase](uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits)*