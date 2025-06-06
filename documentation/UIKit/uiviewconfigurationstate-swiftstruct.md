# UIViewConfigurationState

**Framework**: UIKit  
**Kind**: struct

A structure that encapsulates a view’s state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct UIViewConfigurationState
```

#### Overview

A view configuration state encompasses a trait collection along with all of the common states that affect a view’s appearance — states like selected, focused, or disabled. A view configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a view configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [`configurationState`](uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a view configuration state by defining a custom state key using [`UIConfigurationStateCustomKey`](uiconfigurationstatecustomkey.md).

## Topics

### Managing view configuration states
- [var isSelected: Bool](uiviewconfigurationstate-swift.struct/isselected.md)
  A Boolean value that indicates whether the view is in a selected state.
- [var isHighlighted: Bool](uiviewconfigurationstate-swift.struct/ishighlighted.md)
  A Boolean value that indicates whether the view is in a highlighted state.
- [var isFocused: Bool](uiviewconfigurationstate-swift.struct/isfocused.md)
  A Boolean value that indicates whether the view is in a focused state.
- [var isDisabled: Bool](uiviewconfigurationstate-swift.struct/isdisabled.md)
  A Boolean value that indicates whether the view is in a disabled state.
- [var isPinned: Bool](uiviewconfigurationstate-swift.struct/ispinned.md)
  A Boolean value that indicates whether the view is in a pinned state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## See Also

- [struct UICellConfigurationState](uicellconfigurationstate-swift.struct.md)
  A structure that encapsulates a cell’s state.
- [protocol UIConfigurationState](uiconfigurationstate-8d7pd.md)
  The requirements for an object that encapsulates a view’s state.
- [struct UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewconfigurationstate-swift.struct)*