# UISearchTextField

**Framework**: Uikit  
**Kind**: class

A view for displaying and editing text and search tokens.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISearchTextField
```

#### Overview

Use a search text field to display search criteria represented as text and tokens, and allow the user to edit that criteria. Tokens are discrete representations of nontextual content that your app can create and use to represent filters that limit the search results. Tokens always occur contiguously before any text in the search field.

[`UISearchBar`](uisearchbar.md) hosts a search text field, but you may also use a search text field in other roles, such as the title view of a [`UINavigationItem`](uinavigationitem.md).

> **Note**:  The search field assigns text positions ([`UITextPosition`](uitextposition.md)) to tokens as well as text so that users can interact with tokens using selection gestures and keyboard input. If the current selection includes any tokens, [`selectedTextRange`](uitextinput/selectedtextrange.md) includes their positions. Use the search field’s [`textualRange`](uisearchtextfield/textualrange.md) property to access the range of just the text without the tokens.

Tokens can be programmatically selected by including their position in a range assigned to the [`selectedTextRange`](uitextinput/selectedtextrange.md) property.

## Topics

### Converting text into tokens
- [func replaceTextualPortion(of: UITextRange, with: UISearchToken, at: Int)](uisearchtextfield/replacetextualportion(of:with:at:).md)
  Converts text in a search field into a search token.
- [var textualRange: UITextRange](uisearchtextfield/textualrange.md)
  The range of the field’s text content.
### Supporting token interactions
- [var allowsDeletingTokens: Bool](uisearchtextfield/allowsdeletingtokens.md)
  A Boolean that indicates whether the user can remove tokens from the search field.
- [var allowsCopyingTokens: Bool](uisearchtextfield/allowscopyingtokens.md)
  A Boolean that indicates whether the user can copy or drag tokens from the search field.
- [var delegate: (any UITextFieldDelegate)?](uitextfield/delegate.md)
  The text field’s delegate.
- [protocol UISearchTextFieldDelegate](uisearchtextfielddelegate.md)
  The interface for the delegate of a search field.
- [protocol UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md)
  A protocol that supports pasting tokens.
### Adding and removing tokens
- [var tokens: [UISearchToken]](uisearchtextfield/tokens.md)
  The collection of tokens in the search text field.
- [func insertToken(UISearchToken, at: Int)](uisearchtextfield/inserttoken(_:at:).md)
  Adds a search token at a specific index.
- [func removeToken(at: Int)](uisearchtextfield/removetoken(at:).md)
  Removes a particular search token from the search text field.
### Customizing token behavior
- [var tokenBackgroundColor: UIColor!](uisearchtextfield/tokenbackgroundcolor.md)
  The background color for all tokens in the search text field.
- [func tokens(in: UITextRange) -> [UISearchToken]](uisearchtextfield/tokens(in:).md)
  Returns the search field’s tokens that are within a given range.
- [func positionOfToken(at: Int) -> UITextPosition](uisearchtextfield/positionoftoken(at:).md)
  Converts a token index into a text position.
### Providing search suggestions
- [var searchSuggestions: [any UISearchSuggestion]?](uisearchtextfield/searchsuggestions.md)
  A list of suggestions to offer as shortcuts below the search field.

## Relationships

### Inherits From
- [UITextField](uitextfield.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UIKeyInput](uikeyinput.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UILetterformAwareAdjusting](uiletterformawareadjusting.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITextDraggable](uitextdraggable.md)
- [UITextDroppable](uitextdroppable.md)
- [UITextInput](uitextinput.md)
- [UITextInputTraits](uitextinputtraits.md)
- [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UISearchToken](uisearchtoken.md)
  Search criteria in a search text field, represented by text and an optional icon.
- [protocol UISearchTextFieldDelegate](uisearchtextfielddelegate.md)
  The interface for the delegate of a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uisearchtextfield)*