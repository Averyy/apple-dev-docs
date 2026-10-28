# typeText(_:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Types a string into the element.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
func typeText(_ text: String)
```

```objc
- (void) typeText:(NSString *) text;
```

## Discussion

The element or a descendant must have keyboard focus; otherwise the system raises an error. This API discards any modifiers set in the current context by [`perform(withKeyModifiers:block:)`](./perform%28withkeymodifiers,block%29.md) so that it strictly interprets the provided text. To input keys with modifier flags, use  [`typeKey(_:modifierFlags:)`](./typekey%28_,modifierflags%29-6gaoi.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/typetext(_:))*