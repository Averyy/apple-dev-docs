# typeText(_:)

**Framework**: XCUIAutomation  
**Kind**: method

Types a string into the element.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func typeText(_ text: String)
```

#### Discussion

The element or a descendant must have keyboard focus; otherwise the system raises an error. This API discards any modifiers set in the current context by [`perform(withKeyModifiers:block:)`](xcuielement/perform(withkeymodifiers:block:).md) so that it strictly interprets the provided text. To input keys with modifier flags, use  [`typeKey(_:modifierFlags:)`](xcuielement/typekey(_:modifierflags:)-6gaoi.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/typetext(_:))*